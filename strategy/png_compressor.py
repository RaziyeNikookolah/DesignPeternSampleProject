from compressor import Compressor


class PngCompressor(Compressor):
    def compress(self, file_name):
        print(file_name, "Applying PNG compressor")
