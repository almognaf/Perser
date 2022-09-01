from parser import curser


def get_algorithm_id():
    curser.execute("SELECT MAX(id) FROM AlgorithmMatch ")

    if len(curser.fetchall()) != 0:
        curr_id = curser.fetchall()[0][0]
        algo_id = (curr_id + 1) if curr_id else 1
    else:
        algo_id = 1

    return algo_id


class AlgorithmMatch:
    def __int__(self, algorithm, compound_id, cas_rn, probability):
        """
        Construct a new 'AlgorithmMatch' object.

        :param id: int
        :param algorithm: text
        :param compound_id: int
        :param cas_rn: varchar
        :param probability: float
        :return: returns nothing
        """

        # #TODO: How to populate
        self.id = get_algorithm_id()
        self.algorithm = algorithm
        self.compound_id = compound_id
        self.cas_rn = cas_rn
        self.probability = probability
