
class StringUtility:
    @staticmethod
    def __check_validion(source):
        if not isinstance(source, str):
            raise ValueError("Argument is not a type of string")

    @staticmethod
    def is_null_or_empty(source):
        StringUtility.__check_validion(source)
        if str is None:
            return True
        return 0 == len(source) or source.isspace()

