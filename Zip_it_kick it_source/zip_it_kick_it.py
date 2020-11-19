import os.path
import zipfile
import time
import json
import os.path
from os import path

#GLOBALS
timestr = time.strftime("%Y%m%d-%H%M%S")
now = time.time()


def createfolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def zip():
    try:
        json_file = open("data/config_data.json")
        variables = json.load(json_file)
        archive_location = variables["archive_location"]
        target_location = variables["target_location"]
        days = variables["days"]
        length = len(target_location)
        with zipfile.ZipFile(archive_location+"/"+timestr+'.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
            for root, dirs, files in os.walk(target_location, topdown=False):
                folder = root[length:]
                for file in files:
                    if os.path.getmtime(os.path.join(root, file)) < now - days * 86400:
                        my_zip.write(os.path.join(root, file), os.path.join(folder, file))

            json_file.close()

    except OSError:
        print('Error: zipping. ' + target_location)
    else:
        return True

    json_file = open("data/config_data.json")
    variables = json.load(json_file)
    archive_location = variables["archive_location"]
    if len(os.listdir(archive_location + "/" + timestr + '.zip')) == 0:
        print("Directory is empty")
    else:
        print("Directory is not empty")
    json_file.close()


def delete():
    try:
        json_file = open("data/config_data.json")
        variables = json.load(json_file)
        target_location = variables["target_location"]
        days = variables["days"]
        for root, dirs, files in os.walk(target_location):
            for file in files:
                if os.path.getmtime(os.path.join(root, file)) < now - days * 86400:
                    os.remove(os.path.join(root, file))
        json_file.close()
    except OSError:
        print('Error: deleting. ' + target_location)


def check_path(location):
    if path.exists(location):
        return True
    else:
        return False

def empty_check():
    json_file = open("data/config_data.json")
    variables = json.load(json_file)
    archive_location = variables["archive_location"]
    zp= zipfile.ZipFile(archive_location+"/"+timestr+'.zip')
    size = sum([zinfo.file_size for zinfo in zp.filelist])
    zip_kb = float(size) / 1000  # kB
    print(zip_kb)
    zp.close()
    if zip_kb <= 0:
        print("Directory is empty")
        os.remove(archive_location+"/"+timestr+'.zip')
    else:
        print("Directory is not empty")
    json_file.close()

def main():
    json_file = open("data/config_data.json")
    variables = json.load(json_file)
    archive_location = variables["archive_location"]
    target_location = variables["target_location"]
    if check_path(archive_location) is True and check_path(target_location) is True:
        print("paths are good")
        if zip() is True:
            delete()
            print("complete")

        else:
            print("error")

    else:
        print("File path error")


    json_file.close()


main()
empty_check()
