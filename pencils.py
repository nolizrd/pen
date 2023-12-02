import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.filters import threshold_otsu
from skimage.morphology import binary_closing
import numpy as np
sum_pen = 0

for i in range(1, 13):
    image = plt.imread(f"img ({i}).jpg").mean(2)
    binary = image < threshold_otsu(image) * 1.1
    labeled = label(binary_closing(binary, np.ones((20, 20), np.uint8)))
    sum_pen += sum((region.major_axis_length > 2965) and(region.minor_axis_length>130) for region in regionprops(labeled))
print(sum_pen)
