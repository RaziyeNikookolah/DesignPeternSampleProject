from image_storage import ImageStorage
from jpeg_compressor import JpegCompressor
from black_white_filter import BlackAndWhiteFilter
from png_compressor import PngCompressor
from high_contrast import HighContrastFilter
if __name__ == "__main__":
    img_storage = ImageStorage()
    img_storage.store("a", JpegCompressor(), HighContrastFilter())

    img_storage.store("b", PngCompressor(), BlackAndWhiteFilter())
