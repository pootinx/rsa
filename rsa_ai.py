
e = 3194431902064013299
n = 4959857312573239457
d = 1838763639251553019

B1 = 4249869471061488508
B2 = 1001776371879623227
B3 = 2516869311349389770
B4 = 309660329914070426
B5 = 1847727059104339995

list_block = [B1, B2, B3, B4, B5]


for x in list_block :
    decrypted_message = pow(x, d, n)
    print(decrypted_message)