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


# ON FOLDER CHANGE
def getFileDic():
    # "tube_sn","time_analysis","analyzer_id","injection_pos","injection_pos","not_sure":
    Dic = fileNameParse.listDir(fileNameParse.FOLDER_PATH)
    print(Dic)
    return Dic


# Latest tube_sn's test
def getLatestTestByTubeSn(tube_sn):
    curser.execute("""SELECT * 
                        FROM InvivoMeasurement,InvitroMeasurements
                             WHERE tube_sn=%s AND (`experiment_id`,`end_time`) IN
                                (SELECT experiment_id,MAX(end_time) 
                                    FROM InvivoMeasurements,InvitroMeasurements GROUP BY `experiment_id`)""",
                                          (tube_sn,))
    return curser.fetchall()[0][0]


# Iterate measurement id:
def getMeasurementId():
    curser.execute("SELECT MAX(id) FROM Measurement ")
    curr_id = curser.fetchall()[0][0]
    measurement_id = (curr_id + 1) if curr_id else 1 # Check if Measurement Table is empty to initialize iterator
    print(measurement_id)
    return measurement_id;


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


# Insert new MEASUREMENT (to be done)
def insertMeasurement(measurement_id,type_id,era_id,time_analysis,internal_st,analyzer_id,injection_pos,chromatogram,cef):
    curser.execute("INSERT INTO Measurement VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                   (measurement_id,type_id,era_id,time_analysis,internal_st,analyzer_id,injection_pos,chromatogram,cef))
    mydb.commit();


def insertMeasurementTEST(measurement_id,time_analysis,analyzer_id,injection_pos,internal_st):
    curser.execute("""INSERT INTO Measurement (id,time_analysis,analyzer_id,injection_pos,internal_standards_set_id) 
                               VALUES (%s,%s,%s,%s,%s)""",
                   (measurement_id, time_analysis, analyzer_id, injection_pos, internal_st))
    mydb.commit();


# Update latest test's measurement_id (cross reference)
def updateLatestTest(table_name,measurement_id,test_id):
     curser.execute("""UPDATE %s SET measurement_id = %s
                WHERE experiment_id = %s""",
                    (table_name,measurement_id,test_id))


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
        inv_test = getLatestTestByTubeSn(tube_sn)
        if measurement.time_stamp < inv_test.time_stamp:
            measurement.time_stamp = inv_test.time_stamp
            measurement.type_id = inv_test.type_id;
            inv_test.measurement_id = measurement.id


#conn.commit()
#conn.close()

if __name__ == '__main__':
    fileDic = getFileDic()
    currID = getMeasurementId()

    insertMeasurementTEST(currID,fileDic["time_analysis"],fileDic["analyzer_id"],fileDic["injection_pos"],fileDic["internal_standards_set"])
    mydb.commit();

    print(curser.fetchall())

    #curser.execute("""INSERT TO measurement (""")


