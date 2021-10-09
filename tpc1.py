#!/usr/bin/env python
# coding: utf-8

# In[3]:


def jogo():
    p=int(input("Deseja ser o jogador '1' ou o jogador '2'? "))
    while p!=1 and p!=2:
        p=int(input("Deseja ser o jogador '1' ou o jogador '2'? "))
        
    if p==1:    
        def fosforo ():
            total=21
        
            while total>1:
                n=int(input("quer tirar '1', '2', '3' ou '4' fósforos "))
                while n!=1 and n!=2 and n!=3 and n!=4:
                    n=int(input("quer tirar '1', '2', '3' ou '4' fósforos "))
                i=0
                total=total-n
                print ("depois da sua jogada há", total,"fósforos")
                i=5-n
                total=total-i
                print ("o computador já jogou e há", total, "fósforos")
            r=input("deseja jogar novamente? 's' para sim e 'n' para não ")
            while r!="s" and r!="n":
                r=input("deseja jogar novamente? 's' para sim e 'n' para não ")
            if r=="s":
                jogo()
            else:
                return
                
                    
    
        fosforo()
        
    else:
        def again(tot,m):
            t=tot
            print("depois da sua jogada há", t,"fósforos")
            if (21-t)<5:
                c=5-(21-t)
            elif (21-t)>5 and (21-t)<10:
                c=10-(21-t)
            elif (21-t)>10 and (21-t)<15:
                c=15-(21-t)
            else:
                c=20-(21-t)
            t=t-c
            print("o computador já jogou e há", t, "fósforos")
            while t>1: 
                m=int(input("quer tirar '1', '2', '3' ou '4' fósforos "))
                while m!=1 and m!=2 and m!=3 and m!=4:
                    m=int(input("quer tirar '1', '2', '3' ou '4' fósforos "))
                j=0
                t=t-m
                print("depois da sua jogada há", t,"fósforos")
                j=5-m
                t=t-j
                print ("o computador já jogou e há", t, "fósforos")
            r=input("deseja jogar novamente? 's' para sim e 'n' para não ")
            while r!="s" and r!="n":
                r=input("deseja jogar novamente? '1' para sim e '2' para não ")
            if r=="s":
                jogo()
            else:
                return
    
        
        import random 
        def fosf():
            tot=21
            
            while tot>1:
                l=[1,2,3,4]
                a=random.choice(l)
                tot=tot-a
                print("o computador já jogou e há", tot, "fósforos")
            
                m=int(input("quer tirar '1', '2', '3' ou '4' fósforos "))
                while m!=1 and m!=2 and m!=3 and m!=4:
                    m=int(input("quer tirar '1', '2', '3' ou '4' fósforos "))
                if (m+a)==5:
                    tot=tot-m
                    print ("depois da sua jogada há", tot,"fósforos")
                else:
                    tot=tot-m
                    again(tot,m)
                    return
            r=input("deseja jogar novamente? 's' para sim e 'n' para não")
            while r!="s" and r!="n":
                r=input("deseja jogar novamente? 's' para sim e 'n' para não ")
            if r=="s":
                jogo()
            else:
                return
         
        fosf()
jogo()


# In[ ]:





# In[ ]:




