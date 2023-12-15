### A Pluto.jl notebook ###
# v0.16.4

using Markdown
using InteractiveUtils

# ╔═╡ 6a35c5b8-2ce0-11ec-3a8c-b5a25bab9f9b
using PyCall

# ╔═╡ e07e4a47-a3cc-4ca4-a946-29e7df33ec6d
md"""
# Y.si( If.no_existe() )
"""

# ╔═╡ 2cad8f45-d4ec-45e7-8a0d-253bb8409b39
md"""
*Para pensar:*

¿Cómo implementarían los objetos "True" y "False" bajo el modelo de Objetos que solo reciben y envían mensajes?
"""

# ╔═╡ 962dc41a-93db-4276-b73b-3051b066e98b
md"""
### Fuentes:

[*Dodge: “if” statements* en Python Patterns](https://python-patterns.guide/gang-of-four/composition-over-inheritance/#dodge-if-statements)

[The most critical Python code metric](https://stevedower.id.au/blog/most-critical-python-metric)

[Charla:  If Statements are a Code Smell](https://www.youtube.com/watch?v=P0kfKqMHioQ)

[Charla: Nothing is something](https://youtu.be/OMPfEXIlTVE?t=419)


[Paquete: Radon](https://pypi.org/project/radon/) para calcular métricas de nuestro código
"""

# ╔═╡ ddfe9405-60ce-4ee6-9531-822fbaebefeb
md"""
Este cuaderno utiliza el código del cuaderno de [Reactive Python](https://github.com/fonsp/disorganised-mess/blob/83470e6f8e944757bc064c87b115847bdbeb8300/reactive%20python.jl) por [@fonsp](https://github.com/fonsp)
"""

# ╔═╡ d3fe9870-ac9d-4871-b8cc-1361a446b0a5
import PyCall: interpolate_pycode, Py_file_input, make_fname, Py_eval_input, pynamespace, pyeval_

# ╔═╡ b9903477-5070-43eb-82a9-8b750f79c8fa
macro custom_py_str(code, options...)
    T = length(options) == 1 && 'o' in options[1] ? PyObject : PyAny
    code, locals = interpolate_pycode(code)
    input_type = '\n' in code ? Py_file_input : Py_eval_input
    fname = make_fname(@__FILE__)
    assignlocals = Expr(:block, [(isa(v,String) ?
                                  :(m[$v] = PyObject($(esc(ex)))) :
                                  nothing) for (v,ex) in locals]...)
    code_expr = Expr(:call, esc(:(Base.string)))
    i0 = firstindex(code)
    for i in sort!(collect(filter(k -> isa(k,Integer), keys(locals))))
        push!(code_expr.args, code[i0:prevind(code,i)], esc(locals[i]))
        i0 = i
    end
    push!(code_expr.args, code[i0:lastindex(code)])
    if input_type == Py_eval_input
        removelocals = Expr(:block, [:(delete!(m, $v)) for v in keys(locals)]...)
    else
        # if we are evaluating multi-line input, then it is not
        # safe to remove the local variables, because they might be referred
        # to in Python function definitions etc. that will be called later.
        removelocals = nothing
    end
    quote
        m = pynamespace(Main)
        $assignlocals
        ret = $T(pyeval_($code_expr, m, m, $input_type, $fname))
        $removelocals
        ret
    end
end

# ╔═╡ 688c93e7-b50f-4bb7-ab23-5686fd8ffb18
custom_py"""
1 + 1"""

# ╔═╡ d74aed51-9542-47aa-8c3d-fb634c1a0212
py_reads_writes = begin
	py"""
	import ast
	import functools
	
	
	
	class VariableAccess:
	    def __init__(self, reads, writes):
	        self.reads = frozenset(reads)
	        self.writes = frozenset(writes)
	    
	
	    @classmethod
	    def from_code(cls, code):
	        return cls.from_ast(ast.parse(code))
	    
	
	    @classmethod
	    def from_ast(cls, ast_node):
	        if isinstance(ast_node, ast.Name):
	            return cls(reads=[ast_node.id], writes=[])
	
	        if isinstance(ast_node, ast.Assign):
	            targets = cls.from_ast(ast_node.targets)
	            value = cls.from_ast(ast_node.value)
	            return cls(reads=value.reads, writes=targets.reads | targets.writes | value.writes)
	        if isinstance(ast_node, ast.AugAssign): # x += 3, for example
	            target = cls.from_ast(ast_node.target)
	            value = cls.from_ast(ast_node.value)
	            return cls(reads=value.reads, writes=target.reads | target.writes | value.writes)
	        
	        if isinstance(ast_node, ast.ImportFrom):
	            if ast_node.names[0].name == '*':
	                raise NotImplementedError('"import *" is not supported yet!')
	            return cls.from_ast(ast_node.names)
	        if isinstance(ast_node, ast.alias):
	            return cls(reads=[], writes=[ast_node.asname or ast_node.name])
	        
	        if isinstance(ast_node, ast.ClassDef):
	            bases = cls.from_ast(ast_node.bases)
	            keywords = cls.from_ast(ast_node.keywords)
	            decorators = cls.from_ast(ast_node.decorator_list)
	            body = cls.from_ast(ast_node.body) # no name shadowing because of "if x: y = 10"
	            return cls(
	                reads=bases.reads | keywords.reads | decorators.reads | body.reads,
	                writes=[ast_node.name]
	            )
	        
	        if isinstance(ast_node, ast.Lambda):
	            arguments = cls.from_ast(ast_node.args)
	            body = cls.from_ast(ast_node.body)
	            return cls(reads=arguments.reads | (body.reads - arguments.writes), writes=[])
	        if isinstance(ast_node, ast.FunctionDef):
	            decorators = cls.from_ast(ast_node.decorator_list)
	            arguments = cls.from_ast(ast_node.args)
	            body = cls.from_ast(ast_node.body)
	            return cls(reads=decorators.reads | arguments.reads | (body.reads - arguments.writes), writes=[ast_node.name])
	        if isinstance(ast_node, ast.arg):
	            return cls(reads=[], writes=[ast_node.arg])
	
	        if isinstance(ast_node, ast.For):
	            target = cls.from_ast(ast_node.target) # no name shadowing - target is actually written to
	            iterable = cls.from_ast(ast_node.iter)
	            body = cls.from_ast(ast_node.body)
	            else_body = cls.from_ast(ast_node.orelse)
	            return cls(
	                reads=iterable.reads | body.reads | else_body.reads,
	                writes=target.reads | target.writes | iterable.writes | body.writes | else_body.writes
	            )
	        
	        if isinstance(ast_node, ast.ListComp):
	            element = cls.from_ast(ast_node.elt)
	            generators = cls.from_ast(ast_node.generators)
	            return element | generators # TODO: name shadowing
	        if isinstance(ast_node, ast.SetComp):
	            element = cls.from_ast(ast_node.elt)
	            generators = cls.from_ast(ast_node.generators)
	            return element | generators # TODO: name shadowing
	        if isinstance(ast_node, ast.DictComp):
	            key = cls.from_ast(ast_node.key)
	            value = cls.from_ast(ast_node.value)
	            generators = cls.from_ast(ast_node.generators)
	            return key | value | generators # TODO: name shadowing
	        if isinstance(ast_node, ast.comprehension):
	            target = cls.from_ast(ast_node.target)
	            iterable = cls.from_ast(ast_node.iter)
	            conditions = cls.from_ast(ast_node.ifs)
	            return target | iterable | conditions # TODO: name shadowing
	        
	        if isinstance(ast_node, list):
	            return functools.reduce(
	                cls.__or__,
	                [cls.from_ast(sub_ast) for sub_ast in ast_node],
	                cls(reads=[], writes=[])
	            )
	        
	        for node_type, children in node_children.items():
	            if isinstance(ast_node, node_type):
	                return cls.from_ast([getattr(ast_node, child) for child in children])
	        
	        raise NotImplementedError(f'Cannot parse {type(ast_node)} yet!')
	
	
	    def __eq__(self, other):
	        return self.reads == other.reads and self.writes == other.writes
	
	
	    def __or__(self, other):
	        return type(self)(reads=self.reads | other.reads, writes=self.writes | other.writes)
	    
	
	    def __repr__(self):
	        return f'{type(self).__name__}(reads={list(self.reads)}, writes={list(self.writes)})'
	
	
	node_children = {
	    ast.Constant: [],
	    ast.Pass: [],
	    type(None): [],
	    ast.Expression: ['body'],
	    ast.Expr: ['value'],
	    ast.Module: ['body'],
	    ast.Import: ['names'],
	    ast.Attribute: ['value'],
	    ast.arguments: ['posonlyargs', 'args', 'vararg', 'kwonlyargs', 'kwarg', 'defaults', 'kw_defaults'],
	    ast.Return: ['value'],
	    ast.Call: ['func', 'args', 'keywords'],
	    ast.keyword: ['value'],
	    ast.If: ['test', 'body', 'orelse'],
	    ast.IfExp: ['test', 'body', 'orelse'],
	    ast.While: ['test', 'body', 'orelse'],
	    ast.Tuple: ['elts'],
	    ast.List: ['elts'],
	    ast.Set: ['elts'],
	    ast.Dict: ['keys', 'values'],
	    ast.JoinedStr: ['values'],
	    ast.FormattedValue: ['value'],
	    ast.Subscript: ['value', 'slice'],
	    ast.Index: ['value'],
	    ast.Slice: ['lower', 'upper', 'step'],
	    ast.UnaryOp: ['operand'],
	    ast.BinOp: ['left', 'right'],
	    ast.BoolOp: ['values'],
	    ast.Compare: ['left', 'comparators']
	}

	def reads_writes(code):
		va = VariableAccess.from_code(code)
		return [va.reads, va.writes]
	"""
	
	py"reads_writes"
end

# ╔═╡ 5c432b4e-60e0-4288-8d5a-42e364ce8d16
macro pyr_str(str)
	var"@custom_py_str"
	
	reads, writes = py_reads_writes(str)

	quote
		# if false
		$([let
			julia_s = Symbol("py#var_", py_s)
			import_code = """$(py_s) = \$(s)\n"""
			esc(quote
				let s = $(julia_s) # for pluto to recognise
				@custom_py_str($(import_code)) # load stored PyObject into python using that name
				end
			end)
		end for py_s in reads]...)
		# end
		
		output = @custom_py_str($(str))
		
		# if false

		$([let
			julia_s = Symbol("py#var_", py_s)
			import_code = "$(py_s)"
			esc(quote
				$(julia_s) = @custom_py_str($(import_code)) # store PyObject as julia object, so that it can use Pluto's reactivity
			end)
		end for py_s in writes]...)
		# end
		output
	end
end

# ╔═╡ 27975ccd-5336-4ec8-9cf4-fc5f326dfc1a
pyr"""
datos_ingresados = [
	'A',
]
"""

# ╔═╡ ef76d0a8-17cd-449f-9624-bdab7202c851
pyr"datos_ingresados"

# ╔═╡ 7899aed2-abc1-4a4e-b720-a81f2fcb54cd
pyr"""
def procesar(elemento):
	return 
"""

# ╔═╡ 5b108831-8ec7-42e2-a75a-594fb6054f2f
pyr"""procesar(datos_ingresados[-1])"""

# ╔═╡ 0030198b-a1c2-4cfc-b557-451f400e3980
pyr"""
x=None
"""

# ╔═╡ 48f9fbb8-9d24-491d-a835-eefcf1607675
pyr"""
def aplicar(f, y):
	return [ f(x) for x in y]
"""

# ╔═╡ 5a500747-dc63-44a2-bca6-cb730131ba11
pyr"""aplicar(procesar,datos_ingresados)"""

# ╔═╡ 5f5ab869-c551-42d3-9325-86ecdc424c9b
macro pyr_old_str(str)
	var"@custom_py_str"
	
	reads, writes = py_reads_writes(str)

	quote
		if false
		$([esc(:($(Symbol("#py", s)) = 1))  for s in writes]...)
		$([esc(:($(Symbol("#py", s))))  for s in reads]...)
		end
		@custom_py_str($(str))
	end
end

# ╔═╡ 00000000-0000-0000-0000-000000000001
PLUTO_PROJECT_TOML_CONTENTS = """
[deps]
PyCall = "438e738f-606a-5dbb-bf0a-cddfbfd45ab0"

[compat]
PyCall = "~1.92.3"
"""

# ╔═╡ 00000000-0000-0000-0000-000000000002
PLUTO_MANIFEST_TOML_CONTENTS = """
# This file is machine-generated - editing it directly is not advised

[[Base64]]
uuid = "2a0f44e3-6c83-55bd-87e4-b1978d98bd5f"

[[Conda]]
deps = ["JSON", "VersionParsing"]
git-tree-sha1 = "299304989a5e6473d985212c28928899c74e9421"
uuid = "8f4d0f93-b110-5947-807f-2305c1781a2d"
version = "1.5.2"

[[Dates]]
deps = ["Printf"]
uuid = "ade2ca70-3891-5945-98fb-dc099432e06a"

[[JSON]]
deps = ["Dates", "Mmap", "Parsers", "Unicode"]
git-tree-sha1 = "8076680b162ada2a031f707ac7b4953e30667a37"
uuid = "682c06a0-de6a-54ab-a142-c8b1cf79cde6"
version = "0.21.2"

[[Libdl]]
uuid = "8f399da3-3557-5675-b5ff-fb832c97cbdb"

[[LinearAlgebra]]
deps = ["Libdl"]
uuid = "37e2e46d-f89d-539d-b4ee-838fcccc9c8e"

[[MacroTools]]
deps = ["Markdown", "Random"]
git-tree-sha1 = "5a5bc6bf062f0f95e62d0fe0a2d99699fed82dd9"
uuid = "1914dd2f-81c6-5fcd-8719-6d5c9610ff09"
version = "0.5.8"

[[Markdown]]
deps = ["Base64"]
uuid = "d6f4376e-aef5-505a-96c1-9c027394607a"

[[Mmap]]
uuid = "a63ad114-7e13-5084-954f-fe012c677804"

[[Parsers]]
deps = ["Dates"]
git-tree-sha1 = "98f59ff3639b3d9485a03a72f3ab35bab9465720"
uuid = "69de0a69-1ddd-5017-9359-2bf0b02dc9f0"
version = "2.0.6"

[[Printf]]
deps = ["Unicode"]
uuid = "de0858da-6303-5e67-8744-51eddeeeb8d7"

[[PyCall]]
deps = ["Conda", "Dates", "Libdl", "LinearAlgebra", "MacroTools", "Serialization", "VersionParsing"]
git-tree-sha1 = "169bb8ea6b1b143c5cf57df6d34d022a7b60c6db"
uuid = "438e738f-606a-5dbb-bf0a-cddfbfd45ab0"
version = "1.92.3"

[[Random]]
deps = ["Serialization"]
uuid = "9a3f8284-a2c9-5f02-9a11-845980a1fd5c"

[[Serialization]]
uuid = "9e88b42a-f829-5b0c-bbe9-9e923198166b"

[[Unicode]]
uuid = "4ec0a83e-493e-50e2-b9ac-8f72acf5a8f5"

[[VersionParsing]]
git-tree-sha1 = "80229be1f670524750d905f8fc8148e5a8c4537f"
uuid = "81def892-9a0e-5fdd-b105-ffc91e053289"
version = "1.2.0"
"""

# ╔═╡ Cell order:
# ╟─e07e4a47-a3cc-4ca4-a946-29e7df33ec6d
# ╠═27975ccd-5336-4ec8-9cf4-fc5f326dfc1a
# ╠═ef76d0a8-17cd-449f-9624-bdab7202c851
# ╠═7899aed2-abc1-4a4e-b720-a81f2fcb54cd
# ╠═5b108831-8ec7-42e2-a75a-594fb6054f2f
# ╠═5a500747-dc63-44a2-bca6-cb730131ba11
# ╠═48f9fbb8-9d24-491d-a835-eefcf1607675
# ╟─2cad8f45-d4ec-45e7-8a0d-253bb8409b39
# ╠═962dc41a-93db-4276-b73b-3051b066e98b
# ╟─ddfe9405-60ce-4ee6-9531-822fbaebefeb
# ╟─0030198b-a1c2-4cfc-b557-451f400e3980
# ╟─6a35c5b8-2ce0-11ec-3a8c-b5a25bab9f9b
# ╟─5c432b4e-60e0-4288-8d5a-42e364ce8d16
# ╟─5f5ab869-c551-42d3-9325-86ecdc424c9b
# ╟─d3fe9870-ac9d-4871-b8cc-1361a446b0a5
# ╟─688c93e7-b50f-4bb7-ab23-5686fd8ffb18
# ╟─b9903477-5070-43eb-82a9-8b750f79c8fa
# ╟─d74aed51-9542-47aa-8c3d-fb634c1a0212
# ╟─00000000-0000-0000-0000-000000000001
# ╟─00000000-0000-0000-0000-000000000002
