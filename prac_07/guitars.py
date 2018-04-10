class Guitar:

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2018 - self.year
        return age

    def is_vintage(self):
        return self.get_age() > 50
