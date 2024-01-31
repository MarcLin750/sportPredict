from functions import *

print("\nPour créer votre token il faudra renseigner votre client_id, client_secret puis votre code.\n(Pour optenir le code suivre étapes 6 et 7 du README.)\n")

#initialisation des variables
print("client_id: ", end="")
client_id = input()
print("client_secret: ", end="")
client_secret = input()
print("code:", end="")
code = input()

# la variable authorization prend l'id et le secret encodée en base64
authorization = authorization_code(client_id, client_secret)

# appel de la fonction qui télécharge le token
create_token(authorization, code)

print("Fin du programme...")