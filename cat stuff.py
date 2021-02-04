fo=open('myfile.txt' , 'r')
myletter=fo.read()
print(myletter)
fo.close()


import os.path
if os.path.isfile("myfile.txt"):
    print("yo file exists")
else:
    print("yo file got killed")