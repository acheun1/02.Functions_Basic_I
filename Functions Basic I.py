#Functions Basic I 
#2018 09 14
#Cheung Anthony

#Predict the output of the codes below without running the codes directly.
#Write down your predictions for all challenges below and once done, please compare your predictions with the results from the shell.         

def a():
    return 5
print(a())    
#OUTPUT=5

def a():
    return 5
print(a()+a())    
#OUTPUT = 10

def a():
    return 5
    return 10
print(a())
#OUTPUT = 5
#return 5 executes and return 10 never executes

def a():
    return 5
    print(10)
print(a())    
#OUTPUT = 5
#return 5 executes and print 10 never executes

def a():
    print(5)
            return(5)
x = a()
print(x)    
#OUTPUT = 5, None (because a() does not have a return

def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))  
#OUTPUT = (b+c) + (b+c)
#OUTPUT = (1+2) + (2+3)
#OUTPUT = 8

def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#OUTPUT = ERROR
#b and c converted to string

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a()) 
#OUTPUT = 100,10
#return 10 executes and return 7 never executes

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))    
#OUTPUT = 10
#return 10 executes and return 7 never executes

def a(b,c):
    return b+c
    return 10
print(a(3,5))    
b = 500
print(b)
#OUTPUT= 8 => 500
#return b+c executes and return 10 never executes and argument b is replaced to 500

def a():
    b = 300
    print(b)
print(b)
a()
print(b) 
b = 500
print(b)
#OUTPUT= error
#no print for a(), b is undefined as no global

def a():
    b = 300
    print(b)
    return b
print(b)
print(a())
print(b) 
b = 500
print(b)
#OUTPUT: none, 300 300, none, 500

def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#OUTPUT: none
#function a() is not called, so b not defined

def a():
    print(1)
    b()
    print(2)
#OUTPUT: none
#function not called and arguments not defined

def b():
    print(3)
a()
#OUTPUT:none
#function (a) is not defined

def a():
    print(1)
    x = b()
    print(x)
    return 10
#OUTPUT: none
# a() is never called

def b():
    print(3)
    return 5
y = a()
print(y)
#OUTPUT = error
#a() is not defined