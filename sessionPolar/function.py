import requests
import json

# Créer une transaction
def createTransactionTrainingData(headers, user_id):
    r = requests.post(f'https://www.polaraccesslink.com/v3/users/{user_id}/exercise-transactions', headers = headers)

    if r.status_code >= 200 and r.status_code < 400:
        print(r.json())
    else:
        print(r)

def getExercisesList(headers, user_id):

    r = requests.get(f'https://www.polaraccesslink.com/v3/users/{user_id}/exercise-transactions/286611864', headers = headers
        )   

    if r.status_code >= 200 and r.status_code < 400:
        print(r.json())
    else:
        print(r)

def getExerciseSummary(headers, user_id):
    
    r = requests.get(f'https://www.polaraccesslink.com/v3/users/{user_id}/exercise-transactions/286609387/exercises/340164351', headers = headers
        )

    if r.status_code >= 200 and r.status_code < 400:
        print(r.json())
    else:
        print(r)
        
###############################################################################################################################

def exercisesList(headers):

    r = requests.get('https://www.polaraccesslink.com/v3/exercises', headers = headers)

    if r.status_code >= 200 and r.status_code < 400:
        info=r.json()
        nbr_max_exercise = len(info)
        numero_exercices = 0
        exercise_id = []
        while nbr_max_exercise > numero_exercices:
            exercise_id.append(info[numero_exercices]["id"])
            numero_exercices += 1
    else:
        print(r)

    return exercise_id

def getExercise(headers, exercise_id):
    params = {
        'samples': True,
        'zones': True
    }

    nbr_max_exercise = len(exercise_id)
    numero_exercices = 0

    while nbr_max_exercise > numero_exercices:
        r = requests.get(f'https://www.polaraccesslink.com/v3/exercises/{exercise_id[numero_exercices]}', headers = headers, params = params)
        
        if r.status_code >= 200 and r.status_code < 400:
            info = r.json()
            start_time = info['start_time']
            elements = start_time.split('T')
            date = elements[0]
            heure = elements[1]
            heures, minutes, secondes = map(int, heure.split(':'))
            total_secondes = heures * 3600 + minutes * 60 + secondes

            with open(f"training-session-{date}-{total_secondes}.json", 'w') as op:
                json.dump(info, op, indent=4)
        else:
            print(r)
        numero_exercices += 1
