# BEGIN
class LabelTag:
    def __init__(self, text, tag):
        self.text = text
        self.tag = tag

    def render(self):
        return f'<label>{self.text}{self.tag}</label>'

    def __str__(self):
        return self.render()
# END
