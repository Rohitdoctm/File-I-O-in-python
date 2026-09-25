with open("sample.txt","r") as f:
    data=f.read()
    print(data)
    print(type(data))
newdata=""
with open("sample.txt","r") as f:
    data=f.read()
    newdata=data.replace("different","various")
with open("sample.txt","w") as f:
    f.write(newdata)  
with open("sample.txt","r") as f:
    print(f.read())

