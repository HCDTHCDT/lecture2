def square(x):
    return x*x
def main():
    for i in range(10):
        print("{1} squared is {0}".format(square(i),i))

if __name__=="__main__":
    main()