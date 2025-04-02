with open("example.txt",'r') as st:
    a=st.read()
    ra=a[::-1]
with open("reversed_example.txt",'w') as rst:
    b=rst.write(ra)






with open("example.txt",'r') as st:
    a=st.read()
    ra=''.join(word[::-1] for word in a.split(' '))
with open("reversed_example.txt",'w') as rst:
    b=rst.write(ra)
