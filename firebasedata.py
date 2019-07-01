import pyrebase
from ketquasoxo import ketquasoxo
import json

Config = {
  "apiKey": "AIzaSyCx_Sfzsvvd9jwB-aGlZVesMjmxOYc_O9E",
  "authDomain": "crud-phuc.firebaseapp.com",
  "databaseURL": "https://crud-phuc.firebaseio.com",
  "projectId": "crud-phuc",
  "storageBucket": "crud-phuc.appspot.com",
  "messagingSenderId": "513971924312",
  "appId": "1:513971924312:web:eb0a195b0b0f4e6b"
# cap nhat or them moi
}
firebase = pyrebase.initialize_app(Config)
db = firebase.database()
# # day len db
# # db.child('name').push({"name":"LePhuc"})
# # db.child('soxovungtau').update({"ngay":"12345"})
# # db.child('soxovungtau').update({"ngay1":"3423432"})
# db.child('soxovungtau').update(ketquasoxo())
# db.child('soxovungtau').remove()
dataketqua = json.dumps(ketquasoxo(),indent=4)
print(dataketqua)


