from parser import curser


def get_compound_id():

    curser.execute("SELECT MAX(id) FROM Compound ")

    if len(curser.fetchall()) != 0:
        curr_id = curser.fetchall()[0][0]
        compound_id = (curr_id + 1) if curr_id else 1
    else:
        compound_id = 1

    return compound_id


class Compound:

    def __int__(self, measurment_id, mass, retention_time, max_value, area=None):
        """
        Construct a new 'Compound' object.

        :param id: int
        :param measurment_id: int
        :param mass: float
        :param retention_time: float
        :param area: float
        :param max_value: float
        :return: returns nothing
        """
        self.id = get_compound_id()  # int
        self.measurment_id = measurment_id  # int
        self.mass = mass  # float
        self.retention_time = retention_time  # float
        # TODO: Check from where to get max_value
        self.max_value = max_value  # float
        self.id = get_compound_id()  # int
        if area is None:
            self.area = -1  # float















