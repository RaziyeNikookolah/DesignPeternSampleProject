from compressor import Compressor


class JpegCompressor(Compressor):
    def compress(self, file_name):
        print(file_name, "Applying JPEG compressor")
