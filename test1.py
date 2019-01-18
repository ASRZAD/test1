
def s1(a,b) :
    return(a+b)

def f1  (s1):
    def wrapper(*args,**kwargs):
        args=map(int,args)
        return s1(*args)
    return wrapper
s=f1(s1)
s1=s("2",3)
print(s1)
#@@@@@@@@@@@@@@@@@@@@@@@@@@

print((4).__sizeof__())
(4).__sizeof__()

#@@@@@@@@@@@@@@@@@@@@@@@@@@

with open ('a.txt','r') as f:
    content=f.read()
#print(1/0)

f.closed
s=f.closed
print(s,content)

#@@@@@@@@@@@@@@@@@@@@@@@@@@

def greet(name):
    print("hello {}".format(name))
if __name__=='__main__':
    name=input("what is your name")
    print(name)
    greet(name)

