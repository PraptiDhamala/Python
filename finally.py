# finally ma vako jailee execute huncha error aaye ni na aaye ni
# try:
#     l=[1,2,34,4]
#     i=int(input("Enter the index : "))
#     ptint(l[i])
# except:
#     print("error has occured: ")
# finally:
#     print("Whatever the situation I am always executed")

# print("Whatever the situation I am always executed")


def func1():
    try:
        l=[1,2,34,4]
        i=int(input("Enter the index : "))
        print(l[i])
        return 1
    except:
        print("error has occured: ")
        return 0
    finally:
        print("Whatever the situation I am always executed") #function execute huda ni huncha 

    # print("Whatever the situation I am always executed") #yo hunna

x=func1()
print(x)
