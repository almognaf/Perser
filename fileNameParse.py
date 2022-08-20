import os


# Folder Path
FOLDER_PATH = r'C:\\Users\\alnaf\\Perser\\perses-main-data-new CEF\\data\\FileName2Parse'


def listDir(dir): # NEED TO RECIEVE FILES PATH OR NAME AS PARAM (?)

    fileNames = os.listdir(dir)
    name, type = os.path.splitext(fileNames[0])
    fileArray = name.split('-')
    fileDic = {
        "tube_sn": fileArray[0],
        "analyzer_id": fileArray[1],
        "internal_standards_set_id": fileArray[2],
        "injection_pos": fileArray[3],
        "time_analysis": fileArray[4],
        "not_sure": fileArray[5],
    }
    return fileDic;


if __name__ == '__main__':
    fileDic = listDir(FOLDER_PATH)
    print(fileDic)