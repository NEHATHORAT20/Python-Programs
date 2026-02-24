import os
import zipfile
import logging

def RestoreBackup(zip_file, destination):

    if not os.path.exists(zip_file):
        logging.error("Zip file not found")
        return

    os.makedirs(destination, exist_ok = True)

    with zipfile.ZipFile(zip_file, "r") as zobj:
        zobj.extractall(destination)

    logging.info("Restore completed successfully")