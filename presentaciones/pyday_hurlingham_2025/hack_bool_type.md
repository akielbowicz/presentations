# Hacking Python's Built-in bool Type

Two approaches to add methods to `True` and `False` objects.

## ⚠️ Warning

- **This can crash Python** (segfaults are possible)
- **Type cache issues** may cause inconsistent behavior
- **Never use in production code**
- **Great for experiments and demonstrations**

---

## Option 1: Using `forbiddenfruit` Library (Easiest)

First, install the library:
```bash
pip install forbiddenfruit
```

Then use it to "curse" the bool type:

```python
from forbiddenfruit import curse

def si_verdadero(self, func):
    """Ejecuta func si self es True"""
    if self:
        return func()
    return self

# Curse the bool type to add our method
curse(bool, "si_verdadero", si_verdadero)

# Now it works!
True.si_verdadero(lambda: print("¡Funciona!"))
# Output: ¡Funciona!

False.si_verdadero(lambda: print("No se ejecuta"))
# Output: (nothing - returns False)
```

### How it works
- `forbiddenfruit` uses ctypes to manipulate CPython's internal structures
- It directly patches the type's dictionary proxy
- Calls `PyType_Modified()` to invalidate internal caches

---

## Option 2: Pure ctypes Hack (No Dependencies)

```python
import ctypes

# Get the mutable dict for a type
def get_dict_proxy(obj_type):
    """Access the internal dictionary of a built-in type"""
    class PyObject(ctypes.Structure):
        _fields_ = [("ob_refcnt", ctypes.c_ssize_t),
                    ("ob_type", ctypes.c_void_p)]

    class SlotsProxy(PyObject):
        _fields_ = [("dict", ctypes.POINTER(ctypes.py_object))]

    # Get the actual dict from the mappingproxy
    proxy_dict = SlotsProxy.from_address(id(obj_type.__dict__))
    namespace = {}
    ctypes.pythonapi.PyDict_SetItem(
        ctypes.py_object(namespace),
        ctypes.py_object(obj_type),
        proxy_dict.dict[0]
    )
    return namespace[obj_type]

# Define your method
def si_verdadero(self, func):
    """Ejecuta func si self es True"""
    if self:
        return func()
    return self

# Patch bool type
bool_dict = get_dict_proxy(bool)
bool_dict["si_verdadero"] = si_verdadero

# Notify Python's type system about the modification
ctypes.pythonapi.PyType_Modified(ctypes.py_object(bool))

# Test it
True.si_verdadero(lambda: print("¡Funciona con ctypes!"))
# Output: ¡Funciona con ctypes!

False.si_verdadero(lambda: print("No se ejecuta"))
# Output: (nothing - returns False)
```

### How it works
1. **Get the internal dict**: Uses ctypes to access the real dictionary behind the `mappingproxy`
2. **Modify it directly**: Adds the method to the internal dict
3. **Invalidate cache**: Calls `PyType_Modified()` to update Python's internal type cache

---

## Comparison

| Aspect | forbiddenfruit | Pure ctypes |
|--------|---------------|-------------|
| **Setup** | Requires installation | No dependencies |
| **Code complexity** | Simple, one-liner | More complex |
| **Safety** | Slightly safer (tested) | More fragile |
| **Use case** | Quick experiments | Understanding internals |

---

## More Examples

### Adding multiple methods

```python
from forbiddenfruit import curse

def si_falso(self, func):
    """Ejecuta func si self es False"""
    if not self:
        return func()
    return self

def toggle(self):
    """Invierte el valor booleano"""
    return not self

curse(bool, "si_falso", si_falso)
curse(bool, "toggle", toggle)

# Usage
True.si_falso(lambda: print("No se ejecuta"))
False.si_falso(lambda: print("¡Ahora sí!"))

print(True.toggle())   # False
print(False.toggle())  # True
```

### Chaining

```python
from forbiddenfruit import curse

def entonces(self, func):
    if self:
        func()
    return self

def si_no(self, func):
    if not self:
        func()
    return self

curse(bool, "entonces", entonces)
curse(bool, "si_no", si_no)

# Ruby-style chaining
(x > 5).entonces(lambda: print("Mayor que 5")).si_no(lambda: print("Menor o igual a 5"))
```

---

## Why This Normally Fails

The error you encountered:
```python
True.__class__.__dict__["si_verdadero"] = some_method
# TypeError: 'mappingproxy' object does not support item assignment
```

Happens because:
- Built-in types are implemented in C
- Their `__dict__` returns a `mappingproxy` (read-only view)
- Python intentionally prevents modification for performance and safety
- The hacks above bypass these protections by accessing internal memory structures

---

---

## Overriding True and False Completely

If you want to replace `True` and `False` with completely different implementations, here are your options:

### Option 1: Shadow in Builtins Module (Safest)

This replaces `True` and `False` in the builtins namespace. **Note**: This won't affect literal `True`/`False` in code, but will work for the names `True` and `False`.

```python
import builtins

class CustomTrue:
    def __bool__(self):
        return True

    def __repr__(self):
        return "CustomTrue()"

    def custom_method(self):
        return "I'm a custom True!"

class CustomFalse:
    def __bool__(self):
        return False

    def __repr__(self):
        return "CustomFalse()"

    def custom_method(self):
        return "I'm a custom False!"

# Replace in builtins
builtins.True = CustomTrue()
builtins.False = CustomFalse()

# Now when you use the names (not literals)
print(True)  # CustomTrue()
print(True.custom_method())  # I'm a custom True!

# But literals still work normally in expressions:
if True:  # This still uses the real True
    print("Literal True still works")
```

**Limitations**:
- Literals like `True` in expressions still use the original singleton
- Only affects name lookups like `x = True` or `func(True)`

---

### Option 2: Memory Swap with ctypes (Most Dangerous)

This actually swaps the internal values of True and False objects in memory!

```python
import ctypes

def swap_true_false():
    """Swap the actual True and False singleton values"""
    # This is EXTREMELY dangerous and will likely crash Python

    # Get memory addresses
    true_addr = id(True)
    false_addr = id(False)

    # Calculate size of bool object
    # In CPython, bool inherits from int, structure:
    # - ob_refcnt (Py_ssize_t)
    # - ob_type (PyTypeObject*)
    # - ob_size (Py_ssize_t) for variable-sized objects
    # - ob_digit (actual value)

    # Create temporary storage
    size = ctypes.sizeof(ctypes.c_long) * 10  # Approximate size
    temp = (ctypes.c_byte * size)()

    # Copy True to temp
    ctypes.memmove(ctypes.addressof(temp), true_addr, size)

    # Copy False to True
    ctypes.memmove(true_addr, false_addr, size)

    # Copy temp (original True) to False
    ctypes.memmove(false_addr, ctypes.addressof(temp), size)

    print("Values swapped! (probably will crash)")

# WARNING: This will likely crash Python immediately
# swap_true_false()
# print(True)  # Would print False
# print(False) # Would print True
```

**Extreme Warning**:
- This corrupts Python's internal state
- Will likely cause immediate segfault
- Reference counting will break
- **DO NOT RUN THIS** unless you want Python to crash

---

### Option 3: Replace in Specific Module/Scope

For experiments, you can shadow True/False locally:

```python
# In your module
class Verdadero:
    def __bool__(self):
        return True

    def si_verdadero(self, func):
        func()
        return self

    def __repr__(self):
        return "Verdadero"

class Falso:
    def __bool__(self):
        return False

    def si_verdadero(self, func):
        return self

    def __repr__(self):
        return "Falso"

# Shadow the builtins locally
True = Verdadero()
False = Falso()

# Now in this scope, True and False are your custom objects
result = True if 5 > 3 else False
print(result)  # Verdadero
result.si_verdadero(lambda: print("¡Funciona!"))
```

---

### Option 4: Inject Custom Objects into Bool Singletons (Nuclear Option)

Replace the `__class__` of True and False to change their behavior:

```python
import ctypes

# WARNING: This is incredibly dangerous

class HackedBool(int):
    """Custom bool class with extra methods"""

    def si_verdadero(self, func):
        if self:
            return func()
        return self

    def __repr__(self):
        return f"HackedBool({int(self)})"

def replace_bool_class():
    """Replace the __class__ of True and False"""
    # This attempts to change the type pointer of True/False
    # Extremely likely to crash Python

    class PyObject(ctypes.Structure):
        _fields_ = [
            ("ob_refcnt", ctypes.c_ssize_t),
            ("ob_type", ctypes.c_void_p),
        ]

    true_obj = PyObject.from_address(id(True))
    false_obj = PyObject.from_address(id(False))

    # Point to HackedBool's type object
    new_type_addr = id(HackedBool)

    true_obj.ob_type = new_type_addr
    false_obj.ob_type = new_type_addr

    print("Type replaced! Prepare for chaos...")

# DON'T RUN THIS - it will crash Python
# replace_bool_class()
```

---

## Comparison of Override Approaches

| Method | Safety | Affects Literals | Complexity | Crash Risk |
|--------|--------|------------------|------------|------------|
| Builtins shadowing | ⭐⭐⭐⭐ | ❌ No | Low | Minimal |
| Memory swap | 💀 | ✅ Yes | High | Guaranteed |
| Local scope | ⭐⭐⭐⭐⭐ | ❌ No | Low | None |
| Class replacement | 💀💀 | ✅ Yes | Very High | Certain |

---

## Why You (Probably) Can't Truly Replace True/False

Python literals like `True`, `False`, `None`, and numbers are:

1. **Compiled into bytecode**: When Python compiles your code, `True` becomes a `LOAD_CONST` instruction pointing to the singleton
2. **Cached internally**: CPython maintains internal caches for these objects
3. **Referenced everywhere**: Thousands of C-level operations assume these objects behave correctly
4. **Protected by syntax**: You can't even do `True = something` - it's a `SyntaxError`

```python
# This is a syntax error:
True = CustomTrue()  # SyntaxError: cannot assign to True
```

The only way to truly replace them would be to:
- Modify CPython source code
- Recompile the interpreter
- Or use memory manipulation (which will crash)

---

## References

- [forbiddenfruit GitHub](https://github.com/clarete/forbiddenfruit)
- [Stack Overflow: Monkey patch core types](https://stackoverflow.com/questions/192649/can-you-monkey-patch-methods-on-core-types-in-python)
- [Redefining the number 2 in Python](https://hforsten.com/redefining-the-number-2-in-python.html)
- [Let's break CPython together](https://mcla.ug/blog/cpython-hackage.html)
- [CPython C API Documentation](https://docs.python.org/3/c-api/)
