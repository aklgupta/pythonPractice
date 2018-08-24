"""Q19

Write a python program to generate thumbnails for all Images in a directory.
1) Input an input_path and an output_path
2) Input thumbnail max resolution (width x height)
3) Write thumbnails to the output_path
4) All thumbnails should be <= the max resolution
5) All thumbnails should be in JPG format, with 75% quality
6) Input path may contain different types images files (eg. jpg, png, tiff, bmp). Try to cover as many as possible
7) The directory structure of the output_path should be identical to input_path
"""

from PIL import Image
import os

input_path = raw_input("Input Dir:")
output_path = raw_input("Output Dir:")

width = input("Width in px:")
height = input("Height in px:")

for root, dirs, files in os.walk(input_path):
  out_root = root.replace(input_path, output_path)
  if not os.path.exists(out_root):
    os.mkdir(out_root)
  for f in files:
    img = os.path.join(root, f)
    out = os.path.join(out_root, f) + ".jpg"
    print "Image:", img
    try:
      im = Image.open(os.path.join(root, f))
    except Exception, e:
      print "Unable to convert", img, "\nPlease check file format"
    im.thumbnail((width, height ))
    print "New Size:", im.size
    im.save(out, "JPEG", quality=75)

