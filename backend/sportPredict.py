import os,json
from flask import Flask, request, jsonify
from src.db.hanaDB import Hdb
from hdbcli import dbapi
# from flask_cors import cross_origin    

import requests
# TODO : use prod api
import hackathon_api_fake as api


connection_info = {
    'address'   : 'hackathon-sport-predict',
    'port'      : '30015',
    'user'      : 'RENAUD',
    'password'  : 'Renaud01',

}

app  = Flask(__name__)
port = int(os.environ.get('PORT', 3000))

@app.route('/DB')
def check_hana():
    #  connection = dbapi.connect (
    #     address=connection_info['address'],
    #     port=connection_info['port'],
    #     user=connection_info['user'],
    #     password=connection_info['password'],
    # )
    # cursor = connection.cursor()
    # cursor.execute('select count(*) from "RENAUD"."TRAINING_SESSIONS_MAIN_RENAUD"')
    response = jsonify(message="Dummy message from Tom")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response 





@app.route('/dummy', methods=['GET'])
def get_dummy():
    response = jsonify(message="Dummy message from Tom")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response 
# jsonify({'data': 'dummy'}), 200

@app.route('/lastsession')
def get_lastsession():
    response = jsonify(api.get_lastsession())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response 

# example url/listofsessions?fromSession=DATE_FROM&toSession=DATE_TO
@app.route('/listofsessions')
def get_list_of_sessions():
    fromSession  = request.args.get('fromSession', default = None, type = str)
    toSession    = request.args.get('toSession',  default = None, type = str)
    response     = jsonify(api.get_listofsessions(fromSession, toSession))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response 

# example url/getsession?id=1234
@app.route('/getsession/')
def get_session():
    sessionid = request.args.get('id', default = '', type = str)
    response  = jsonify(api.get_session(sessionid))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# example url/exerciseofsession?id=1234
@app.route('/exerciseofsession/')
def get_exerice_of_session():
    sessionid = request.args.get('id', default = '', type = str)
    response  = jsonify(api.get_exerciceofsession(sessionid))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/delallsequences/')
def delete_allsequences():
    response = jsonify(api.delete_allsequences())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/delsequencetype/')
def delete_sequence_type():
    minduration = request.args.get('minduration', default = '', type = str)
    minspeed    = request.args.get('minspeed', default = '', type = str)
    response    = jsonify(api.delete_1sequencetype(minduration, minspeed))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/delsequence/')
def delete_single_sequence():
    seqid       = request.args.get('id', default = '', type = str)
    minduration = request.args.get('minduration', default = '', type = str)
    minspeed    = request.args.get('minspeed', default = '', type = str)
    response    = jsonify(api.delete_1sequence(seqid, minduration, minspeed))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/getLastPolar')
def persist():
    return """
    1. recup des dernieres sessions avec Polar (cf Marc code)
    => genere des json
    """
    
    # 2. Here we call Nico scripts with json (scripts a modifier)
    # """


@app.route('/')
def hello():
    hackathonTitle = 'Sport Predict Hackathon Paris 2024'
    apiurl = 'https://sport-predict-insightful-lizard-pk.cfapps.eu12.hana.ondemand.com'
    return f"""

    <html>
        <header>
        <title>{hackathonTitle}</title>
    </header>
    <body>
        <h1>{hackathonTitle}</h1>
        <p>Endpoints API : {apiurl} 
            <ul>
                <li>Dummy api test              : <a href='{apiurl}/dummy'>Dummy</a></li>
                <li>list all sessions           : <a href='{apiurl}/listofsessions'>listofsessions</a></li>
                <li>get last session            : <a href='{apiurl}/lastsession'>lastsession</a></li>
                <li>get unique session          : <a href='{apiurl}/getsession/?id=2019-12-24T12:02:06.605'>getsession</a></li>
                <li>get exercises of session    : <a href='{apiurl}/exerciseofsession/?id=2019-12-24T12:02:06.605'>exerciseofsession</a></li>
                <li>delete all sequences        : <a href='{apiurl}/delallsequences'>delallsequences</a></li>
                <li>delete sequence type        : <a href='{apiurl}/delsequencetype/?minduration=240&minspeed=17'>delsequencetype</a></li>
                <li>delete single sequence      : <a href='{apiurl}/delsequence/?id=1234&minduration=240&minspeed=17'>delsequence</a></li>
            </ul>
        </p>
    </body>
</html>
    """
if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=port)