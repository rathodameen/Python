
#task 1
take list of numbers 
return True only if the first and last elemetn are even numbers
else return False
list=[2,3,7,9,4]
for i in range(0,len(list)):
    if list[i] and list[i] %2==0:
        print(True)
    else:
        print(False)
#task 2

# num=[2,3,4,5,6,5,6,7,8]
# for n in range(0,len(num)):


#task write a function that replecates the code functionality



#task__
num=[2,4,2,4,6,7,8,75,3,5,2]
unq_list=[]
for i in range(0,len(num)):
    if num.count(num[i])==1:
        unq_list.append(num[i])
print(unq_list)


#task_
num=[2,4,6,3,7,33,64,5,31,37,61,95,57]
new=[]
for i in range(0,len(num)):
    n=num[i] #1
    fact=0 # to store the factors
    for j in range(1,n+1):
        if n%j==0:
            fact+=1
    if fact>2:
        new.append(n)
print(new)
