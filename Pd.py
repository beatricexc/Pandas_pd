import pandas as pd
print(pd.__version__)

mydataset = {
    'cars' : ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]

}

myvar = pd.DataFrame(mydataset)

print(myvar)


#creating a simple Panda Series from a list

a = [1,7,2]

myvar = pd.Series(a)

print(myvar)

print(myvar[0]) # indexes as labels

myvar = pd.Series(a, index = ["x", "y", "z"])#creating custom labels

