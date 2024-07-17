#List
values=[1,4,55,"SANKETking"]
print(values[-1])


#Tuple

mytuple1=(1,2,3)
mytuple2=mytuple1
print(mytuple2)




#Dictionary
dict={}

dict["FirstName"]="Sanket"
dict["LastName"]="Patil"

print(dict)
print(dict["LastName"])

#if-else
greeting = "Good Morning"
if greeting == "Good Morning":
    print("Condition Matches")
else:
    print("Incorrect condition")



#for loop

obj=[2,3,4,5,6,7]
for i in obj:
    print(i)

#sum of first 5 natural number
sum=0
for i in range(1,6):
    sum=sum+i


print(sum)

#while loop
i=3

while i>1:
    print(i)
    i=i-1

print("while loop condition is done")
