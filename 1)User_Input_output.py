def matrix(m,n):
    output=[]
    for i in range(m):
        row=[]
        for j in range(n):
            element=int(input(f"Enter the element output[{i}][{j}]: "))
            row.append(element)
        output.append(row)
            
    return output

m=int(input("Enter the value of m :"))
n=int(input("Enter the value of m :"))
print("Enter the Matrix A")
A=matrix(m,n)
print(A)
print("Enter the Matrix B")
B=matrix(m,n)
print(B)