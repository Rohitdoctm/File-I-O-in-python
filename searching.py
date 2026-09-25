def check():
    with open("sample.txt","r") as f:
        data=f.read()
        word=input("Enter the word to be search in sample.txt file ")
        if(data.find(word)!=-1):
            print("The word is present:")
            return
        else:
            print("The word is not present")
check()            