import numpy as np
from pyasn1_modules.rfc2437 import rsaOAEPEncryptionSET


class Road:

    def __init__(self,
                 starting_position,
                 end_position):

        self.starting_position = starting_position
        self.end_position = end_position
        self.length = self.end_position - self.starting_position