import skimage
import color

rgb = skimage.io.imread("png/red.png")[0][0]
color.Color(rgb)
