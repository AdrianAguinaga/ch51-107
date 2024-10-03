print("Hello world")
# console.log("Hello world");

# Variables
name = "adrian"
age = 138
found = False
name = True
name = 12
# let name = "adrian";
# const name = "adrian";
print(name)

# if/else statement
if age<100:
    print("dont worry youre not that old")
elif age==100:
    print("wow youre a century")
else:
    print("Well seems that youre a little bit old")

#fuctions
def say_Hello():
    print ("Hello there")
# function say_Hello(){}
#call functions
say_Hello()

print("my age is "+str(age)+" years old")

# array -- list
colors = ["yellow","green","blue"]
print(colors)

# add
colors.append("pink")
print(colors)


print(colors[0])

# # for loops
for x in colors:
    print(x)

# for(let i=0;i<colors.length;i++){
# let temp = colors[i];
# console.log(temp);
# }

# dictionary
me = {
    "first_name":"Adrian",
    "last_name":"Aguinaga",
    "age":38
}
print(me)
print(me["first_name"])
me["first_name"] = "Mauricio"
print(me["first_name"])




