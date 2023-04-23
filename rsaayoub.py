d = dict(zip(' ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(10, 37)))

def dechifrement(mots):
    e = 5
    dd = 13
    n = 85
    dec = []
    for lettre in mots:
        r = (d[lettre] ** e) % n
        dec.append(str(r))
    return dec

# Get input from the user
o = input("Enter a string to decode: ")
lesvals = dechifrement(o)
print(lesvals)

def dech(lesvals):
    e = 5
    dd = 13
    n = 85
    ch = {}
    for j in lesvals:
        j = int(j)
        x = (j ** dd) % n
        ch[j] = x
    return ch

ch = dech(lesvals)
print(ch)

def inverse_mots():
    s=''
    liste=[]
    for i in range(len(ch)+1):
        for clé,val in ch.items():
            if val == i:
                s = clé
        liste.append(s)
    return liste

print(inverse_mots())