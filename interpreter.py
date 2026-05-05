import sys
import json
import lexer
import parser

def execute(ast):
    vars_store = {}
    for node in ast:
        if node['type'] == "Assignment":
            vars_store[node['name']] = node['value'].strip('+')
        elif node['type'] == "Print":
            val = node['value']
            print(vars_store.get(val, val.strip('+')))
        elif node['type'] == "Loop":
            for _ in range(int(node['iterations'])):
                print("Looping... (⊙_⊙)")

def main():
    if len(sys.argv) < 2: return
    with open(sys.argv[1], 'r') as f:
        code = f.read()
    
    # Flow: String -> Tokens -> AST -> Execution
    tokens = lexer.get_tokens(code)
    ast = parser.build_ast(tokens)
    
    # Requirement: Output AST as JSON
    print("--- AST JSON ---")
    print(json.dumps(ast, indent=2))
    
    print("\n--- EXECUTION ---")
    execute(ast)

if __name__ == "__main__":
    main()
