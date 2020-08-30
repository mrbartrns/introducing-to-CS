# brute force
def rank(matrix: list):
    '''
    input: 2 by 2 matrix (x, y) ex) [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]
    return: ranking
    '''
    res = [0] * len(matrix)
    ranking = []
    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            if matrix[i][0] > matrix[j][0] and matrix[i][1] > matrix[j][1]:
                res[i] += 1
            elif matrix[i][0] < matrix[j][0] and matrix[i][1] < matrix[j][1]:
                res[j] += 1
    return res

print(rank([[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]))