from HTMLElement import HTMLElement


# BEGIN
class HTMLHrElement(HTMLElement):
    def __str__(self):
        attr_line = self._stringify_attributes()
        return f'<hr{attr_line}>'
# END
