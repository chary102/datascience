def mat_mul(A,B): 
    ra,ca=len(A),len(A[0])
    rb,cb=len(B),len(B[0])

    if ca!=rb:          
        print("error")


    r=[[0 for _ in range(cb)] for _ in range(ra)]

    for i in range(ra):
        print(i)
        for j in range(cb):
            print(j)
            for k in range(ca):
                print(k)
                r[i][j]+=A[i][k] * B[k][j]
                print(r[i][j])
    return r

A=[[1,2],[3,4]]
B=[[5,6],[7,8]]

print(mat_mul(A,B))




'''def mat_mul(A, B):
    ra,ca = len(A), len(A[0])
    rb,cb = len(B), len(B[0])
    
    if ra != rb or ca != cb:
        print("error")
    
  
    r = [[0 for _ in range(ca)] for _ in range(ra)]
    print(r)

    for i in range(ra):
        print(i)
        for j in range(ca):
            print(j)
            r[i][j] = A[i][j] + B[i][j]
            print(r[i][j])
    
    return r

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(mat_mul(A, B))'''






