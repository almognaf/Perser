from parser import curser


def get_spectrum_id(compound_id):

    curser.execute("SELECT MAX(id) FROM Spectrum where compound_id =%s ", compound_id)

    if len(curser.fetchall()) != 0:
        curr_id = curser.fetchall()[0][0]
        spectrum_id = (curr_id + 1) if curr_id else 1
    else:
        spectrum_id = 1

    return spectrum_id


class Spectrum:

    def __int__(self, compound_id, x, y, z):
        """
               Construct a new 'Spectrum' object.

               :param id: int
               :param compound_id: int
               :param x: int
               :param y: int
               :param z: int
               :return: returns nothing
               """
        self.compound_id = compound_id
        self.x = x
        self.y = y
        self.z = z
        self.spectrum_id = get_spectrum_id(self.compound_id)