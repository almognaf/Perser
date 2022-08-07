import sqlite3
import fileNameParse
import parsecef

conn = sqlite3.connect('RespirationScan_markes.db')
curser = conn.cursor()


# ON FOLDER CHANGE
fileDic = fileNameParse.listDir(fileNameParse.FOLDER_PATH)
print(fileDic)

# Latest tube_sn test
curser.execute("SELECT * FROM InvivoMeasurement,InvitroMeasurements  WHERE tube_sn=? AND (`experiment_id`,`end_time`) IN" +
               " (SELECT experiment_id,MAX(end_time) FROM InvivoMeasurements,InvitroMeasurements GROUP BY `experiment_id`)",(fileDic["tube_sn"],))
latest_test = curser.fetchall()[0][0]


# Iterate measurement id:
curser.execute("SELECT MAX(measurement_id) FROM InvivoMeasurements ")
curr_id = curser.fetchall()[0][0]
print(curr_id)
measurement_id = curr_id + 1

# Create MEASUREMENT
curser.execute("""CREATE TABLE Measurement (
                       id int,
                       type_id int,
                       era_id int,
                       time_analysis TIMESTAMP,
                       internal_standards_set_id int,
                       analyzer_id int,
                       injection_pos int,
                       chromatogram varchar(255),
                       cef varchar(255)
)""")


# Insert new MEASUREMENT (to be done)
curser.execute("INSERT INTO Measurement VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(measurement_id,))



# Update latest test's measurement_id
curser.execute("""UPDATE %s SET measurement_id = %s
            WHERE experiment_id = %s  
""",) # (InvivoMeasurements\InvitroMeasurements, measurement_id, latest_test[experiment_id])



#curser.execute("SELECT * FROM InvivoMeasurements WHERE tube_id=?",(2,))
#conn.commit()
#conn.close()



