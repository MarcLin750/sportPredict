import base64
import requests
import json

# fonction qui convertit l'Id et le secret en base64
def authorization_code(client_id, client_secret):
    message = client_id + ':' + client_secret
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    authorization_code = base64_bytes.decode('ascii')

    return authorization_code

# fonction qui télécharge le token
def create_token(authorization, code):
    
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': 'Basic ' + authorization,
      'Accept': 'application/json'
    }
    body = {
      'grant_type': 'authorization_code',
      'code': code
    }

    r = requests.post('https://polarremote.com/v2/oauth2/token', data=body, headers=headers)

    if r.status_code == 200: # vérifie que la reqête est valide 
        response_json = r.json()
        with open("token.json", 'w') as op: # le w signifie write pour écrire
            json.dump(response_json, op, indent=4) # indent 4 fait qu'il y aura à chaque fois une indentation de 4 
        print("\nLe token à bien été téléchargé avec succès.\n")
    else:
        print("Echec de la requête: ", r.status_code)

