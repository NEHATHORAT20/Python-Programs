import os
import shutil
import hashlib
import zipfile
import time
import logging

def calculate_hash(path):
    hobj = hashlib.md5()

    with open(path, "rb") as fobj:
        while True:
            data = fobj.read(1024)
            if not data:
                break
            hobj.update(data)

    return hobj.hexdigest()


def BackupFiles(Source, Destination):

    CopiedFiles = []

    os.makedirs(Destination, exist_ok = True)

    for root, dirs, files in os.walk(Source):
        ignore = [".tmp", ".log", ".exe"]

        for file in files:

            if any(file.endswith(ext) for ext in ignore):
                continue

            src_path = os.path.join(root, file)
            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok = True)

            if (not os.path.exists(dest_path) or calculate_hash(src_path) != calculate_hash(dest_path)):
                shutil.copy2(src_path, dest_path)
                CopiedFiles.append(relative)

    return CopiedFiles

def make_zip(folder):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zobj:
    
        for root, dirs, files in os.walk(folder):
            for file in files:
                full = os.path.join(root, file)
                rel = os.path.relpath(full, folder)
                zobj.write(full, rel)

    return zip_name