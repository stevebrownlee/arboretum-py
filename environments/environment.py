class Environment:

    def __init__(self, name):
        self.name = name
        # capacity?
        self.inhabitants = []

    def __str__(self):
        return self.name
