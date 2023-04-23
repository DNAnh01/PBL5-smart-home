import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

service_account_file_path = os.path.join(os.path.abspath("database"), "serviceAccountKey.json").replace("\\", "/")
cred = credentials.Certificate(service_account_file_path)
firebase_admin.initialize_app(cred)

db = firestore.client()