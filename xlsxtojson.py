import openpyxl
import json

"""
function for getting the number of rows of the current sample 
to prevent overflow or data override from the next sample, the
function receiving the first row of the current sample and the sheet,
and returns the number of rows from start of sample(X) till start of Sample(X + 1)  """


def get_cur_sample_range(cur_row, sheety):
    found = False
    i = 1
    while not found:
        coord = 'A' + str(int(cur_row) + i)
        if str(sheety[coord].value).__contains__("Sample"):
            break
        i += 1
        #  UseCase for the last Sample in sheet to ensure we won't overflow
        if int(cur_row) + i == sheety.max_row:
            return i
    return i


""" 
function that receiving the number of the current report's row and the sheet
and returns only the parameters we need from the "report" area. """


def get_report(current_row, sheets):
    tube_num = None
    thermal = None
    deorb = None
    found = False
    i = 1
    # while not reached to next sample
    while not found and not str(sheets['A' + str(int(current_row) + i)].value).__contains__(
            "Sample"):
        #  coord is parameter that holding the
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
    sheetCurrRow = '1'
    # sample_row_count to handle last sample case and for make sure we in range
    sample_row_count = '0'
    curr_row = '0'
    File = ""
    Method = ""
    Tube = 0
    Tube_Number = 0
    Thermal_Cycles = 0
    Desorb_Start_Time = ""
    samples = []
    curr_sample = {}

    #  while loop to go over the samples in the Excel sheet without overflowing
    while int(sheetCurrRow) < sheet.max_row:


        if str(sheet[sampleCol + sheetCurrRow].value).__contains__("Sample"):
            curr_row = str(sheetCurrRow)
            # taking the number of rows we have till the next sample
            curr_sample_range = get_cur_sample_range(curr_row, sheet)

            #  While loop to make sure we will parse each sample data as individual and to prevent overflow
            while int(sample_row_count) < curr_sample_range:

                curr_row = str(int(curr_row) + 1)
                #  if statement for parsing relevant data inside "File" area if we there
                if str(sheet['B' + curr_row].value).__contains__("File"):
                    #  taking the value inside col 'F' at our curr_row
                    File = sheet['F' + curr_row].value
                    curr_sample["File"] = File

                #  if statement for parsing relevant data inside "Method" area if we there
                if str(sheet['B' + curr_row].value).__contains__("Method:"):
                    #  taking the value inside col 'F' at our curr_row
                    Method = sheet['F' + curr_row].value
                    curr_sample["Method"] = Method

                #  if statement for parsing relevant data inside "Markes" area if we there
                if str(sheet['B' + curr_row].value).__contains__("Markes"):
                    # tube start after 2 rows
                    fixed_row = str(int(curr_row) + 2)
                    Tube = int(sheet['I' + fixed_row].value)
                    curr_sample["Tube"] = Tube

                #  if statement for parsing relevant data inside "Report" area if we there
                if str(sheet['B' + curr_row].value).__contains__("Report"):
                    #  using the get_report function we can fetch the data we need from "Report" section
                    Tube_Number, Thermal_Cycles, Desorb_Start_Time = get_report(curr_row, sheet)
                    curr_sample["Tube_Number"] = Tube_Number
                    curr_sample["Thermal_Cycles"] = Thermal_Cycles
                    curr_sample["Desorb_Start_Time"] = Desorb_Start_Time

                #  increasing the sample_row_count in 1
                sample_row_count = str(int(sample_row_count) + 1)

            #  Append a copy of the last dict to Samples[] for not loosing it in the next loop
            samples.append(curr_sample.copy())

            #  reset the sample_row_counter for the next sample in the loop
            sample_row_count = '0'

        """
           iterating the general sheet row (sheetCurrRow) in 1 every time we not in the inside
           Parsing while loop until one of the following conditions will happen (pseudo code):
           sheetCurrRow.value.contains("Sample") = parse new sample data
           or
           sheetCurrRow !< she et.max_row = end of excel sheet and program
        """
        sheetCurrRow = str(int(sheetCurrRow) + 1)

    #  taking the dict array made from the Excel sheet we received and creating the Json we need
    with open('result.json', 'w') as fp:
        json.dump(samples, fp, indent=4)
