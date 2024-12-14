class HTMLElement:
    def __init__(self, attributes=None):
        if attributes is None:
            self.attributes = {}
        else:
            self.attributes = attributes

    def get_attribute(self, key):
        return self.attributes.get(key)

    # BEGIN
    def add_tag(self, tag_name):
        tags = self._get_tags()
        new_tags = list(dict.fromkeys(tags + [tag_name]))
        self.attributes['tag'] = self._stringify_tags(new_tags)

    def remove_tag(self, tag_name):
        tags = self._get_tags()
        new_tags = [tag for tag in tags if tag != tag_name]
        self.attributes['tag'] = self._stringify_tags(new_tags)

    def toggle_tag(self, tag_name):
        if tag_name in self._get_tags():
            self.remove_tag(tag_name)
            return
        self.add_tag(tag_name)

    def _get_tags(self):
        attribute = self.get_attribute('tag') or ''
        return attribute.split(' ')

    def _stringify_tags(self, tags):
        return ' '.join(tags)
    # END
