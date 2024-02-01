import requests
import base64
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

    rToken = requests.post('https://polarremote.com/v2/oauth2/token', data=body, headers=headers)

    if rToken.status_code == 200: # vérifie que la reqête est valide 
        tokenInfo = rToken.json()
        access_token = tokenInfo['access_token']
        User_id = str(tokenInfo['x_user_id'])

        # enregistrement automatique de l'utilisateur
        input_body1 = {
          "member-id": "User_id_" + User_id
        }
        headers1 = {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'Authorization': 'Bearer ' + access_token
        }

        rUser = requests.post('https://www.polaraccesslink.com/v3/users', headers = headers1, json=input_body1)

        if rUser.status_code >= 200 and rUser.status_code < 400:
            userInfo = rUser.json()
            
            info = [] # list des éléments tokenInfo et UserInfo
            info.append(tokenInfo)
            info.append(userInfo)
    
            with open("userInfo.json", 'w') as op: # userInfo.json correspond au nom du fichier créer et le w signifie write pour écrire
                json.dump(info, op, indent=4) # indent 4 fait qu'il y aura à chaque fois une indentation de 4 
            print("Voici votre token: ", access_token)
            print("\nLe fichier d'info à été téléchargé avec succès.\n")

        else:
            print(rUser.status_code)
    else:
        print("Echec de la requête: ", rToken.status_code)

# récupère le token et user_id dans le fichier json
def getInfo():
    try:
        with open("userInfo.json") as f:
            data = json.load(f)
    except:
        with open("../userInfo.json") as f:
            data = json.load(f)

    token = data[0]["access_token"]
    user_id = str(data[0]["x_user_id"])
    return token, user_id

def createTransactionTrainingData(token, user_id):
    headers = {
      'Accept': 'application/json',
      'Authorization': 'Bearer ' + token
    }

    r = requests.post('https://www.polaraccesslink.com/v3/users/'+user_id+'/exercise-transactions', headers = headers)

    if r.status_code >= 200 and r.status_code < 400:
        print(r.json())
    else:
        print(r)

# renvoie la liste des exercices
def getExercisesList(token):

  headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + token
  }

  r = requests.get('https://www.polaraccesslink.com/v3/exercises', headers = headers)

  if r.status_code >= 200 and r.status_code < 400:
      print(r.json())
  else:
      print(r)

def exercisesList(token):
    headers = {
      'Accept': 'application/json',  'Authorization': 'Bearer ' + token
    }

    r = requests.get('https://www.polaraccesslink.com/v3/users/38196969/exercise-transactions/286142734', headers = headers
        )

    if r.status_code >= 200 and r.status_code < 400:
        print(r.json())
    else:
        print(r)

def getExerciseSummary(token):
    headers = {
      'Accept': 'application/json',  'Authorization': 'Bearer ' + token
    }

    r = requests.get('https://www.polaraccesslink.com/v3/users/38196969/exercise-transactions/286142734/exercises/338806535', headers = headers
        )

    if r.status_code >= 200 and r.status_code < 400:
        print(r.json())
    else:
        print(r)