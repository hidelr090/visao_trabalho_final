
def homogeneity(image):
    lines, columns = image.shape
    soma = 0
    for i in range(lines):
        for j in range(columns):
            soma+=(image[i][j]/(1+((i-j)**2)))

    return soma


