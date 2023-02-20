def deco(fun):
    def wrap(*args,**kwargs):
        print("Start...")
        fun(*args,**kwargs)
        print("End...")
    return wrap

@deco
def show(msg):
    print("Message is : ",msg)

show("Welcome...")