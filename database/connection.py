import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage
import os

service_account_file_path = os.path.join(os.path.abspath("database"), "serviceAccountKey.json").replace("\\", "/")
cred = credentials.Certificate(service_account_file_path)
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://pbl5-smart-home-91965-default-rtdb.firebaseio.com',
    'storageBucket':'pbl5-smart-home-91965.appspot.com'
})

# Truy cập Firestore
db = firestore.client()

# Truy cập Storage
bucket = storage.bucket('pbl5-smart-home-91965.appspot.com')