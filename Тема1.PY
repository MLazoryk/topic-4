# Setting up the prices for the products
price_per_croissant = 1.04
price_per_glass = 0.34
price_per_coffee_pack = 4.42

# Quantity of each product
num_croissants = int(input("Enter the number of croissants: "))
num_glasses = int (input("Enter the number of glasses: "))
num_coffee_packs = int (input("Enter the number of coffee packs: "))

# Calculate the Total Cost
total_cost = num_croissants * price_per_croissant + \
num_glasses * price_per_glass + \
num_coffee_packs * price_per_coffee_pack 

# Determine the number of whole dollars and cents
total_dollars = int (total_cost)
total_cents = int (total_cost * 100)

# Output the result 
print (f"Total cost in whole dollars: {total_dollars} dollars" )
print (f"Total cost in cents: {total_cents} cents" )
