from firebase import Firebase

config = {
  "apiKey": "AIzaSyB9RkZFAwtJfZUXYvXZBb2S4GYVSzOkpjEv",
  "authDomain": "location-a26be.firebaseapp.com",
  "databaseURL": "https://location-a26be-default-rtdb.asia-southeast1.firebasedatabase.app",
  "storageBucket": "location-a26be.appspot.com"
}

firebase = Firebase(config)
db = firebase.database()


try:
    db.child("locationCar").update({"longitude": 11.287,"latitude": 178.1})
except:
    print("internet connection Error!!")