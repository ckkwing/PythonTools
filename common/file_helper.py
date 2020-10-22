import os


class FileHelper:
    @staticmethod
    def get_file_extension(file_path):
        return os.path.splitext(file_path)[1]

    @staticmethod
    def is_suffix(file, *suffix_name):
        array = map(file.lower().endswith, suffix_name)
        if True in array:
            return True
        else:
            return False
