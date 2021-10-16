#!/usr/bin/env python
# coding: utf-8

# # Manisfesto:

# * __identificador__: TPC2
# * __título__: Adivinha o número
# * __data de inicio__: 2021-10-13
# * __data de fim__: 2021-10-16
# * __supervisor__: José Carlos Ramalho, url: https://www.di.uminho.pt/~jcr/thesup-v2.php
# * __autor__: Joana Padrao, nº a96101
# * __resumo__: Ao jogar a pessoa pensa num número. O programa vai perguntando sucessivamente se o número que ele propõe é maior, menor ou igual ao número pensado (variável p). Por sua vez, o programa propõe o número fazendo a divisão inteira por 2 da diferença do limite superior e do limite inferior e de seguida soma esse valor ao limite inferior, sendo esse o número que o programa propõe (variável n). O limite inferior começa em 0 e o limite superior começa em 100 e à medida que se faz as divisões, se o número proposto for inferior ao pensado pela pessoa o limite inferior passa a ser o valor prosposto mais uma unidade, se por sua vez, o número prosposto for superior o limite superior passa a ser o valor superior subtraindo uma unidade. E este processo é repetido até se encontrar o número, sendo esta condição verificada pela vairável encontrado, quando a pessoa diz que o número pensado é igual ao proposto, o valor da variável encontrado passa a ser verdadeiro então os passos que se realizariam não serão mais realizados, visto que a condição do ciclo while não será mais verdadeira.

# # Programa:

# In[3]:


ninf=0
nsup=100
def adivinha(ninf, nsup):
    encontrado=False
    while not encontrado:
        a=nsup-ninf
        b=a//2
        n=ninf+b
        print(n)
        p=input("É superior 's', inferior 'if' ou igual 'ig' ao seu número?")
        while p!="s" and p!="if" and p!="ig":
            print(n)
            p=input("É superior 's', inferior 'if' ou igual 'ig' ao seu número?")
        if p=="ig":
            print("O número é ",n)
            encontrado=True
        elif p=="if":
            ninf=n+1
        else:
            nsup=n-1

adivinha(ninf, nsup)


# In[ ]:




