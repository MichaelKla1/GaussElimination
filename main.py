matrix = [[0,2,3,4],[5,0,7,8],[9,10,0,12],[13,14,15,0]]
resvec = [17,18,19,20]
def solutionOfMatrixByGaussElimination(matrix,resvec):
    """
    Return the solution vector of square matrix that has result vector resvec
    :param matrix: matrix
    :param resvec: result vector
    :return: solution vector of square matrix that has result vector resvec
    """
    rowscount = len(matrix)
    if rowscount < 1:
        return [] #empty matrix
    colscount = len(matrix[0])
    i=0
    while i<rowscount:
        colscount = len(matrix[i])
        if colscount!=rowscount:
            return [] #matrix is not squared
        rowdivider=matrix[i][i]
        if rowdivider == 0:
            s = i + 1
            flag = 0
            while s < rowscount:
                if matrix[s][i]!=0:
                    #swap lines
                    temp = matrix[s].copy()
                    matrix[s]=matrix[i].copy()
                    matrix[i]=temp
                    flag=1
                    rowdivider = matrix[i][i]
                    temp = resvec[s]
                    resvec[s] = resvec[i]
                    resvec[i] = temp
                    break
                s+=1
            if flag == 0:
                return []  # same lines in matrix
        k=i
        while k<colscount:
            matrix[i][k]=matrix[i][k]/rowdivider
            k+=1
        resvec[i] = resvec[i]/rowdivider
        k=i+1
        while k<rowscount:

            n = matrix[k][i]
            j=i
            while j<colscount:
                matrix[k][j] = matrix[k][j] - n*matrix[i][j]
                j+=1
            resvec[k] = resvec[k] - n*resvec[i]
            k += 1
        i+=1
    #rotate matrix 180 degree
    i1 = 0
    i2 = colscount - 1
    i3 = 0
    while i3 < colscount:  # rotate cols
        i1=0
        i2 = colscount - 1
        while i1 < i2:
            temp = matrix[i3][i1]
            matrix[i3][i1] = matrix[i3][i2]
            matrix[i3][i2] = temp
            i1 += 1
            i2 -= 1
        i3 += 1
    i1=0
    i2=colscount-1
    while i1<i2: #rotate rows
        temp = matrix[i1].copy()
        matrix[i1] = matrix[i2].copy()
        matrix[i2] = temp
        temp = resvec[i1]
        resvec[i1] = resvec[i2]
        resvec[i2] = temp
        i1+=1
        i2-=1
    i = 0
    while i < rowscount:
        colscount = len(matrix[i])
        if colscount != rowscount:
            return []  # matrix is not squared
        rowdivider = matrix[i][i]
        if rowdivider == 0:
            s = i + 1
            flag = 0
            while s < rowscount:
                if matrix[s][i] != 0:
                    # swap lines
                    temp = matrix[s].copy()
                    matrix[s] = matrix[i].copy()
                    matrix[i] = temp
                    flag = 1
                    rowdivider = matrix[i][i]
                    break
                s += 1
            if flag == 0:
                return []  # same lines in matrix
        k = i
        while k < colscount:
            matrix[i][k] = matrix[i][k] / rowdivider
            k += 1
        resvec[i] = resvec[i] / rowdivider
        k = i + 1
        while k < rowscount:

            n = matrix[k][i]
            j = i
            while j < colscount:
                matrix[k][j] = matrix[k][j] - n * matrix[i][j]
                j += 1
            resvec[k] = resvec[k] - n*resvec[i]
            k += 1
        i += 1
    #rotate resvec
    i1 = 0
    i2 = colscount - 1
    while i1 < i2:  # rotate rows
        temp = resvec[i1]
        resvec[i1] = resvec[i2]
        resvec[i2] = temp
        i1 += 1
        i2 -= 1
    return resvec





print(solutionOfMatrixByGaussElimination(matrix,resvec))