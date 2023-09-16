class Town:
    def __init__(self, title):
        self.title = title
        self.residents = []
        self.post_offices = []

    def add_residents(self, resident):
        self.residents.append(resident)

    def add_post_offices(self, postoffice):
        self.post_offices.append(postoffice)
