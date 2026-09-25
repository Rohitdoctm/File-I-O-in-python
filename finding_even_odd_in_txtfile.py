def count_Even():
    count=0
    with open("number.txt","r") as f:
        data=f.read()
        num=""
        for val in range(len(data)):
            if(data[val]==","):
                if(int(num)%2==0):
                    count=count+1
                    num=""
            else:
                num=num+data[val]        
    return count
ans=count_Even()
print("The number of even digit present in the number.txt file is=",ans)
# to find the no of odd digits in number.txt file just change the if condition %2!=0