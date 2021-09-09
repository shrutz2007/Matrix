def trans(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i]=matrix[i][j]
            
x=[[12,4],[6,8],[3,10]]
result=[[0,0,0],[0,0,0]]
trans(x)
for r in result:
    print(r)