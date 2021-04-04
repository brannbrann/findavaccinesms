def testy(y):
    y += 'another test'

def testx():
    x = []
    x.append('this is a test')
    y = x[:]

    testy(y)

    print(x,y)

testx()

# Because lists are mutable in Python :D 
# That means when you assign x = y, it really means they are the same variable
# with two (or more) names. Rather confusing.