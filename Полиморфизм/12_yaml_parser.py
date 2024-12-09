import yaml


class YAMLParser:
# BEGIN
    def parse(self, data):
        return yaml.safe_load(data)
# END
