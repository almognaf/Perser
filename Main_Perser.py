
import time
import Main_Perser


import fileNameParse


def extract_filename_data_to_dict(file_name):
    name = file_name.split('/')
    # TODO: Check if name is valid
    fixed_name = (name[6])[0:len(name[6]) - 1]
    print(fixed_name)
    file_dic = fileNameParse.list_dir(fixed_name)
    print(file_dic)
    return file_dic


class MainPerser:
    def __init__(self, file_path: str):
        self.filename = file_path
        self.filename_fixed = extract_filename_data_to_dict(self.filename)

    def print(self):
        print(self.filename)
