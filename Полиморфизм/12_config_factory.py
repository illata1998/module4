import os
from parsers.json_parser import JSONParser
from parsers.yaml_parser import YAMLParser
from src.config_klass import Config


PARSERS = {
    '.yaml': YAMLParser,
    '.yml': YAMLParser,
    '.json': JSONParser,
}


# BEGIN
class ConfigFactory:
    def factory(file_path):
        type = os.path.splitext(file_path)[1]
        parser = PARSERS[type]()

        raw_data = open(file_path).read()
        data = parser.parse(raw_data)

        return Config(data)
# END
