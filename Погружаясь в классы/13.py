from abc import ABC, abstractmethod


class Enumerable(ABC):
    @abstractmethod
    def get_iterator(self):
        pass

    # BEGIN
    def max_by(self, fn):
        items = list(self.get_iterator())
        result = max(items, key=fn, default=None)
        return result
    # END
