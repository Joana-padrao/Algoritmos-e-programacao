#!/usr/bin/env python
# coding: utf-8

# In[2]:


def criarTermo(coef, exp):
    return(coef, exp)

def criarPolinomio():
    return[]

def inserirTermo(p, t):
    return p.append(t)

def verTermo(t):
    c,e =t
    if e==0:
        return str(c)
    else:
        return (str(c)+ "x^"+str(e))


def verPolinomio(p):
    res=""
    for t in p:
        if res=="":
            res=verTermo(t)
        else:
            res=res + " + " + verTermo(t)
    return res

def calcPol(p, x):
    res=0
    for(c,e) in p:
        res = res + (c*(x**e))
    return res

def tabela (p, nlinhas):
    for i in range (nlinhas +1):
        print(str(i)+" : : " + str(calcPol(p,i)))
        
def chaveOrd(t):
    c,e = t
    return e

def ordenarPol(p):
    p.sort(reverse=True,key=chaveOrd)
    return p

p1=[(2,2), (5,1)]
def derivarPol(p):
    res=[]
    for (c,e) in p:
        if e>0:
            res.append((c*e, e-1))
    return res
verPolinomio(derivarPol(p1))
    
def simplificarPol(p):
    res =[]
    n=""
    coef=0
    pol=0
    ordenarPol(p)
    for t in p:
        c,e =t
        if n=="":
            n=t
            pol=e
            coef=c
            res.append((c,e))
        else:
            if pol==e:
                coef=coef+c
                del res[-1]
                res.append((coef,e))
                pol=e
            else:
                res.append((c,e))
                coef=c
                pol=e         
    return res
    
def sair():
    print("Até à próxima")
    
def invalida():
    print("Opção inválida")

def menu():
    op="1"
    while op!="0":
        op=input('''
           polinómios
          (1) criar um polinómio
          (2) calcular um polinómio
          (3) calcular tabela
          (4) simplificar um polinómio
          (5) cacular a derivada de um polinómio
          (0) Sair
          
          Qual a sua opção? ''')

        if (op=="1"):
            p=[]
            p=criarPolinomio()
            n=int(input("Quantos termos terá o polinómio? "))
            for i in range (n):
                coef=int(input("Qual o valor do coeficiente? "))
                exp=int(input("Qual o valor do expoente? "))
                c=criarTermo(coef, exp)
                inserirTermo(p, c)
            print(verPolinomio(p))
            
        elif (op=="2"):
            x=int(input("Qual é o valor da variável? "))
            print(calcPol(p, x))
            
        elif (op=="3"):
            n=int(input("Quer calcular o valor do polinómio até que número da variável? "))
            print(tabela(p, n))
        
        elif (op=="4"):
            print(verPolinomio(simplificarPol(p)))
            
        elif (op=="5"):
            print(verPolinomio(simplificarPol(derivarPol(p))))
                
        elif (op=="0"):
            sair()
        else:
            invalida()
                
menu()
             


# In[ ]:




