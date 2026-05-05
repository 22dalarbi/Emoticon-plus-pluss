import json

def build_ast(tokens):
    ast = []
    i = 0
    # Requirement: Check 4 different grammars (Assignment, Print, Loop, If)
    while i < len(tokens):
        t = tokens[i]
        
        if t['type'] == 'VAR_DEC':
            ast.append({
                "type": "Assignment",
                "name": tokens[i+1]['value'],
                "var_type": tokens[i+2]['value'],
                "value": tokens[i+3]['value']
            })
            i += 5
        elif t['type'] == 'PRINT':
            ast.append({"type": "Print", "value": tokens[i+1]['value']})
            i += 3
        elif t['type'] == 'LOOP':
            ast.append({"type": "Loop", "iterations": tokens[i+1]['value']})
            i += 5
        elif t['type'] == 'IF':
            ast.append({"type": "IfStatement", "condition": tokens[i+1]['value']})
            i += 5
        else:
            i += 1
    return ast # This returns the tree as a list/dict that converts to JSON