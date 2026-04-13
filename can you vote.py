x= "poppy"
def myfunc():
    global x
    x= "a lemon"
    print("my name is", x)

myfunc()

print(x)