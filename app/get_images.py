import base64
import os
import sqlite3

def listall(list_path):
    all_folders = []
    all_files = []
    for root,folders,files in os.walk(list_path):
    
        for eachfold in folders:
            all_folders.append(root.replace("\\","/")+"/"+eachfold.replace("\\","/"))
    
        for eachfile in files:
            all_files.append(os.path.join(root,eachfile))
            print(eachfile)
    
    return all_folders, all_files



def get_all_images(tag):
    encoded_image_list = []
    if tag == "main":
        all_folders, all_images = listall("images")
    else:     
        all_folders, all_images = listall(os.path.join("images", tag)) 
    for image in all_images:
        with open(image, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            encoded_image_list.append(encoded_string)
    return encoded_image_list

def get_data_database(database_name, table_name, tag):
    data = []
    with sqlite3.connect("database/" + database_name) as conn:
        if tag == "main":
            data = (conn.cursor().execute("select * from " + table_name).fetchall())
        else:
            data = (conn.cursor().execute("select * from " + table_name + " where tags= '" + tag + "'").fetchall())
        data = list(data)
    return data

def get_images(database_name, table_name, tag):
    with sqlite3.connect("database/" + database_name) as conn:
        if tag == "main":
            data = (conn.cursor().execute("select * from " + table_name).fetchall())
        else:
            data = (conn.cursor().execute("select * from " + table_name + " where tags= '" + tag + "'").fetchall())
        data = list(data)

    all_images = []

    for a in data:
      
        encoded_image_list = []
        with open(os.path.join("images", a[0]), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            encoded_image_list.append(encoded_string)
            all_images.append((a[0], a[1], a[2],encoded_string))
    return all_images

    

def get_all_cloths_data(tag):
    all_cloths_data = get_images("cloths_db", "cloth", tag)
    return all_cloths_data

def get_tags():
    with open("database/tags") as f:
        tags = f.readlines()
        tags = tags[0]
        tags = tags.split(",")
    print(tags)
    return (tags)

def get_new_image_id():
    images_list = listall("images")[1]
    images_length = len(images_list)
    return 99999 - images_length