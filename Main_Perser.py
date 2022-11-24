
import time
from Classes import AlgorithmMatch,InternalStandard,Compound,Spectrum,Measurement
import parser,parsecef
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
        measurement = Measurement(type_id, 0, self.filename_dic["time_analysis"], self.filename_dic["internal_standards_set_id"],
                                                     self.filename_dic["analayzer_id"],
                                                            self.filename_dic["injection_pos"],chromotogram, cef) #TODO: chromo and cef

        parse_cef = parsecef.ParseCEF(file_path, measurment.id)

        spectrum = Spectrum([parse_cef.curr_compound.id], parse_cef.x, parse_cef.y, parse_cef.z) # TODO: Not sure what is z location

        internal_standard = InternalStandard.InternalStandard(name, self.filename_dic["analayzer_id"],
                                                                  parse_cef.rt, rt_stdev, parse_cef.cas) # TODO: name,rt_stdev

        internal_standard_set = InternalStandard.InternalStandardSet(measurment.internal_standards_set_id, internal_standard.id)

        algorithm_match = AlgorithmMatch(algorithm, compound_id, cas_rn, probability) #TODO: where to get all


     # SHOULD IMPLEMENT HANDLER WITH SQL SCRIPT TO PUSH ALL TO DB

    def print(self):
        print(self.filename)
