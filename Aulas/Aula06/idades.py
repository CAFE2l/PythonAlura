idades = [15, 19, 8, 22, 14, 10, 19, 25]


# for i in range(len(idades)):
#     print(i, idades[i])


usuarios = [
    ("guilherme", 15, 2010),
    ("daniela", 19, 2009),
    ("paulo", 8, 2011),
    ("maria", 22, 2008),
    ("joão", 14, 2012),
    ("ana", 10, 2013),
    ("carlos", 19, 2010),
    ("sofia", 25, 2005),
]

for nome, _, _ in usuarios:
    print(nome)


idades_crescente = sorted(idades)
idades_decrescente = sorted(idades, reverse=True)

print(idades_crescente)
print(idades_decrescente)
