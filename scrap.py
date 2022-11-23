import numpy as np
import skimage

rgb = skimage.io.imread("png/red.png")[0][0]
print(rgb)
rgbarr = np.array(rgb)
d50r = skimage.color.rgb2lab(rgb, illuminant='D50')
d65r = skimage.color.rgb2lab(rgb, illuminant='D65')
d75r = skimage.color.rgb2lab(rgb, illuminant='D75')
print(d50r, d65r, d75r)
