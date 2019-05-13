import numpy as np

def homogeneity(image):
    lines, columns = image.shape
    soma = 0
    for i in range(lines):
        for j in range(columns):
            soma+=(image[i][j]/(1+((i-j)**2)))

    return soma

def variancia(image):
	i_sum = 0
	j_sum = 0

	mean = np.mean(image)

	for i in range(image.shape[0]):
		j_sum = 0
		for j in range(image.shape[1]):
			j_sum += ((1-mean)**2)*image[i,j]
		
		i_sum+=j_sum
	
	return i_sum