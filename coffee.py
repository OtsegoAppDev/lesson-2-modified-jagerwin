def printReceipt(name, coffeeNum, hChocolateNum, totalCost):
  print("*************************************")
  print("Thank you for purchasing from Knights Coffee Shop " + name)
  print(" ")
  print("Your Cashier was Joe Shmoe")
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

printReceipt("Mr. O'Shea", 20,0,5.00)
printReceipt("Ms. Jones", 0, 1, .50)
printReceipt("Mr. Jeffers", 1, 1, .75)

