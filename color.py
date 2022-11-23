import numpy as np
import skimage
import colorsys


def cmyk(r, g, b):
    bgr = np.array([b, g, r]) / 255.0
    with np.errstate(invalid='ignore', divide='ignore'):
        k = 1.0 - np.max(bgr)
        c = (1 - bgr[..., 2] - k) / (1 - k)
        m = (1 - bgr[..., 1] - k) / (1 - k)
        y = (1 - bgr[..., 0] - k) / (1 - k)
    return np.array((c, m, y, k) * 255).astype(np.int)


def lch(rgb):
    ill = ['D50', 'D65', 'D75']
    return [skimage.color.lab2lch(skimage.color.rgb2lab(rgb, illuminant=i)) for i in ill]


class Color:
    def __init__(self, rgb):
        self.rgb = rgb
        self.d50, self.d65, self.d75 = lch(rgb)
        self.r = self.rgb[0]
        self.g = self.rgb[1]
        self.b = self.rgb[2]
        self.hex = '#%02x%02x%02x' % (self.r, self.g, self.b)
        self.hsv = colorsys.rgb_to_hsv(self.r, self.g, self.b)
        self.hlv = colorsys.rgb_to_hls(self.r, self.g, self.b)
        self.cmyk = cmyk(self.r, self.g, self.b)
