my_dict = dict(zip(' ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(10,37)))
n=85
e=5
d=13
def mots(mot):
    m = ''
    for lettre in mot:
        m += str (my_dict[lettre])
    return int(m)
def chiffrement(x):
    n=85
    e=5
    q=mots(x)
    r=(q**e)%n 
    return r
def dechiffrement(y):
    n=85
    d=13
    t=chiffrement(y)
    w= (t**d)%n
    return w
def inverse_mots(val):
    s=''
    f=dechiffrement(val)
    for clé,valeur in my_dict.items():
        if valeur==f:
            s+=clé
            return s
v = (input("Donner le message : "))
print("Donc la valeur de ce message dans le tablaue est : ",mots(v))
print ( "Le message chifré en valeur est donc : ",chiffrement(v))
print ( "Alors le message dechifré en valeur est : ",dechiffrement(v))
print ( "Le message en lettre est : ",inverse_mots(v))
