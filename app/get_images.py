import base64
import os

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



def get_all_images(location):
    encoded_image_list = []
    all_folders, all_images = listall("images") 
    for image in all_images:
        with open(image, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            encoded_image_list.append(encoded_string)
    return encoded_image_list