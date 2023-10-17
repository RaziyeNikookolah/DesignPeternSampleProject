from filter import Filter


class HighContrastFilter(Filter):
    def apply(self, file_name):
        print(file_name, "Applying High Contrast Filter")
