from firebase import Firebase

config = {
  "apiKey": "AIzaSyB9RkZFAwtJfZUXYvXZBb2S4GYVSzOkpjEv",
  "authDomain": "location-a26be.firebaseapp.com",
  "databaseURL": "https://location-a26be-default-rtdb.asia-southeast1.firebasedatabase.app",
  "storageBucket": "location-a26be.appspot.com"
}

firebase = Firebase(config)

db = firebase.database()

users = db.child("location").get()
data = users.val()
print(data.items())
for key, value in data.items():
    # print(key, value)
    if key == "latitude":
      print(value)
    if key == "longitude":
      print(value)
