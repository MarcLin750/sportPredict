from function import *

# récupère le token et user_id dans le fichier json
try:
    try:
        with open("../userInfo.json") as f:
            data = json.load(f)
    except:
        with open("../../userInfo.json") as f:
            data = json.load(f)

    access_token = data[0]["access_token"]
    user_id = str(data[0]["x_user_id"])
    
    headers = {
      'Accept': 'application/json',  'Authorization': f'Bearer {access_token}'
    }

    print("\n\nLe token et l'id ont été récupérés avec succès.")

except Exception as e:
    print("\n\nUne erreur s'est produite.")


exercise_id = exercisesList(headers)

getExercise(headers, exercise_id)