# function num1
def sayhi(user_name):
    print("hello"+ user_name)

# function 2
def cal(num1,num2):
    sum=int(num1)+int(num2)
    sub=int (num1)-int (num2)
    multi=int(num1)*int (num2)
    div=int(num1)/int(num2)
    print("Sum of those numbers are: "+ str(sum))
    print("Sub of those number is: "+ str(sub))
    print("multi of those number is: "+ str(multi))
    print("div of those number is: "+ str(div))

# function 3
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3


    

print(max_num(400,50,600))
Name= input("Enter your name: ")
sayhi(Name)
num_1= input("Enter a number: ")
num_2= input("Enter another number: ")
cal(num_1,num_2)
is_female=True 

if is_female:
    print("you are a female")
else:
    print("you are not a female")
