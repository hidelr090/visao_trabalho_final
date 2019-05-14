from skimage.color import rgb2gray
from skimage.io import imread
from histopy.GLCM import hidel_glcm


class HistoImage(object):
	"""docstring for NewImage"""
	def __init__(self, image):

		if image.split('.')[1].upper() not in ['JPG', 'PNG', 'JPEG']:
			raise Exception('This module only works with JPG or PNG images.')

		self.__name_image = image
		self.image = imread(image)
		self.__type = 'RGB' if len(self.image.shape) == 3 else 'GRAY'
		

	def __repr__(self):
		return "<histopy image: '{}', type: {}>".format(
								self.__name_image, self.__type)

	def to_gray(self):
		if self.__type == 'RGB':
			self.image = rgb2gray(self.image)
			self.__type = 'RGB' if len(self.image.shape) == 3 else 'GRAY'
		else:	
			raise Exception('This image is already grayed out.')

	def glcm(self, angle='east', distance=1, normalize=False):
		if self.__type == 'RGB':
			raise Exception('The image must be grayed out to apply the GLCM, for now.')
		else:
			print("Hidel function is running for {} angle, distance {} and normalize {}...".format(angle, distance, normalize))
			return hidel_glcm(self.image, angle='east', distance=distance, normalize=normalize)


# ni = HistoImage('placa.jpeg')