from File import File
from errors.FileError import FileError


# BEGIN
def read_files(file_list):
    data = []
    for file_path in file_list:
        file = File(file_path)
        try:
            data.append(file.read())
        # перехватываем базовую ошибку библиотеки
        except FileError:
            data.append(None)
    return data
# END
