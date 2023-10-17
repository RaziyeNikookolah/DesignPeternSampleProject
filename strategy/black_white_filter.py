from filter import Filter


class BlackAndWhiteFilter(Filter):
    def apply(self, file_name):
        print(file_name, "Applying Black and White Filter")
