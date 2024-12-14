class GoogleStorage:
    def __init__(self):
        self.elements = {}

    # BEGIN
    def get(self, key):
        return self.elements.get(key)

    def set(self, key, value):
        self.elements[key] = value

    def count(self):
        raise Exception("Can't be calculated")
    # END
