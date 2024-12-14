from FileInfo import FileInfo


# BEGIN
class SmartFileInfo(FileInfo):
    def get_size(self, unit='b'):
        size = super().get_size()
        if unit == 'b':
            return size
        elif unit == 'kb':
            return size / 1024
        else:
            raise ValueError(f'Unknown unit name: {unit}')
# END
