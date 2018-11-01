class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "My guitar: {}, first made in {}".format(self.name, self.year)

    def get_age(self):
        age = 2018 - self.year
        self.age = age
        return self.age

    def is_vintage(self):
        if self.age > 50:
            return True
        else:
            return False