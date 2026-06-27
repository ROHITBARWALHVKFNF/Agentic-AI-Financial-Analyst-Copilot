import os

UPLOAD_DIR = "data/reports"

os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_uploaded_file(file):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path