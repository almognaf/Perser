import openpyxl
import json
from openpyxl import Workbook, load_workbook
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string



def get_cur_sample_range(cur_row, sheety):
    res = 0
    found = False
    i = 1
    while not found:
        coord = 'A' + str(int(cur_row) + i)
        if str(sheety[coord].value).__contains__("Sample"):
            res = int(i)
            found = True
            break
        i += 1

        if int(cur_row) + i == sheety.max_row:
            #print("range is:", i)
            return i
    #print("range is:", i)
    return res


def get_report(current_row, sheets):
    tube_num = None
    thermal = None
    deorb = None
    found = False
    i = 1
    while not found and not str(sheets['A' + str(int(current_row) + i)].value).__contains__("Sample"): # while not reached to next sample

            coord = 'C' + str(int(current_row) + i)
            if str(sheets[coord].value).__contains__("Tube Number"):
                tube_num = int(sheets['I' + str(int(current_row) + i)].value)
            if str(sheets[coord].value).__contains__("Thermal Cycles"):
                thermal = int(sheet['I' + str(int(current_row) + i)].value)
            if str(sheets[coord].value).__contains__("Desorb Start Time"):
                deorb = str(sheets['I' + str(int(current_row) + i)].value)

            i += 1
            if int(current_row) + i == sheets.max_row:
                break

    return tube_num, thermal, deorb


if __name__ == '__main__':

    # enter your file path
    path = './rawdata.xlsx'

    # load excel file
    book = openpyxl.load_workbook(path)

    # select the sheet
    sheet = book['SeqReport']



    sampleCol = 'A'
    sampleRow = '1'
    sample_row_count = '0' # check if reached last sample
    curr_row = '0'
    flag = True
    File = ""
    Method = ""
    Tube = 0
    Tube_Number = 0
    Thermal_Cycles = 0
    Desorb_Start_Time = ""
    samples = []

    while flag and (int(sampleRow) < sheet.max_row):

         if str(sheet[sampleCol+sampleRow].value).__contains__("Sample"):
            curr_row = str(sampleRow)
            #print(str(sheet[sampleCol+sampleRow].value)+":")
            curr_sample_range = get_cur_sample_range(curr_row, sheet)

            curr_sample = dict()
            while int(sample_row_count) < curr_sample_range:



                    curr_row = str(int(curr_row) + 1)
                    if str(sheet['B'+curr_row].value).__contains__("File"):
                      #  print(" File:",sheet['F'+curr_row].value)
                        File = sheet['F'+curr_row].value
                        curr_sample["File"] = File
                    if str(sheet['B' + curr_row].value).__contains__("Method:"):
                       # print(" Method:", sheet['F' + curr_row].value)
                        Method = sheet['F' + curr_row].value
                        curr_sample["Method"] = Method
                    if str(sheet['B' + curr_row].value).__contains__("Markes"):
                        fixed_row = str(int(curr_row) + 2) # tube start after 2 rows
                        Tube = int(sheet['I' + fixed_row].value)
                        curr_sample["Tube"] = Tube
                       # print(" Tube:", Tube )
                    if str(sheet['B' + curr_row].value).__contains__("Report"):
                        Tube_Number, Thermal_Cycles, Desorb_Start_Time = get_report(curr_row, sheet)
                        curr_sample["Tube_Number"] = Tube_Number
                        curr_sample["Thermal_Cycles"] = Thermal_Cycles
                        curr_sample["Desorb_Start_Time"] = Desorb_Start_Time
                        #print(" Tube_Number:",Tube_Number,"\n","Thermal_Cycles:", Thermal_Cycles,"\n","Desorb_Start_Time:", Desorb_Start_Time)

                    sample_row_count = str(int(sample_row_count) + 1)


            samples.append(curr_sample)

            sample_row_count = '0'

         sampleRow = str(int(sampleRow) + 1)


print(samples)


with open('result.json', 'w') as fp:
    json.dump(samples, fp , indent=4)




