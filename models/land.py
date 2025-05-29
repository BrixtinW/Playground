class Land:
    def __init__(self, name, owner=None, numPeasants=1, housing=4, charactersPresent=None, is_captial=False):
        self.name = name
        self.numPeasants = numPeasants
        self.numAvailablePeasants = numPeasants
        self.housing = housing
        self.owner = owner
        self.is_capital = is_captial
        if charactersPresent is None:
            self.charactersPresent = []
        else:
            self.charactersPresent = charactersPresent 