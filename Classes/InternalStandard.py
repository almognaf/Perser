import sqlite3
import fileNameParse
import parsecef
import mysql.connector

from parser import curser


# def get_compound_id():
#     curser.execute("SELECT MAX(id) FROM Compound ")
#
#     if len(curser.fetchall()) != 0:
#         curr_id = curser.fetchall()[0][0]
#         compound_id = (curr_id + 1) if curr_id else 1
#     else:
#         compound_id = 1
#
#     return compound_id


class InternalStandard:
    def __int__(self, id, name, analyzer_id, retention_time, retention_time_stdev,cas_rn):
        """
        Construct a new 'InternalStandard' object.

        :param id: int
        :param name: text
        :param analyzer_id: int
        :param retention_time: float
        :param retention_time_stdev: float
        :param cas_rn: varchar
        :return: returns nothing
        """
        # #TODO: How to populate
        self.id = id # iterate id (not sure)
        self.name = name
        self.analyzer_id = analyzer_id
        self.retention_time = retention_time  # rt in parscef
        self.retention_time_stdev = retention_time_stdev # standard deviation
        self.cas_rn = cas_rn # cas id


class InternalStandardSet:
    def __int__(self, id, internal_standard_id):
        """
        Construct a new 'InternalStandardSet' object.

        :param id: int
        :param internal_standard_id: int

        :return: returns nothing
        """

        # # TODO: How to populate
        self.id = id
        self.internal_standard_id = internal_standard_id #TODO
