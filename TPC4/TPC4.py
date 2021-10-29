#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def criarFracao(num, den):
    return (num, den)

def verFracao(f):
    print(str(f[0]) + "/" + str(f[1]))
    
def mdc(a,b):
    if a<b:
        return mdc(b,a)
    elif (a % b==0):
        return b
    else:
        return mdc(a, a%b)
    
def simplificarFracao(f):
    num, den=f
    a=mdc(num, den)
    return (num/a, den/a)

def somaFracao(f1, f2):
    n1, d1=f1
    n2, d2=f2
    frac=criarFracao(((n1*d2)+(n2*d1)), (d1*d2))
    return frac

def subtrairFracao(f1, f2):
    n1, d1=f1
    n2, d2=f2
    frac=criarFracao(((n1*d2)-(n2*d1)), (d1*d2))
    return frac

def multiplicarFracao(f1, f2):
    n1, d1=f1
    n2, d2=f2
    frac=criarFracao((n1*n2), (d1*d2))
    return frac

def dividirFracao(f1, f2):
    n1, d1=f1
    n2, d2=f2
    frac=criarFracao((n1*d2), (n2*d1))
    return frac

from random import randint
def listaFracao():
    n=int(input("Quantos elementos tem a lista? "))
    lnum=[]
    lden=[]
    l=[]
    for i in range (n):
        el=randint(0,100)
        lnum.append(el)
    for j in range (n):
        el=randint(0,100)
        lden.append(el)
    for k in range (n):
        f=simplificarFracao(criarFracao(lnum[k], lden[k]))
        l.append(f)
    return l
 
def somarLista(lis):
    res=(0,1)
    for elem in lis:
        res=somaFracao(res, elem)
    return res

def maiorFracao(lis):
    li=[]
    grande=0
    for j in range (len(lis)):
        num, den= lis[j]
        f=num/den
        li.append(f)
    i=0
    maior=li[i]
    for i in range (len(li)-1):
        if maior<li[i+1]:
            maior=li[i+1]
            grande=lis[i+1]
    return grande

def sair():
    print("Até à próxima")
    
def invalida():
    print("Opção inválida")
    
def menu():
    op="1"
    while op!="0":
        op=input('''
           Frações
          (1) Criar uma fração
          (2) Simplificar uma fração
          (3) Somar duas frações
          (4) Subtrair duas frações
          (5) Multiplicar duas frações
          (6) Dividir duas frações
          (7) Criar uma lista de n frações
          (8) Somar uma lista de frações
          (9) Ver qual a maior fração de uma lista
          (0) Sair
          
          Qual a sua opção? ''')

        if (op=="1"):
            num=int(input("Qual é o numerador? "))
            den=int(input("Qual é o denominador? "))
            verFracao(criarFracao(num, den))
        
        elif (op=="2"):
            num=int(input("Qual é o numerador? "))
            den=int(input("Qual é o denominador? "))
            verFracao(simplificarFracao(criarFracao(num, den)))
            
        elif (op=="3"):
            n1=int(input("Qual o numerador da primeira fração? "))
            d1=int(input("Qual o denominador da primeira fração? "))
            n2=int(input("Qual o numerador da segunda fração? "))
            d2=int(input("Qual o denominador da segunda fração? "))
            f1=criarFracao(n1, d1)
            f2=criarFracao(n2, d2)
            verFracao(simplificarFracao(somaFracao(f1, f2)))
            
        elif (op=="4"):
            n1=int(input("Qual o numerador da primeira fração? "))
            d1=int(input("Qual o denominador da primeira fração? "))
            n2=int(input("Qual o numerador da segunda fração? "))
            d2=int(input("Qual o denominador da segunda fração? "))
            f1=criarFracao(n1, d1)
            f2=criarFracao(n2, d2)
            verFracao(simplificarFracao(subtrairFracao(f1, f2)))
            
        elif (op=="5"):
            n1=int(input("Qual o numerador da primeira fração? "))
            d1=int(input("Qual o denominador da primeira fração? "))
            n2=int(input("Qual o numerador da segunda fração? "))
            d2=int(input("Qual o denominador da segunda fração? "))
            f1=criarFracao(n1, d1)
            f2=criarFracao(n2, d2)
            verFracao(simplificarFracao(multiplicarFracao(f1, f2)))
        
        elif (op=="6"):
            n1=int(input("Qual o numerador da primeira fração? "))
            d1=int(input("Qual o denominador da primeira fração? "))
            n2=int(input("Qual o numerador da segunda fração? "))
            d2=int(input("Qual o denominador da segunda fração? "))
            f1=criarFracao(n1, d1)
            f2=criarFracao(n2, d2)
            verFracao(simplificarFracao(dividirFracao(f1, f2)))
            
        elif (op=="7"):
            lis=listaFracao()
            print(lis)
        
        elif (op=="8"):
            verFracao(simplificarFracao(somarLista(lis)))
            
        elif (op=="9"):
            verFracao(maiorFracao(lis))
            
        elif (op=="0"):
            sair()
        else:
            invalida()
menu()

