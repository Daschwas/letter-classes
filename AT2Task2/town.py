class Town:
    def __init__(self, title):
        self.title = title
        self.residents = []

    def add_residents(self, resident):
        self.residents.append(resident)


