# -*- coding: utf-8 -*-
# SOLUÇÃO DO PROBLEMA COM ARQUIVO

arquivo = open("../ExercíciosURI/Exercicio1789/entrada.txt", "r")

L = arquivo.readline()
V = arquivo.readline()
V = V.split(" ")

arquivo = arquivo.write(10)
print(arquivo)

arquivo.close()

entrada = [int(entrada) for entrada in V]

lesmaRapida = 0

if L >= 1 and L <= 500:
	entrada.sort()
	lesmaRapida = entrada[len(entrada) - 1]

if lesmaRapida < 10:
	print("1")
elif lesmaRapida >= 10 and lesmaRapida < 20:
	print("2")
else:
	print("3")
"""
