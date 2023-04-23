my_dict = dict(zip(' ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(10,37)))
n=85
e=5
d=13
def mots(key):
    m=0
    for clé,valeur in my_dict.items():
        if clé==key:
            m+=valeur
            return int(m)
def inverse_mots(val):
    s=''
    f=val
    for clé,valeur in my_dict.items():
        if valeur==f:
            s+=clé
            return s
# def mots(mot):
#     m = ''
#     for lettre in mot:
#         m += str (my_dict[lettre])
#     return int(m)
def chiffrement(x):
    n=85
    e=5
    r=0
    for lettre in x :
        f=mots(lettre)
        r=(f**e)%n 

    print("Alors le message dechifré en valeur est est : ",r)
    return r
    # inv=inverse_mots(r)
    
    
def dechiffrement(y):
    n=85
    d=13
    w= (y**d)%n
    inv=inverse_mots(w)
    print("Alors le message dechifré en valeur est : ",inv)
v = (input("Donner le message : "))

# print(,mots(v))
print("La valeur dde message apré le tablau est :",mots(v))
chiffrement(v)
# dechiffrement(r)
# print(my_dict.items())
