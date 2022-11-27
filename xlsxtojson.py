import openpyxl
import json
import time

""" get_cur_sample_range
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


""" get_report()
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
            thermal = int(sheets['I' + str(int(current_row) + i)].value)
        if str(sheets[coord].value).__contains__("Desorb Start Time"):
            deorb = str(sheets['I' + str(int(current_row) + i)].value)

        i += 1
        if int(current_row) + i == sheets.max_row:
            break

    return tube_num, thermal, deorb


def create_json(to_json):
    with open('C:/Users/alnaf/Perser/Jsons/' + 'result_' + str(time.time()) + '.json', 'w') as fp:
        json.dump(to_json, fp, indent=4)
        fp.close()

def xlsx_to_json(xlsx_path):
    path = xlsx_path
    # path = 'Reports/rawdata.xlsx'

    # load excel file
    book = openpyxl.load_workbook(path)

    # select the sheet
    sheet = book['SeqReport']

    sample_col = 'A'
    sheet_curr_row = '1'
    # sample_row_count to handle last sample case and for make sure we in range
    sample_row_count = '0'
    curr_row = '0'
    file = ""
    method = ""
    tube = 0
    tube_number = 0
    thermal_cycles = 0
    desorb_start_time = ""
    samples = []
    curr_sample = {}

    #  while loop to go over the samples in the Excel sheet without overflowing
    while int(sheet_curr_row) < sheet.max_row:

        if str(sheet[sample_col + sheet_curr_row].value).__contains__("Sample"):
            curr_row = str(sheet_curr_row)
            # taking the number of rows we have till the next sample
            curr_sample_range = get_cur_sample_range(curr_row, sheet)

            #  While loop to make sure we will parse each sample data as individual and to prevent overflow
            while int(sample_row_count) < curr_sample_range:

                curr_row = str(int(curr_row) + 1)
                #  if statement for parsing relevant data inside "File" area if we there
                if str(sheet['B' + curr_row].value).__contains__("File"):
                    #  taking the value inside col 'F' at our curr_row
                    file = sheet['F' + curr_row].value
                    curr_sample["File"] = file

                #  if statement for parsing relevant data inside "Method" area if we there
                if str(sheet['B' + curr_row].value).__contains__("Method:"):
                    #  taking the value inside col 'F' at our curr_row
                    method = sheet['F' + curr_row].value
                    curr_sample["Method"] = method

                #  if statement for parsing relevant data inside "Markes" area if we there
                if str(sheet['B' + curr_row].value).__contains__("Markes"):
                    # tube start after 2 rows
                    fixed_row = str(int(curr_row) + 2)
                    tube = int(sheet['I' + fixed_row].value)
                    curr_sample["Tube"] = tube

                #  if statement for parsing relevant data inside "Report" area if we there
                if str(sheet['B' + curr_row].value).__contains__("Report"):
                    #  using the get_report function we can fetch the data we need from "Report" section
                    tube_number, thermal_cycles, desorb_start_time = get_report(curr_row, sheet)
                    curr_sample["Tube_Number"] = tube_number
                    curr_sample["Thermal_Cycles"] = thermal_cycles
                    curr_sample["Desorb_Start_Time"] = desorb_start_time

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
               sheetCurrRow !< sheet.max_row = end of excel sheet and program
            """
        sheet_curr_row = str(int(sheet_curr_row) + 1)

    openpyxl.Workbook.close(book)
    #  taking the dict array made from the Excel sheet we received and creating the Json we need

    create_json(samples)


