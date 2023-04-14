import re


class RegularExpressionComparator:
    @staticmethod
    def equals_source_and_regular_ex(source, regular_ex):
        pattern = re.compile(regular_ex)
        return pattern.fullmatch(source) is not None
