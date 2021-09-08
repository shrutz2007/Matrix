def matrix(m,n):
    output=[]
    for i in range(m):
        row=[]
        for j in range(n):
            element=int(input(f"Enter the element output[{i}][{j}]: "))
            row.append(element)
        output.append(row)
    return output
def sum(A,B):
    output1=[]
    for i in range(len(A)):  #num of rows
        row=[]
        for j in range(len(A[0])):  #num of Cols
            row.append(A[i][j]+B[i][j])
        output1.append(row)
    return output1
m=int(input("Enter the value of m :"))
n=int(input("Enter the value of m :"))
print("Enter the Matrix A")
A=matrix(m,n)
print(A)
print("Enter the Matrix B")
B=matrix(m,n)
print(B)
s=sum(A,B)
print(s)