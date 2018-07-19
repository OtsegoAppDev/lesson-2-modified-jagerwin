def printReceipt(name, coffeeNum, hChocolateNum, totalCost):
  print("*************************************")
  print("Thank you for purchasing from Knights Coffee Shop " + name)
  print(" ")
  print("Coffees..............." + str(coffeeNum)+" x 0.25")
  print("Hot Chocolates........" + str(hChocolateNum) + " x 0.50")
  print("----------------------------------")
  print("Total Cost.............$"+str(totalCost))
name = "John Doe"
coffeeNum = 3
hChocolateNum = 2
totalCost = 1.75
printReceipt(name, coffeeNum, hChocolateNum, totalCost)
#Added student work here