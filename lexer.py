import re

def get_tokens(code):
    # Requirement: Minimum 10 different types of tokens
    token_specification = [
        ('VAR_DEC',   r':\)'),          # :)
        ('VAR_UPD',   r':/'),          # :/
        ('IF',        r':\('),         # :(
        ('ELSE',      r':\|'),         # :|
        ('LOOP',      r'@_@'),         # @_@
        ('PRINT',     r'xD'),          # xD
        ('TYPE',      r'o_o|OwO|\^-\^'), # o_o, OwO, ^-^
        ('EOL',       r'~'),           # ~
        ('BLOCK_S',   r'\['),          # [
        ('BLOCK_E',   r'\]'),          # ]
        ('STRING',    r'\+.*?\+'),     # +Text+
        ('NUMBER',    r'\d+'),         # Integers
        ('IDENTIFIER',r'[a-zA-Z_]\w*'),# Variables
        ('OP',        r'[+\-*/><=]+'), # Operators
        ('SKIP',      r'\s+'),         # Whitespace
        ('COMMENT',   r'\(⊙_⊙\).*?\(⊙_⊙\)'), # (⊙_⊙) Text (⊙_⊙)
    ]
    
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tokens = []
    
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind != 'SKIP' and kind != 'COMMENT':
            tokens.append({'type': kind, 'value': value})
    return tokens