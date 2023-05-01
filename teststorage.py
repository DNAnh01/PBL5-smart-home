from database.connection import bucket

import threading
import os
import time

files_to_upload = [
    'E:/BKDN/ky6/PBL5/src/z_face_recognition/dataset/NgocAnh/2bdae2ac2478f926a06918.jpg',
    'E:/BKDN/ky6/PBL5/src/z_face_recognition/dataset/HongVan/IMG_20230302_102155.jpg',
    'E:/BKDN/ky6/PBL5/src/z_face_recognition/dataset/NguyenAnh/z4303245781578_b6388271c62153b7f0e99f981de8a066.jpg',
    'E:/BKDN/ky6/PBL5/src/z_face_recognition/dataset/NhuQuynh/IMG_02.jpg'
]

def upload_file(file_path):
    file_name = os.path.basename(file_path)
    blob = bucket.blob(file_name) 
    start_time = time.time()
    blob.upload_from_filename(file_path)
    blob.make_public() # đặt quyền truy cập public-read cho tệp tin
    end_time = time.time()
    print("Public URL of {}: {}".format(file_name, blob.public_url))
    print("Running time of {}: {} s".format(file_name, end_time - start_time))


threads = []

for file_path in files_to_upload:
    thread = threading.Thread(target=upload_file, args=(file_path,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Done.")
