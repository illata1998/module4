import os
from errors.NotExistsError import NotExistsError
from errors.NotReadableError import NotReadableError


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        file_path = self.file_path

        # BEGIN
        if not os.path.exists(file_path):
            raise NotExistsError(f"'{file_path}' does not exist")

        if not os.access(file_path, os.R_OK):
            raise NotReadableError(f"'{file_path}' does not read")
        # END
        with open(file_path, 'r') as file:
            return file.read()
