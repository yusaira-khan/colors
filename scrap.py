import numpy
import skimage

rgb = numpy.array([[0, 0, 255]])
lab = skimage.color.rgb2lab(rgb, illuminant='D50')
print(lab)
