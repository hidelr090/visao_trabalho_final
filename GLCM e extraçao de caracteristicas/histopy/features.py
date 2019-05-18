import numpy as np

def homogeneity(image):
	soma = 0
	for i in range(len(image)):
		for j in range(len(image[i])):
			soma+=(image[i][j]/(1+((i-j)**2)))

	return soma

def variance(image):
	i_sum = 0
	j_sum = 0

	mean = np.mean(image)

	for i in range(len(image)):
		j_sum = 0
		for j in range(len(image[i])):
			j_sum += ((1-mean)**2)*image[i,j]
		i_sum+=j_sum

	return i_sum
	
def uniformity(image):
	sum_index_values = 0
	for i in image:
		for j in i:
			sum_index_values += j**2
	return sum_index_values

def entropy(image):
	sum_index_values = 0
	for i in image:
		for j in i:
			if j > 0:
				sum_index_values += j*np.log10(j)
	return -(sum_index_values)

def correlation(image):
	sum_index_values = 0

	for i in range(len(image)):
		for j in range(len(image[i])):
			if image[i,j] != 0:
				sum_index_values += (i - np.mean(image[i])) * (j - np.mean(image[:,j])) * image[i,j]/(np.std(image[i])*np.std(image[:,j]))
	return sum_index_values

def contrast(image):
	sum_index_values = 0
	
	for i in range(len(image)):
		for j in range(len(image[i])):
			sum_index_values += ((i - j) ** 2) * image[i,j]
	return sum_index_values