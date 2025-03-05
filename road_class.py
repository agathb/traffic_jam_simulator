class Road:

    def __init__(self,
                 starting_position,
                 end_position,
                 vertical_position):

        self.starting_position = starting_position
        self.end_position = end_position
        self.length = self.end_position - self.starting_position
        self.vertical_position = vertical_position