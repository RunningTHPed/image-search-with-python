import os
import numpy as np
import imageio

# specify the directory containing the subdirectories with .jpg images
root_dir = 'static/feature'

# loop through all subdirectories
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        # check if the file has a .jpg extension
        if file.endswith(".jpg"):
            # read the .jpg image using imageio
            img = imageio.imread(os.path.join(subdir, file))
            # convert the image to numpy array
            img_np = np.array(img)
            # save the numpy array as .npy file
            np.save(os.path.join(subdir, file[:-4] + '.npy'), img_np)
