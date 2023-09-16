class Town:
    """
    This class is currently unused but could be used in future methods if one needs to specify the town a resident
    lives in (so one could specify the town the recipient lives in, and the program than works out the right
    post office to send the letter to - rather than depositing it directly at the post office).

    The intention of this class would be to act as a container for the residents, and post offices that are
    located within the town.
    """
    def __init__(self, title):
        """
        The only paramater specified is the name of the town.
        The resident and post office lists dictate which residents and post offices are located in the town.
        """
        self.title = title
        self.residents = []
        self.post_offices = []

    def add_residents(self, resident):
        """
        This adds a specific instance of the resident class to the town's resident list.
        """
        self.residents.append(resident)

    def add_post_offices(self, postoffice):
        """
        This adds a specific instance of the post office class to the town's post office list.
        """
        self.post_offices.append(postoffice)
