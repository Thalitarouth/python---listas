# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:45:01 2022

@author: lab54

#Exemplo 1 

coleção = ["\n\nMaria",22,"anos e saláriosde R$",1287.98]
print(coleção[0])
print(coleção[1])
print(coleção[2])
print(coleção[3])


#Exercicio 1 

notas = [4.7,5.6,8.9,3.5,6.6,7.4,8.0,9.5]
soma = 0.0
i=0
while i<8:
    soma += notas[i]
    i +=1
print("i= ",i)
print(f"média:{soma/i: 5.2f}")

  
    #Exercicio 2 
    
notas = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
soma = 0.0
i=0
while i<8:
    notas[i]=float(input(f"entrar com o valor da nota {i}:"))
    soma +=notas[i]
    i+=1
    print("valor parcial da soma das notas =",soma)
    print(f"média:{soma/i:5.2f}")
    print("notas = ", notas)         
    


notas = [0.0,0.0,0.0,0.0,0.0]
soma = 0.0
i=0
while i<5:
    notas [i]= float(input(f"entrar com o valor da nota{i+1}:\t"))
    i+=1
nota_escolhida = int(input("Qual a nota que deseja ver? = "))
print(f"nota escolhida foi a:{nota_escolhida:}ª") 
print("nota =" , notas[nota_escolhida - 1 ])
                        


lista_0 = [1,2,3]
lista_1 = lista_0
print("lista_0 = ",lista_0)
print("lista_1 = ", lista_1)
lista_1 [0] = 4
lista_1 [1] = 5
lista_1 [2] = 6
#a atualização de valores tem de ser feita para cada elemento individualmente
print("novos valores de lista_1 =", lista_1)
print("lista[0] tem a mesma referência de lista [1]: lista_0 =", lista_0)



lista_0 = [1,2,3]
lista_1 = lista_0 [:]
print("lista_0 = ",lista_0)
print("lista_1 = ", lista_1)
lista_1 [0] = 4
lista_1 [1] = 5
lista_1 [2] = 6
#a atualização de valores tem de ser feita para cada elemento individualmente
print("novos valores de lista_1 =", lista_1)
print("lista[0] tem a mesma referência de lista [1]: lista_0 =", lista_0)

"""

#segmentação(fatiamento) de listas
lista_2  = [1,2,3,4,5,6]
#[a:b] à esquerda dois pontos: posição do início do segmento; à direita dos pontos = posição final (não incluído)
print("\n\nlista_2[0:6] = lista completa", lista_2[0:6])
print("lista_2[:6] = lista completa", lista_2[:6] )
print("lista_2[:-1] = menos um elemento a partir do fim da lista", lista_2[:-1])
print("lista_2[:2] = menos dois elementos a partir do fim da lista", lista_2 [:-2])
print("lista_2[-3] = menos um elemento a partir do fim da lista", lista_2[:-3])
print("lista_2[:-5] = menos cinco elementos a partir do fim da lista",lista_2[:-5])
print("lista_2[0:3] = trÊs elementos a partir da primeira lista", lista_2[0:1])
print("lista_2[0:5] = cinco primeiros elementos da lista", lista_2 = [1, 2, 3, 4, 5])
print("lista_2[0:6]")
































