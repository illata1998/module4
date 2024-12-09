import copy


# BEGIN
class InMemoryKV():
    def __init__(self, initial=None):
        if initial is None:
            self.map = {}
        else:
            self.map = copy.deepcopy(initial)

    def set_(self, key, value):
        self.map[key] = value

    def unset_(self, key):
        self.map.pop(key)

    def get_(self, key, default=None):
        return self.map.get(key, default)

    def to_dict(self):
        return copy.deepcopy(self.map)
# END
