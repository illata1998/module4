from HTMLElement import HTMLElement


class HTMLImgElement(HTMLElement):
    ATTRIBUTE_NAMES = ['src']

    @classmethod
    def get_attribute_names(cls):
        return super().ATTRIBUTE_NAMES + cls.ATTRIBUTE_NAMES

    # BEGIN
    def is_valid(self):
        attributes = self.get_attributes()
        names = attributes.keys()
        valid_names = self.get_attribute_names()
        diff = names - set(valid_names)

        return not diff
    # END
