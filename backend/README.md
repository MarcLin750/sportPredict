# External API : To be used from UI 

- (not ready) *polarload()*:
	1) *polarloading()* +
	2) *get_sessions(>get_lastsessions())*
	3) *insert_sessions()*
	4) *populate_enrichment(>get_lastsessions())*
	5) *get_sequenceminvalues(>get_lastsessions())* => loop to perform extractrealsequences()
- *get_lastsessions()*
- *get_listofsessions(optional fromSession, optional toSession)*
- *get_session(sessionID) + get_exerciceofsession(sessionID)*
- (on going) *populate_sequences(fromSession, minduration, minspeed)*
- (not ready) *get_listsequenceminvalues()*
- (not ready) *get_listsequences(minduration, minspeed)*
- (not ready) *get_sequence(sequenceID, minduration, minspeed) + get_detailofsequence(sequenceID, minduration, minspeed)*
- (not ready) *delete_allsequences()* :
	1) *deleteinternal_sequence(none, none, none)*
- (not ready) *delete_1sequencetype(minduration, minspeed)*
	1) *deleteinternal_sequence(none, minduration, minspeed)*
- (not ready) *delete_1sequence(sequenceID, minduration, minspeed)*
	1) *deleteinternal_sequence(sequenceID, minduration, minspeed)*
- *cleanup_reset_runningverified()*
	1) Null if not Running session, else True
	2) False if MAXSPEED < 5 or > 45
	3) False if AVGSPEED < 2 or > 30
	4) False if DISTANCE < 15 or > 50000
	5) False if AVGSPEED > 20 and DISTANCE > 10000



# Test app 

## local checks

Run local app using flask
It will generate a local url 
    flask --app sportPredict run  --host=0.0.0.0

## test backend

Run tests locally
*prerequisite : * run a local flask app 
    cd backend
    flask --app sportPredict run  --host=0.0.0.0

    pip install pytest
    cd .\backend\tests
    python -m pytest -s --api_url <YOUR_LOCAL_FLASK_URL>
    # Or run test on deployed app
	python -m pytest -s --api_url https://sport-predict-insightful-lizard-pk.cfapps.eu12.hana.ondemand.com/

# Deploy app

## Configuration
### update python requirements

    pip freeze > requirements.txt
    
 ### update manifest.yml

Entrypoint of the app should be *sportPredict.py* 

## Cloud deployment

### Cloud informations

- Global account : *Advanced Analytics group (BITBIAA)* / 986d6699-c598-4497-966b-7718631f3aa5
- Subaccount : *hackathon_sport-predict* / 54a36cb9-7573-45e8-a569-cbae86ef0d41
- Space : *prod*
- App name : *sport-predict*
- BTP link : [Direct link on subaccount](https://canary.cockpit.btp.int.sap/cockpit#/globalaccount/986d6699-c598-4497-966b-7718631f3aa5/subaccount/54a36cb9-7573-45e8-a569-cbae86ef0d41/subaccountoverview)


*prerequisite :* have *Space Developer* role in subaccount

Deploy app : 

    cf login --sso          # if asked, open given url to retrieve token and copy paste the new token in console
    cf push


# Internal API 

Used locally in dev mode to do some checks, DB admin tasks etc ...

- *localfileloading()*     : load in memory every sessions from local files (from data/Renaud/training-session*)
- *polarloading()*         : load in memory recent sessions (last 30 days sessions) from the Polar website
    => both must have the same output....

- *dropcreate_basic()*      : drop + create tables: MAIN, AUTOLAPS, LAPS + EXOSAMPLE
- *dropcreate_enriched()*   : drop + create tables: MAIN_ENRICHED
- *dropcreate_sequences()*  : drop + create tables: SEQUENCE_MAIN, SEQUENCE_DETAILS
- *get_lastsessionfromdb()* : get the latest session inserted in the database
- *insert_sessions()*       : insert into the DB every sessions more recent than the get_lastsessionfromdb()
- *generate_enrichment()*   : insert/generate into the Enrichment DB table, all new records that are more recent than the get_lastsessionfromdb()
- *get_sequenceminvalues()* : returns every distinct values of tuple 'Min Duration Session' / 'Min Speed Session'
- *delete_sequences()*      : removes every items from the 2 Sequences tables (main + details) that correspond to a tuple 'Min Duration Session' / 'Min Speed Session'. If none => delete all
- *extractrealsequences()*  : insert/generate into the 2 Sequences DB table, all new records that are more recent than the get_lastsessionfromdb() for the PARAM: MinDurationSession + MinSpeedSession
- *get_listofsessions()*    : get the list of sessionsID (startime) according to the parameters (optional: begin date + end date, default: all)


NB: To be run locally (python scripts) :

- all dropcreate_tables() + 
- localfileloading() initial +
- insert_sessions() initial + delta
- general_enrichement() initial +
- extractrealsequences(4min, 16km/h)