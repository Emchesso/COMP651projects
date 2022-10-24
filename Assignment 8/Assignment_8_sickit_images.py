# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 15:52:26 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import matplotlib.pyplot as plt
import skimage as sk
import numpy as np

img = sk.data.cell()
v_min, v_max = np.percentile(img, (3.25, 96.75))
better_contrast = sk.exposure.rescale_intensity(img, in_range=(v_min, v_max))
plt.imshow(better_contrast)
sk.io.imsave("cell_better_contrast.jpg", better_contrast)
# sharper_contrast = sk.exposure.rescale_intensity(img)
# plt.imshow(sharper_contrast)


