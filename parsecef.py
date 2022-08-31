#!/usr/bin/env python
# coding: utf-8
# In[1]:
import Classes.Compound

import json
import xml.etree.ElementTree as ET


class ParseCEF:

    def __int__(self, cef_file_path, curr_id):

        self.filePath = cef_file_path
        self.measurment_Id = curr_id

        # In[36]:

        tree = ET.parse(self.filePath)
        root = tree.getroot()

        # Loop through each compound
        for compound in root.iter("Compound"):
            # get m, rt, a, y
            loc = compound.find("Location")
            location = loc.attrib

            m = float(location["m"])
            rt = float(location["rt"])
            a = int(location["a"])
            y = int(location["y"])
            curr_compound = Classes.Compound(curr_id, m, rt, a)
            # get formula, name, probability
            mol = compound.find("Results/Molecule")
            curr_compound_id = curr_compound.id
            molecule = mol.attrib
            # if molecule["name"]:
            #     print(molecule["name"])
            # else:
            #     print(-1)

            formula = molecule["formula"]
            name = molecule["name"]
            probability = molecule["probability"]

            # get CAS ID
            acc = mol.find("DataBase/Accession")
            accession = acc.attrib

            cas = accession["id"]

            # get spectrum
            spec = compound.find("Spectrum/MSPeaks")
            x = []
            y = []
            spec_tuples = []  # spectrum as list of tuples

            for peak in spec.iter("p"):
                x_val = float(peak.attrib["x"])
                y_val = float(peak.attrib["y"])

                # spectrum as list
                x.append(x_val)
                y.append(y_val)

                # spectrum tuple
                spec_tuples.append((x_val, y_val))

            # spectrum arrays for x, y in dict
            spec_dict = {"x": x, "y": y}

            json_dict = json.dumps(spec_dict)
            json_tuples = json.dumps(spec_tuples)

            # print collected compound information
            print(f"m: {m}, rt: {rt}, a: {a}, y: {y}")
            print(f"{formula}, {name}, cas: {cas} prob: {probability}")
            print(f"x: {x}, y: {y}")
            # print(spec_list)
