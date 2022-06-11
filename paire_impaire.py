t1=int(input('la taille'))
t2=int(input('la taille'))
l1=[]
l2=[]
l3=[]
for i in range (0,t1):
        x=int(input())
        l1.append(x)
for i in range (0,t2):
    n=int(input())
    l2.append(n)
    
#def odd_ev(L1,L2):
def fct(l1,l2):
    for x in l1:
            if(x%2 ==0):
                l3.append(x)

    for n in l2:
            if(n%2!=0):
                l3.append(n)
    return l3

print(fct(l1,l2))