from datetime import datetime
from Classes.Measurement import *

FOLDER_PATH = 'C:/Users/alnaf/Perser/perses-main-data-new CEF/data/test'


def get_time_analysis(date_time_str):
    # FORMAT: YYYY_MM_DD_HH_MM_SS
    fixed_time = date_time_str.split('_')
    fixed_time[0] = (fixed_time[0])[2:4]
    time_to_str = fixed_time[2] + '/' + fixed_time[1] + '/' + fixed_time[0] + ' ' + fixed_time[3] + ':' + fixed_time[4] + ':' + fixed_time[5]
    timestamp = datetime.strptime(time_to_str, '%d/%m/%y %H:%M:%S')

    return timestamp


def check():
    print("did")


def list_dir(file_name):  # NEED TO RECIEVE FILES PATH OR NAME AS PARAM (?)
    measurment = Measurment()
    file_array = file_name.split('-')
    print(file_array)
    file_dict = dict(tube_sn=file_array[0], time_analysis=get_time_analysis(file_array[1]), analyzer_id=file_array[2],
                     injection_pos=file_array[3], internal_standards_set=file_array[4], not_sure=file_array[5])

    return file_dict


if __name__ == '__main__':
    file_dict = list_dir(FOLDER_PATH)
    print(file_dict["time_analysis"])
