import sqlite3
import fileNameParse
import parsecef
import mysql.connector

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="lustersoul123",
    database="respirationscan"
)
curser = mydb.cursor()


## MUST READ THIS ##
# TO TEST INSERT MUST EDIT FILE NAME IN PERSER\DATA\TEST\x-2018_09_19_01_55_19-x-x-x-x.cef
# EDIT ONLY 'x' PLACE HOLDERS (no need to change date)


# ON FOLDER CHANGE
def getFileDic():
    # "tube_sn","time_analysis","analyzer_id","injection_pos","injection_pos","not_sure":
    dic = fileNameParse.list_dir(fileNameParse.FOLDER_PATH)
    print(dic)
    return dic


# Latest tube_sn's test
def get_typeid(tube_sn, invivo=[], invitro=[]):
    curser.execute("""SELECT * 
                        FROM InvivoMeasurement,InvitroMeasurements
                             WHERE tube_sn=%s AND (`experiment_id`,`end_time`) IN
                                (SELECT experiment_id,MAX(end_time) 
                                    FROM InvivoMeasurements,InvitroMeasurements GROUP BY `experiment_id`)""",
                   (tube_sn,))
    return curser.fetchall()[0][0]



def getLatestTestByTubeionilalaSn(tube_sn):
    curser.execute("""SELECT measurment_id 
                        FROM InvivoMeasurement,InvitroMeasurements
                             WHERE tube_sn=%s AND (`experiment_id`,`end_time`) IN
                                (SELECT experiment_id,MAX(end_time) 
                                    FROM InvivoMeasurements,InvitroMeasurements GROUP BY `experiment_id`)""",
                   (tube_sn,))
    return curser.fetchall()[0][0]

def getLatestTestByTubeionilalaSn(measurment_id):
    curser.execute("""SELECT type_id 
                        FROM Measurment
                             WHERE id=%s""",
                   (measurment_id,))
    return curser.fetchall()[0][0]

type_id = getLatestTestByTubeionilalaSn(getLatestTestByTubeionilalaSn(tube_sn))
# Iterate measurement id:
def getMeasurementId():
    curser.execute("SELECT MAX(id) FROM Measurement ")
    curr_id = curser.fetchall()[0][0]
    measurement_id = (curr_id + 1) if curr_id else 1  # Check if Measurement Table is empty to initialize iterator
    print(measurement_id)
    return measurement_id


# Create MEASUREMENT
def createMeasurementTable():
    curser.execute("""CREATE TABLE Measurement (
                           id int NOT NULL PRIMARY KEY,
                           type_id int,
                           era_id int,
                           time_analysis TIMESTAMP,
                           internal_standards_set_id int,
                           analyzer_id int,
                           chromatogram varchar(255),
                           cef varchar(255)
    )""")


# Insert new MEASUREMENT (to be done) # DO NOT USE - INSTEAD , USE insertMeasurementTEST for now
def insertMeasurement(measurement_id, type_id, era_id, time_analysis, internal_st, analyzer_id, injection_pos,
                      chromatogram, cef):
    curser.execute("INSERT INTO Measurement VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   (measurement_id, type_id, era_id, time_analysis, internal_st, analyzer_id, injection_pos,
                    chromatogram, cef))
    mydb.commit()


# MEANWHILE USE THIS FUNC FOR THE TEST
def insertMeasurementTEST(measurement_id, time_analysis, analyzer_id, injection_pos, internal_st):
    curser.execute("""INSERT INTO Measurement (id,time_analysis,analyzer_id,injection_pos,internal_standards_set_id) 
                               VALUES (%s,%s,%s,%s,%s)""",
                   (measurement_id, time_analysis, analyzer_id, injection_pos, internal_st))

    mydb.commit()


#Insert Measurement TYPE - NOT SURE HOW TO GET TYPE_ID
def insertMeasurementType(measurement_id, type_id=1):
    curser.execute("""INSERT INTO MeasurementType (id,type) 
                                 VALUES (%s,%s)""",
                   (measurement_id, type_id))
    mydb.commit()


# Insert ERA time and era_id - NOT SURE HOW TO GET TIME AND ERA_ID
def insertEra(time_analysis, era_id=1):
    curser.execute("""INSERT INTO era (id,date_start) 
                                 VALUES (%s,%s)""",
                   (era_id, time_analysis))
    mydb.commit()


# Insert internal Standard - NOT SURE ABOUT INTERNAL_STANDARD_ID
def insertInternalStandard(measurement_id, internal_standards_set, analyzer_id):
    curser.execute("""INSERT INTO internalstandard (id,analyzer_id) 
                                     VALUES (%s,%s)""",
                   (measurement_id, analyzer_id))
    mydb.commit()

    curser.execute("""INSERT INTO internalstandardsset (id,internal_standard_id) 
                                 VALUES (%s,%s)""",
                   (internal_standards_set, measurement_id))
    mydb.commit()


#Insert Analyzer - Analyzer ID from file name
def insertAnalyzer(analyzer_id, brand=1):
    print(analyzer_id)
    query = "INSERT INTO analyzer (id,brand) VALUES (%s,%s)"
    curser.execute(query, (analyzer_id, brand))
    mydb.commit()


# Update latest test's measurement_id (cross reference)
def updateLatestTest(table_name, measurement_id, test_id):
    curser.execute("""UPDATE %s SET measurement_id = %s
                WHERE experiment_id = %s""",
                   (table_name, measurement_id, test_id))


def getMeasurementByTubeSn(tube_sn):
    curser.execute("""SELECT * 
                         FROM Measurement
                              WHERE tube_sn=%s""",
                   (tube_sn,))
    return curser.fetchall()[0][0]


# For each tube_sn => get measurement by sn => get latest invivo/invitro test =>
# check if test time stamp is updated to date by checking time tamp =>
# if not , update relevant fields and cross-reference.
def cross_reference_maintenance(tube_sn_list):
    for tube_sn in tube_sn_list:
        measurement = getMeasurementByTubeSn(tube_sn)
        inv_test = get_typeid(tube_sn)
        if measurement.time_stamp < inv_test.time_stamp:
            measurement.time_stamp = inv_test.time_stamp
            measurement.type_id = inv_test.type_id
            inv_test.measurement_id = measurement.id



def handleNewFile():
    # IN PARAMETERS : SHOULD GET NEW FILE NAME FROM FILE MONITOR
    # MUST INSERT VALUES IN THIS ORDER BECAUSE OF FOREIGN KEYS DEPENDENCIES
    file_dic = getFileDic()
    curr_id = getMeasurementId()
    insertAnalyzer(file_dic["analyzer_id"])
    insertInternalStandard(curr_id, file_dic["internal_standards_set"], file_dic["analyzer_id"])
    insertEra(file_dic["analyzer_id"])
    insertMeasurementType(curr_id)
    insertMeasurementTEST(curr_id, file_dic["time_analysis"], file_dic["analyzer_id"],
                          file_dic["injection_pos"], file_dic["internal_standards_set"])


if __name__ == '__main__':
    handleNewFile()


