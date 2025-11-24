# Adding Different Method Implementations to True and False

How to add a method to True and False with different implementations for each.

---

## Option 1: Add Method to bool Class (checks self internally)

The simplest approach - add one method to `bool` that behaves differently based on the value:

```python
from forbiddenfruit import curse

def si_verdadero(self, func):
    """Different implementation based on True/False"""
    if self:  # If True
        return func()
    else:  # If False
        return self

curse(bool, "si_verdadero", si_verdadero)

# Now they behave differently
True.si_verdadero(lambda: print("¡Ejecutado!"))  # Prints: ¡Ejecutado!
False.si_verdadero(lambda: print("No se ejecuta"))  # Returns False, prints nothing
```

---

## Option 2: Attach Different Functions to True and False Instances

Use ctypes to attach different bound methods directly to the singleton objects:

```python
import ctypes
import types

# Get True's instance dict (if it exists)
class PyObject(ctypes.Structure):
    _fields_ = [
        ("ob_refcnt", ctypes.c_ssize_t),
        ("ob_type", ctypes.c_void_p)
    ]

class PyBoolObject(PyObject):
    _fields_ = [
        ("ob_size", ctypes.c_ssize_t),
        ("ob_digit", ctypes.c_long),
        ("__dict__", ctypes.py_object)  # May not exist for bool!
    ]

# Define different implementations
def true_implementation(func):
    print("True: executing function")
    return func()

def false_implementation(func):
    print("False: not executing")
    return None

# Try to attach to instances (this likely won't work for bool singletons)
# Bool objects don't have __dict__ attribute
try:
    True.__dict__['si_verdadero'] = true_implementation
except AttributeError:
    print("Can't add to True's __dict__ - it doesn't exist!")
```

**Problem**: `True` and `False` don't have instance `__dict__` attributes, so this won't work.

---

## Option 3: Store Implementations in External Dict (Recommended)

Since you can't attach different methods to the singleton instances, use an external registry:

```python
from forbiddenfruit import curse

# Registry of implementations
_bool_implementations = {
    True: lambda func: func(),  # True executes
    False: lambda func: None     # False doesn't
}

def si_verdadero(self, func):
    """Dispatch to different implementations"""
    impl = _bool_implementations[self]
    return impl(func)

curse(bool, "si_verdadero", si_verdadero)

# Test
True.si_verdadero(lambda: print("True ejecuta"))   # Prints: True ejecuta
False.si_verdadero(lambda: print("False no"))       # Prints nothing
```

You can make implementations more sophisticated:

```python
from forbiddenfruit import curse

class TrueImplementation:
    def si_verdadero(self, func):
        print(">>> Ejecutando porque soy True")
        result = func()
        print(">>> Terminado")
        return result

    def si_falso(self, func):
        print(">>> No ejecuto porque soy True")
        return None

class FalseImplementation:
    def si_verdadero(self, func):
        print(">>> No ejecuto porque soy False")
        return None

    def si_falso(self, func):
        print(">>> Ejecutando porque soy False")
        result = func()
        print(">>> Terminado")
        return result

# Registry
_impls = {
    True: TrueImplementation(),
    False: FalseImplementation()
}

def si_verdadero(self, func):
    return _impls[self].si_verdadero(func)

def si_falso(self, func):
    return _impls[self].si_falso(func)

curse(bool, "si_verdadero", si_verdadero)
curse(bool, "si_falso", si_falso)

# Test
True.si_verdadero(lambda: print("Hola desde True"))
# >>> Ejecutando porque soy True
# Hola desde True
# >>> Terminado

False.si_verdadero(lambda: print("Hola desde False"))
# >>> No ejecuto porque soy False

True.si_falso(lambda: print("Hola"))
# >>> No ejecuto porque soy True

False.si_falso(lambda: print("Adiós"))
# >>> Ejecutando porque soy False
# Adiós
# >>> Terminado
```

---

## Option 4: Monkey-patch with Descriptor Protocol

Use a descriptor to provide different behavior:

```python
from forbiddenfruit import curse

class BoolMethodDispatcher:
    """Descriptor that dispatches to different implementations"""

    def __init__(self, true_impl, false_impl):
        self.true_impl = true_impl
        self.false_impl = false_impl

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        # Return different bound method based on value
        impl = self.true_impl if obj else self.false_impl
        return lambda func: impl(obj, func)

# Different implementations
def when_true(self, func):
    print(f"Ejecutando porque {self} es True")
    return func()

def when_false(self, func):
    print(f"No ejecutando porque {self} es False")
    return self

# Create dispatcher
dispatcher = BoolMethodDispatcher(when_true, when_false)

# This won't work directly because we can't use descriptors on bool class properly
# But we can simulate it with a regular method:
def si_verdadero(self, func):
    if self:
        print(f"Ejecutando porque {self} es True")
        return func()
    else:
        print(f"No ejecutando porque {self} es False")
        return self

curse(bool, "si_verdadero", si_verdadero)
```

---

## Option 5: Multiple Dispatch with Type Checking

Use the actual identity of True/False:

```python
from forbiddenfruit import curse

def si_verdadero(self, func):
    """Check identity to dispatch"""
    if self is True:
        print(">>> Implementación específica de True")
        return func()
    elif self is False:
        print(">>> Implementación específica de False")
        return self
    else:
        # Handle other bool values (shouldn't happen)
        return func() if self else self

curse(bool, "si_verdadero", si_verdadero)

# Test
True.si_verdadero(lambda: print("¡Hola!"))
# >>> Implementación específica de True
# ¡Hola!

False.si_verdadero(lambda: print("¡Hola!"))
# >>> Implementación específica de False
```

---

## Complete Example: Ruby-style Methods

```python
from forbiddenfruit import curse

# Implementation registry
implementations = {
    True: {
        'entonces': lambda func: func(),
        'si_no': lambda func: None,
    },
    False: {
        'entonces': lambda func: None,
        'si_no': lambda func: func(),
    }
}

def entonces(self, func):
    """Execute func if True"""
    result = implementations[self]['entonces'](func)
    return self  # For chaining

def si_no(self, func):
    """Execute func if False"""
    result = implementations[self]['si_no'](func)
    return self  # For chaining

curse(bool, "entonces", entonces)
curse(bool, "si_no", si_no)

# Ruby-style chaining
x = 10

(x > 5).entonces(lambda: print("Mayor que 5")).si_no(lambda: print("Menor o igual"))
# Output: Mayor que 5

(x < 3).entonces(lambda: print("Menor que 3")).si_no(lambda: print("Mayor o igual"))
# Output: Mayor o igual
```

---

## Summary

| Approach | Complexity | Performance | Flexibility |
|----------|-----------|-------------|-------------|
| **Internal if-check** | ⭐ Simple | ⭐⭐⭐ Fast | ⭐⭐ Limited |
| **External registry** | ⭐⭐ Moderate | ⭐⭐ Good | ⭐⭐⭐ High |
| **Identity check** | ⭐ Simple | ⭐⭐⭐ Fast | ⭐⭐ Moderate |

**Recommendation**: Use the **external registry** approach (Option 3) if you need complex, separate implementations. Use **internal if-check** (Option 1) for simple cases.

The key insight is that since `True` and `False` are singletons and share the same class (`bool`), you can't truly give them different method objects. Instead, you add one method to `bool` that dispatches to different logic based on the value.
