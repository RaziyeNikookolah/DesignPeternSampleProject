class ImageStorage:

    def store(self, file_name, compressor, filter):
        compressor.compress(file_name)
        filter.apply(file_name)
