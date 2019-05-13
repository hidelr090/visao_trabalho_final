
def hidel_glcm(image, angle='east', distance=1):

    lines, columns = image.shape

    glcm_matrix = []
    glcm_lines=0
    glcm_columns=0
    
    if(angle=='east'):
        
        for i in range(lines):
            for j in range(columns-distance):
                reference = int(image[i][j])
                neighbour = int(image[i][j+distance])
                if(reference > glcm_lines):
                    glcm_lines = reference
                if(neighbour > glcm_columns):
                    glcm_columns = neighbour
        print(glcm_lines, glcm_columns)            
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
    
        return glcm_matrix

    if(angle=='west'):
        for i in range(lines):
            for j in range(distance, columns, 1):
                reference = int(image[i][j])
                neighbour = int(image[i][j-distance])
                if(reference > glcm_lines):
                    glcm_lines = reference
                if(neighbour > glcm_columns):
                    glcm_columns = neighbour
        print(glcm_lines, glcm_columns)            
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
        
        return glcm_matrix

    if(angle == 'north'):
        for i in range(distance, lines, 1):
            for j in range(columns):
                reference = int(image[i][j])
                neighbour = int(image[i-distance][j])
                if(reference > glcm_lines):
                    glcm_lines = reference
                if(neighbour > glcm_columns):
                    glcm_columns = neighbour
        print(glcm_lines, glcm_columns)            
        
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
        
        return glcm_matrix

    if(angle == 'south'):
        for i in range(lines-distance):
            for j in range(columns):
                reference = int(image[i][j])
                neighbour = int(image[i+distance][j])
                if(reference > glcm_lines):
                    glcm_lines = reference
                if(neighbour > glcm_columns):
                    glcm_columns = neighbour
        print(glcm_lines, glcm_columns)            
        
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
        
        return glcm_matrix
    
    if(angle == 'northwest'):
        for i in range(distance, lines, 1):
            for j in range(distance, columns, 1):
                reference = int(image[i][j])
                neighbour = int(image[i-distance][j-distance])
                if(reference > glcm_lines):
                    glcm_lines = reference
                if(neighbour > glcm_columns):
                    glcm_columns = neighbour
        print(glcm_lines, glcm_columns)            
        
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
        
        return glcm_matrix
    
    if(angle == 'northeast'):
        for i in range(distance, lines, 1):
            for j in range(columns-distance):
                reference = int(image[i][j])
                neighbour = int(image[i-distance][j+distance])
                if(reference > glcm_lines):
                    glcm_lines = reference
                if(neighbour > glcm_columns):
                    glcm_columns = neighbour
        print(glcm_lines, glcm_columns)            
        
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
        
        return glcm_matrix
    
    if(angle == 'southeast'):
        for i in range(lines-distance):
            for j in range(columns-distance):
                reference = int(image[i][j])
                neighbour = int(image[i+distance][j+distance])
                if(reference > glcm_lines):
                    glcm_lines = reference
                if(neighbour > glcm_columns):
                    glcm_columns = neighbour
        print(glcm_lines, glcm_columns)            
        
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
        
        return glcm_matrix
    
    if(angle == 'southwest'):
        for i in range(distance, lines, 1):
            for j in range(distance, columns, 1):
                reference = int(image[i][j])
                neighbour = int(image[i-distance][j-distance])
                if(reference > glcm_lines):
                    glcm_lines = reference
                if(neighbour > glcm_columns):
                    glcm_columns = neighbour
        print(glcm_lines, glcm_columns)            
        
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
        
        return glcm_matrix

    



