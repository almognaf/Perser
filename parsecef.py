#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys
import xml.etree.ElementTree as ET
import json


# In[14]:

if __name__ == '__main__':

    cef_path = "perses-main-data-new CEF/data/new CEF/4-Set_1-TD_469869-BOA-PD-TD#_469869-Staph.Aureus_48_0-4h_Rep-1d-Exp_0-PA_0_2022-06-14_13-17-15_1_70eV_2022_06_21_11_00_38.cef"

    print_results = True


    # In[36]:


    tree = ET.parse(cef_path)
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

        # get formula, name, probability
        mol = compound.find("Results/Molecule")

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
        spec_tuples = [] # spectrum as list of tuples

        for peak in spec.iter("p"):

            x_val = float(peak.attrib["x"])
            y_val = float(peak.attrib["y"])

            # spectrum as list
            x.append(x_val)
            y.append(y_val)

            # spectrum tuple
            spec_tuples.append((x_val,y_val))

        # spectrum arrays for x, y in dict
        spec_dict = {"x": x, "y": y}

        json_dict   = json.dumps(spec_dict)
        json_tuples = json.dumps(spec_tuples)

        # print collected compound information
        if print_results:
            print(f"m: {m}, rt: {rt}, a: {a}, y: {y}")
            print(f"{formula}, {name}, cas: {cas} prob: {probability}")
            print(f"x: {x}, y: {y}")
            #print(spec_list)

