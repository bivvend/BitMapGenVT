import sys
import os
import time #used for profiling
from PIL import Image, ImageDraw

# EXAMPLE COMMAND python bitmap_skew.py input.bmp 1 False
#    Expected parameters
#    -------------------
#    input bitmap
#    pixel offset per line
#    Show output positions True/False

def generate_image(bitmap, pixel_offset_per_line, debug):
    '''Generate image function'''
    print("X offset of each line: {} pixel(s)".format(str(pixel_offset_per_line)))
    
    if os.path.isfile(bitmap is not True):
        print("Input file not found")
        return False

    im = Image.open(bitmap)
    pixels_array_input = im.load()
    size_x, size_y = im.size 
    print("Input image size: {} , {}".format(str(size_x), str(size_y)))

    im_out = Image.new("1", (size_x + size_y*pixel_offset_per_line, size_y), 1)
    pixels_array_output = im_out.load()

    for y in range(0, size_y):
        for x in range(0, size_x):
            try:
                pixels_array_output[x + (size_y - y) * pixel_offset_per_line, y] = pixels_array_input[x, y]
                if debug:
                    print("{},{} => {},{}".format(str(x), str(y), str(x + (size_y - y) * pixel_offset_per_line), str(y))) 
            except:
                pass #ignore attempts to write outside of array

    im_out.save("output.bmp")
    size_x, size_y = im_out.size
    print("Output image size: {} , {}".format(str(size_x), str(size_y)))

    return True

if __name__ == "__main__":
    try:
        if sys.argv[1] == "?":
            print("Expected parameters")
            print("-------------------")
            print("input bitmap")
            print("pixel offset per line")
            print("Show pixel output True/False")
            exit()

        input_bitmap = sys.argv[1]
        input_pixel_offset_per_line = int(sys.argv[2])
        input_debug = bool(sys.argv[3] == "True")

    except Exception as e:
        print("Input parameters incorrect. Terminating.")        
        exit()
    print("Starting generation...")
    time1 = time.time()
    if generate_image(input_bitmap, input_pixel_offset_per_line, input_debug):
        print("Generation successful.")
    else:
        print("Generation failed.")
    time2 = time.time()
    run_time = time2-time1
    print("Run time {} seconds".format(run_time))
    