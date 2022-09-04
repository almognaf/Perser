
import time
import Main_Perser


import fileNameParse


def extract_filename_data_to_dict(file_name):
    name = file_name.split('/')
    # TODO: Check if name is valid
    fixed_name = (name[6])[5:len(name[6]) - 1]
    print(fixed_name)
    file_dic = fileNameParse.list_dir(fixed_name)
    print(file_dic)
    return file_dic


class MainPerser:
    def __init__(self, file_path: str):
        self.filename = file_path
        self.filename_dic = extract_filename_data_to_dict(self.filename)
        type_id = parser.get_typeid(self.filename_fixed["tube_sn"])
        #(self, type_id, era_id, time_analysis, internal_standards_set_id, analayzer_id, injection_pos, chromotogram, cef):
        measurment = Classes.Measurement(type_id, 0, self.filename_dic["time_analysis"], self.filename_dic["internal_standards_set_id"],
                                         self.filename_dic["analayzer_id"], self.filename_dic["injection_pos"], chromotogram, cef)


    def print(self):
        print(self.filename)
