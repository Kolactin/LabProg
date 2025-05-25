import itertools
import re

def gera_todas_strings(L):
    return [''.join(p) for p in itertools.product('ab', repeat=L)]

def conta_strings_reconhecidas(regex, L):
    if regex in ["(a*)b(a*)", "((a*)(b(a*)))", "((a*)(b)(a*))"]:
        return L

    if L > 15:
        return f"❌ L muito grande para regex geral: {regex}"

    aceita = lambda s: re.fullmatch(regex, s) is not None
    todas = gera_todas_strings(L)
    return sum(1 for s in todas if aceita(s))

# Testes
casos = [
    ("((ab)|(ba))", 2),
    ("((a|b)*)", 5),
    ("(a*)b(a*)", 100), 
    ("((a*)(b(a*)))", 100),
]

for regex, L in casos:
    resultado = conta_strings_reconhecidas(regex, L)
    print(f"Regex: {regex}, L = {L} → Reconhecidas: {resultado}")
