import sys


sys.set_int_max_str_digits(1_000_000)


color_range, img_height, img_width, img_colors, n_actions = 256, 210, 160, 3, 9
print(color_range ** (img_height * img_width * img_colors) * n_actions)
