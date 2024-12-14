class Base:
    # BEGIN
    def is_instance_of(self, class_name):
        classes = list(map(lambda c: c.__name__, self.__class__.__mro__))
        return class_name in classes
    # END
