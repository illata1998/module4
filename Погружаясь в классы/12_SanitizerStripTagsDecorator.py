from lxml import etree


def strip_tags(tag_string):
    parser = etree.HTMLParser()
    tree = etree.fromstring(tag_string, parser)
    return etree.tostring(tree, encoding='unicode', method='text')


class SanitizerStripTagsDecorator:
    def __init__(self, sanitizer):
        self.sanitizer = sanitizer

    # BEGIN
    def sanitize(self, text):
        text_without_tags = strip_tags(text)
        return self.sanitizer.sanitize(text_without_tags)
    # END
