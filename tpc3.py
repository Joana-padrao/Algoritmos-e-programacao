#!/usr/bin/env python
# coding: utf-8

# ## Programa

# In[2]:


def criarListaM():
    l=[]
    n=int(input("Número de elementos da lista: "))
    while n>0:
        a=int(input("Escreva o valor "))
        l.append(a)
        n=n-1
    print(l)
    return l

from random import randint   
def criarListaA():
    n=int(input("Número de elementos da lista: "))
    lista2=[]
    for i in range (n):
        el=randint(0,100)
        lista2.append(el)
    print(lista2)
    return lista2

def maiorElemento(lis):
    i=0
    maior=lis[i]
    for i in range (len(lis)-1):
        if maior<lis[i+1]:
            maior=lis[i+1]

    print("O maior elemento é", maior)
    return maior

def bubbleSort(lis):
    i=0
    a=0
    for i in range (len(lis)-1):
        if lis[i]>lis[i+1]:
            m=lis[i]
            lis[i]=lis[i+1]
            lis[i+1]=m
            a=a+1

    while a!=0:
        a=0
        for i in range (len(lis)-1):
            if lis[i]>lis[i+1]:
                m=lis[i]
                lis[i]=lis[i+1]
                lis[i+1]=m
                a=a+1
    print(lis)
    return lis
   
def sair():
    print("Até à próxima")
    
def invalida():
    print("Opção inválida")
    
def menu():
    op="1"
    while op!="0":
        op=input('''
           Gestão de listas de inteiros
          (1) Introduza a lista à mão
          (2) Gerar lista com valores aleatórios
          (3) Maior elemento da lista
          (4) Bubble sort
          (0) Sair
          
          Qual a sua opção? ''')

        if (op=="1"):
            lis=criarListaM()
            #print(lis)
        elif (op=="2"):
            lis=criarListaA()
            #print(lis)
        elif (op=="3"):
            e=maiorElemento(lis)
            #print(e)
        elif (op=="4"):
            lis=bubbleSort(lis)
            #print(lis)
        elif (op=="0"):
            sair()
        else:
            invalida()
menu()


# ## Manifesto

# * __identificador:__ TPC3
# * __título:__ lista de inteiros
# * __data de início:__ 2021-10-18
# * __data de fim:__ 2021-10-24
# * __supervisor:__ José Carlos Ramalho, url: https://www.di.uminho.pt/~jcr/thesup-v2.php
# * __autor:__ Joana Padrao, nº a96101
# * __resumo:__ Na função bubbleSort, o programa começa por correr uma lista dada e se o elemento for maior que o elemento seguinte realiza-se uma troca nas posições desses elementos, senão adiciona-se uma unidade a uma variável (a) que no início começa com o valor zero; dessa forma se o valor dessa variável fôr igual ao valor do tamanho da lista sabemos que não se realizaram trocas na lista, ou seja, a lista já está por ordem. Logo o programa corre sempre a lista pelo menos uma vez e, se a lista já tiver por ordem não se realiza mais nada, se isso não se verificar, o programa vai continuar, devido ao ciclo while, e só acabará quando a variável a fôr zero, ou seja, não se realizaram nenhumas trocas.

# In[ ]:




