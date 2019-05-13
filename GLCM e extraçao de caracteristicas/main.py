import GLCM as glcm
import features as ft
import skimage.io as skm
from skimage.color import rgb2gray

image = skm.imread('/home/hidel/Documents/Git/visao_trabalho_final/picos_nitido.jpg')
image = rgb2gray(image)

matrix = glcm.hidel_glcm(image)

print(ft.homogeneity(image))
print(ft.variancia(image))