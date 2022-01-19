class Race:
    def __init__(self, name):
        self.name = name
        self.drivers = []
        # An empty list that will contain all the drivers (objects) participating in the race

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name cannot be an empty string!")
        self.__name = value

