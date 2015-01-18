import ast
import symtable


def get_stmts(module):
    lastlineno = None
    for stmt in reversed(module.body):
        if isinstance(stmt, ast.FunctionDef):
            yield (stmt.name, (stmt.lineno-1, (None if lastlineno is None else lastlineno)))
        lastlineno = stmt.lineno - 1


def get_imports(module):
    for stmt in module.body:
        if isinstance(stmt, ast.ImportFrom):
            assert stmt.level == 0
            assert '.' not in stmt.module
            for alias in stmt.names:
                assert alias.asname is None
                yield (alias.name, (stmt.module,alias.name))


def parse_module(module_name):
    filename = module_name + ".py"
    with open(filename, 'r') as f:
        source = f.read()

    srclines = source.splitlines()
    module = ast.parse(source, filename)
    table = symtable.symtable(source, filename, "exec")
    stmts = list(get_stmts(module))
    last_fun = stmts[0][0]
    lines = {name:"\n".join(srclines[s:e]).strip() for (name,(s,e)) in stmts}
    imports = dict(get_imports(module))

    def parse_dependencies(name):
        ns = table.lookup(name).get_namespace()
        for g in table.lookup(name).get_namespace().get_globals():
            if g in dir(__builtins__):
                continue

            if table.lookup(g).is_imported():
                imported = imports[g]
                if imported[0] != "leetcode":
                    yield imported
            else:
                yield (module_name, g)

    return last_fun, lines, {name:tuple(parse_dependencies(name)) for name in lines}


def get_module(modules, module_name):
    module = modules.get(module_name, None)
    if module is None:
        module = parse_module(module_name)
        modules[module_name] = module
    return module


def get_dependencies(modules, mf):
    return get_module(modules, mf[0])[2][mf[1]]


def get_lines(modules, mf):
    return get_module(modules, mf[0])[1][mf[1]]


def load_functions(module_name):
    modules = {}
    visited = set()

    root = (module_name, get_module(modules, module_name)[0])
    unresolved = [root]

    while unresolved:
        mf = unresolved[0]
        unresolved = unresolved[1:]
        if mf in visited:
            continue
        visited.add(mf)
        unresolved += get_dependencies(modules, mf)

    code = "\n\n".join(get_lines(modules, mf) for mf in visited)
    return root[1], code


def get_function_args(module_name, fun_name):
    filename = module_name + ".py"

    with open(filename, 'r') as f:
        source = f.read()

    module = ast.parse(source, filename)

    for stmt in module.body:
        if not isinstance(stmt, ast.FunctionDef):
            continue

        if stmt.name == fun_name:
            assert stmt.args.vararg is None
            assert stmt.args.kwarg is None
            assert not stmt.args.defaults
            return [arg.id for arg in stmt.args.args]


SOLUTION = """
class Solution:
    def {name}(self, {args}):
        return {name}({args})
"""


def main(filename):
    if filename.endswith(".py"):
        module_name = filename[:-3]
    else:
        module_name = filename

    fun_name, code = load_functions(module_name)
    args = get_function_args(module_name, fun_name)
    print "\n\n".join(
        [code.strip(),
         SOLUTION.format(name=fun_name, args=", ".join(args)).strip()])

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
