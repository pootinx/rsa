def encrypt_RSA(message, e, n):
    """
    Chiffre un message en utilisant RSA
    """
    message = message.upper()
    # Convertir le message en nombres en utilisant le codage donné
    message_numbers = [{' ': 10, 'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20, 'K': 21, 'L': 22, 'M': 23, 'N': 24, 'O': 25, 'P': 26,
                      'Q': 27, 'R': 28, 'S': 29, 'T': 30, 'U': 31, 'V': 32, 'W': 33, 'X': 34, 'Y': 35, 'Z': 36}[c] for c in message]
    # Chiffrer chaque nombre en utilisant la clé publique et l'exposant modulaire
    
    encrypted_numbers = [pow(num, e, n) for num in message_numbers]
    
    return encrypted_numbers
#_____________________________ pow(num, e, n) function calculates num^e % n______________________________
 
def decrypt_RSA(encrypted_numbers, d, n):
    """
    Déchiffre un message chiffré en utilisant RSA
    """
    # Déchiffrer chaque nombre en utilisant la clé privée et l'exposant modulaire
    decrypted_numbers = [pow(num, d, n) for num in encrypted_numbers]
    print("Block dechifre : ",decrypted_numbers)
    # Convertir les nombres déchiffrés en caractères en utilisant le codage donné
    decoded_message = ''.join([{10: ' ', 11: 'A', 12: 'B', 13: 'C', 14: 'D', 15: 'E', 16: 'F', 17: 'G', 18: 'H', 19: 'I', 20: 'J', 21: 'K', 22: 'L', 23: 'M', 24: 'N', 25: 'O', 26: 'P',
                         27: 'Q', 28: 'R', 29: 'S', 30: 'T', 31: 'U', 32: 'V', 33: 'W', 34: 'X', 35: 'Y', 36: 'Z'}[num] for num in decrypted_numbers])
    return decoded_message
# def display_menu():
#     print("-------------Chiffrement RSA------------")
#     print("1. Chiffrés un message")
#     print("2. déchiffrés un message")
#     print("3. Quit")
#     choice = input("Entrer un choix (1-3): \n")
#     return choice

# def main():
#     while True:
#         choice = display_menu()
#         if choice == '1':
#             message =input("Entrer le message a Chiffrés : ")
#             e = 3194431902064013299
#             n = 4959857312573239457
#             encrypted_message = encrypt_RSA(message, e, n)
#             print("Le message Chiffrés : ", encrypted_message)
#         elif choice == '2':
#             t = input("Entrer le message a déchiffrés: ")
#             encrypted_numbers = t.split(", ")
#             d = 1838763639251553019
#             n = 4959857312573239457
#         elif choice == '3':
#             break
#         else:
#             print("Choix invalide. Essayer à nouveau.")

# if __name__ == "__main__":
#     main()


e = 3194431902064013299
n = 4959857312573239457
d = 1838763639251553019

message = input("Entré un message : ")
# Chiffrement du message
encrypted_message = encrypt_RSA(message, e, n)
print("Les blocks chifré : ",encrypted_message)

# Déchiffrement du message chiffré
decrypted_message = decrypt_RSA(encrypted_message, d, n)
print("le message déchifré est : ",decrypted_message)
