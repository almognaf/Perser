import os
from datetime import datetime

FOLDER_PATH = r'C:\\Users\\natanel\\Desktop\\Perser\\perses-main-data-new CEF\\data\\test'


def get_time_analysis(date_time_str):
    # FORMAT: YYYY_MM_DD_HH_MM_SS
    fixedTime = date_time_str.split('_')
    fixedTime[0] = (fixedTime[0])[2:4]
    timeToStr = fixedTime[2] + '/' + fixedTime[1] + '/' + fixedTime[0] + ' ' + fixedTime[3] + ':' + fixedTime[4] + ':' + fixedTime[5]
    timestamp = datetime.strptime(timeToStr, '%d/%m/%y %H:%M:%S')
    return timestamp




def listDir(dir): # NEED TO RECIEVE FILES PATH OR NAME AS PARAM (?)

    fileNames = os.listdir(dir)
    name, type = os.path.splitext(fileNames[0])
    fileArray = name.split('-')
    fileDic = {
        "tube_sn": fileArray[0],
        "time_analysis": get_time_analysis(fileArray[1]),
        "analyzer_id": fileArray[2],
        "injection_pos": fileArray[3],
        "internal_standards_set": fileArray[4],
        "not_sure": fileArray[5],
    }
    return fileDic;


if __name__ == '__main__':
    fileDic = listDir(FOLDER_PATH)
    print(fileDic["time_analysis"])
