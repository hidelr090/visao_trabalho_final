import numpy as np
from skimage.io import imsave
from skimage.io import imread_collection, imread
import os

from skimage.color import rgb2gray


def hidel_glcm(image, angle=0, distance=1, normalize=False):

	lines, columns = image.shape

	glcm_matrix = []
	glcm_lines=0
	glcm_columns=0
	
	if(angle==0):
		
		for i in range(lines):
			for j in range(columns-distance):
				reference = int(image[i][j])
				neighbour = int(image[i][j+distance])
				if(reference > glcm_lines):
					glcm_lines = reference
				if(neighbour > glcm_columns):
					glcm_columns = neighbour
		#print(glcm_lines, glcm_columns)            
		for i in range(glcm_lines+1):
			lista = []
			for j in range(glcm_columns+1):
				lista.append(0)
			glcm_matrix.append(lista)
		
						
		for i in range(lines):
			for j in range(columns-distance):
				reference = int(image[i][j])
				neighbour = int(image[i][j+distance])
				#print(reference)
				#print(neighbour)
				glcm_matrix[reference][neighbour]+=1
		if normalize == True:
			return (glcm_matrix - np.min(glcm_matrix))/np.ptp(glcm_matrix)
		return glcm_matrix

	'''if(angle=='west'):
		for i in range(lines):
			for j in range(distance, columns, 1):
				reference = int(image[i][j])
				neighbour = int(image[i][j-distance])
				if(reference > glcm_lines):
					glcm_lines = reference
				if(neighbour > glcm_columns):
					glcm_columns = neighbour
		#print(glcm_lines, glcm_columns)            
		for i in range(glcm_lines+1):
			lista = []
			for j in range(glcm_columns+1):
				lista.append(0)
			glcm_matrix.append(lista)
		
						
		for i in range(lines):
			for j in range(distance, columns, 1):
				reference = int(image[i][j])
				neighbour = int(image[i][j-distance])
				#print(reference)
				#print(neighbour)
				glcm_matrix[reference][neighbour]+=1
		if normalize == True:
			return (glcm_matrix - np.min(glcm_matrix))/np.ptp(glcm_matrix)
		return glcm_matrix'''

	if(angle == 90):
		for i in range(distance, lines, 1):
			for j in range(columns):
				reference = int(image[i][j])
				neighbour = int(image[i-distance][j])
				if(reference > glcm_lines):
					glcm_lines = reference
				if(neighbour > glcm_columns):
					glcm_columns = neighbour
		#print(glcm_lines, glcm_columns)            
		
		for i in range(glcm_lines+1):
			lista = []
			for j in range(glcm_columns+1):
				lista.append(0)
			glcm_matrix.append(lista)
		
						
		for i in range(distance, lines, 1):
			for j in range(columns):
				reference = int(image[i][j])
				neighbour = int(image[i-distance][j])
				#print(reference)
				#print(neighbour)
				glcm_matrix[reference][neighbour]+=1
		if normalize == True:
			return (glcm_matrix - np.min(glcm_matrix))/np.ptp(glcm_matrix)
		return glcm_matrix

	'''if(angle == 'south'):
		for i in range(lines-distance):
			for j in range(columns):
				reference = int(image[i][j])
				neighbour = int(image[i+distance][j])
				if(reference > glcm_lines):
					glcm_lines = reference
				if(neighbour > glcm_columns):
					glcm_columns = neighbour
		#print(glcm_lines, glcm_columns)            
		
		for i in range(glcm_lines+1):
			lista = []
			for j in range(glcm_columns+1):
				lista.append(0)
			glcm_matrix.append(lista)
		
						
		for i in range(lines-distance):
			for j in range(columns):
				reference = int(image[i][j])
				neighbour = int(image[i+distance][j])
				#print(reference)
				#print(neighbour)
				glcm_matrix[reference][neighbour]+=1
		if normalize == True:
			return (glcm_matrix - np.min(glcm_matrix))/np.ptp(glcm_matrix)
		return glcm_matrix'''
	
	if(angle == 45):
		for i in range(distance, lines, 1):
			for j in range(distance, columns, 1):
				reference = int(image[i][j])
				neighbour = int(image[i-distance][j-distance])
				if(reference > glcm_lines):
					glcm_lines = reference
				if(neighbour > glcm_columns):
					glcm_columns = neighbour
		#print(glcm_lines, glcm_columns)            
		
		for i in range(glcm_lines+1):
			lista = []
			for j in range(glcm_columns+1):
				lista.append(0)
			glcm_matrix.append(lista)
		
						
		for i in range(distance, lines, 1):
			for j in range(distance, columns, 1):
				reference = int(image[i][j])
				neighbour = int(image[i-distance][j-distance])
				#print(reference)
				#print(neighbour)
				glcm_matrix[reference][neighbour]+=1
		if normalize == True:
			return (glcm_matrix - np.min(glcm_matrix))/np.ptp(glcm_matrix)
		return glcm_matrix
	
	if(angle == 135):
		for i in range(distance, lines, 1):
			for j in range(columns-distance):
				reference = int(image[i][j])
				neighbour = int(image[i-distance][j+distance])
				if(reference > glcm_lines):
					glcm_lines = reference
				if(neighbour > glcm_columns):
					glcm_columns = neighbour
		#print(glcm_lines, glcm_columns)            
		
		for i in range(glcm_lines+1):
			lista = []
			for j in range(glcm_columns+1):
				lista.append(0)
			glcm_matrix.append(lista)
		
						
		for i in range(distance, lines, 1):
			for j in range(columns-distance):
				reference = int(image[i][j])
				neighbour = int(image[i-distance][j+distance])
				#print(reference)
				#print(neighbour)
				glcm_matrix[reference][neighbour]+=1
		if normalize == True:
			return (glcm_matrix - np.min(glcm_matrix))/np.ptp(glcm_matrix)
		return glcm_matrix
	
	'''if(angle == 'southeast'):
		for i in range(lines-distance):
			for j in range(columns-distance):
				reference = int(image[i][j])
				neighbour = int(image[i+distance][j+distance])
				if(reference > glcm_lines):
					glcm_lines = reference
				if(neighbour > glcm_columns):
					glcm_columns = neighbour
		#print(glcm_lines, glcm_columns)            
		
		for i in range(glcm_lines+1):
			lista = []
			for j in range(glcm_columns+1):
				lista.append(0)
			glcm_matrix.append(lista)
		
						
		for i in range(lines-distance):
			for j in range(columns-distance):
				reference = int(image[i][j])
				neighbour = int(image[i+distance][j+distance])
				#print(reference)
				#print(neighbour)
				glcm_matrix[reference][neighbour]+=1
		if normalize == True:
			return (glcm_matrix - np.min(glcm_matrix))/np.ptp(glcm_matrix)
		return glcm_matrix'''
	
	'''if(angle == 'southwest'):
		for i in range(distance, lines, 1):
			for j in range(distance, columns, 1):
				reference = int(image[i][j])
				neighbour = int(image[i-distance][j-distance])
				if(reference > glcm_lines):
					glcm_lines = reference
				if(neighbour > glcm_columns):
					glcm_columns = neighbour
		#print(glcm_lines, glcm_columns)            
		
		for i in range(glcm_lines+1):
			lista = []
			for j in range(glcm_columns+1):
				lista.append(0)
			glcm_matrix.append(lista)
		
						
		for i in range(distance, lines, 1):
			for j in range(distance, columns, 1):
				reference = int(image[i][j])
				neighbour = int(image[i-distance][j-distance])
				#print(reference)
				#print(neighbour)
				glcm_matrix[reference][neighbour]+=1

		if normalize == True:
			return (glcm_matrix - np.min(glcm_matrix))/np.ptp(glcm_matrix)
		return glcm_matrix'''


def gray_255_scale(image):  
    arr = np.zeros(image.shape)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = int(round(image[i,j] * 255))
    return arr