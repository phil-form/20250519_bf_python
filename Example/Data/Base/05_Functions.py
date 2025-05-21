def testFunction():
    print("test function")

def testArgFunc(agr_1, arg_2):
    for i in range(agr_1):
        print(arg_2)

def testRtnArg(agr_1, arg_2=50):
    print(agr_1, arg_2)
    arg_2 += 12
    return agr_1 * arg_2

a = 5
b = "my super string!"
testArgFunc(a, b)
testFunction()
c = testRtnArg(arg_2=a, agr_1=75)
print(c)
print(a)