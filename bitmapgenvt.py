import sys
import time #used for profiling
from PIL import Image, ImageDraw

def generate_image(size_x, size_y, num_lines_per_block, line_length_pixels, line_y_pitch_pixels, pixel_offset_per_line):
    '''Generate image function'''
    print("Image size set as : {} , {}".format(str(size_x), str(size_y)))
    print("{} lines per block".format(str(num_lines_per_block)))
    print("Line length {} pixels".format(str(line_length_pixels)))
    print("Y pitch of repeats: {} pixel(s)".format(str(line_y_pitch_pixels)))
    print("X offset of each line: {} pixel(s)".format(str(pixel_offset_per_line)))
    im = Image.new("1", (size_x, size_y), 1)
    pixels_array = im.load()
    start_x = 0
    start_y = size_y-1

    current_x = start_x
    current_y = start_y
    
    while current_y >= 0:
        for line in range(0, num_lines_per_block):
            for pixel_x in range(0, line_length_pixels):
                try:
                    pixels_array[current_x + pixel_x, current_y] = 0
                except:
                    pass
            current_y -= 1
            current_x += pixel_offset_per_line
        current_y -= line_y_pitch_pixels - num_lines_per_block
        current_x = 0


    im.save("output.bmp")

    return True

if __name__ == "__main__":
    try:
        input_size_x = int(sys.argv[1])
        input_size_y = int(sys.argv[2])
        input_num_lines_per_block  = int(sys.argv[3])
        input_line_length_pixels = int(sys.argv[4])
        input_line_y_pitch_pixels = int(sys.argv[5])
        input_pixel_offset_per_line = int(sys.argv[6])
        
        bad_param = False
        if input_size_x < 1:
            bad_param = True
        if input_size_y < 1:
            bad_param = True
        if input_line_y_pitch_pixels < 0:
            bad_param = True
        if bad_param:
            print("Negative or bad parameters sent")
            exit()
    except Exception as e:
        print("Input parameters incorrect. Terminating.")
        exit()
    print("Starting generation...")
    time1 = time.time()
    if generate_image(input_size_x, input_size_y, input_num_lines_per_block,
        input_line_length_pixels, input_line_y_pitch_pixels, input_pixel_offset_per_line):
        print("Generation successful.")
    else:
        print("Generation failed.")
    time2 = time.time()
    run_time = time2-time1
    print("Run time {}".format(run_time))
    