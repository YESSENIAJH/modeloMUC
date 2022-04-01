import web
import app
import pyrebase
import firebase.config as token 
import json

urls = (
    '/', 'mvc.controllers.api.sensores'
)
app = web.application(urls, globals())

request.open('GET','/sensores')


class Sensores:
    def GET(self):
        firebase = pyrebase.initializae.app(token.firebase.config)
        db = firebase.database()
        sensores = db.child("sensores").get()
        result = json.sensores
    return sensores.val()