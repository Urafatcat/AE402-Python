file=open("fat cat.jpg","rb")
img=file.read()
file.close()

file=open("veryfatcat.jpg","wb")
file.write(img)
file.close()


