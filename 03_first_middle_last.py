print("This program returns your initials.")
first_name = str(input("Enter your first name:"))
middle_name = str(input("Enter your middle name:"))
last_name = str(input("Enter your last name:"))
lotNumber = str("037-00901-00027")
countryCode = lotNumber[0:3]
productCode = lotNumber[4:9]
batchNumber = lotNumber[-5:]

    
print("Your initials are", first_name[0:1],".", middle_name[0:1],".", last_name[0:1])
print("Lot number:",lotNumber)
print("Country code:",countryCode)
print("Product code:",productCode)
print("Batch number:",batchNumber)
