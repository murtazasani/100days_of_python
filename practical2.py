name1 = input("What's your Name: ")
name2 = input("What's your Name: ")
name3 = input("What's your Name: ")

slices = input("Number of slices in Pizza: ")
priceOfPizza = input("What's price of the Pizza: ")

ateby1 = input(name1 + " How many slices you ate: ")
ateby2 = input(name2 + " How many slices you ate: ")
ateby3 = input(name3 + " How many slices you ate: ")

slicepercentage1 = (float(ateby1)/float(slices))*100
slicepercentage2 = (float(ateby2)/float(slices))*100
slicepercentage3 = (float(ateby3)/float(slices))*100

priceOf1 = (float(priceOfPizza)/int(100))*float(slicepercentage1)
priceOf2 = (float(priceOfPizza)/int(100))*float(slicepercentage2)
priceOf3 = (float(priceOfPizza)/int(100))*float(slicepercentage3)

print(name1 + " Your Bill is " + str(priceOf1) + " $.")
print(name2 + " Your Bill is " + str(priceOf2) + " $.")
print(name3 + " Your Bill is " + str(priceOf3) + " $.")
