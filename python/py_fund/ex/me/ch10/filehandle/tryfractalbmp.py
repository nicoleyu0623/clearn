'''creates a mandelbrot fract and writes it as a os independent bmp file'''

from imagewriter.fractal import mandelbrot
from imagewriter.bmp import write_grayscale
from imagewriter.bmp import dimensions


def test_create_fractal_pixels(width):
    height = int(width / 1.75)
    pixels = mandelbrot(width,height)
    print(type(pixels))
    print("pixels has length:",len(pixels))
    return pixels


def test_write_to_bmp_file(fname, pixels):
    write_grayscale(fname, pixels)
    print('wrote to file', fname)

def test_print_image_dimensions(fname):
    w,h = dimensions(fname)
    print("image dimensions: width: {}, height: {}".format(w,h))


def main():
    fn = 'mandel.bmp'
    img_width = 448
    pixels = test_create_fractal_pixels(img_width)
    test_write_to_bmp_file(fn, pixels)
    test_print_image_dimensions(fn)


if __name__ == '__main__':
    main()




