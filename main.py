# This program calculates a retail item's
# sale price.

# DISCOUNT_PERCENTAGE is used as a global
# constant for the discount percentage.
DISCOUNT_PERCENTAGE = 0.20

def calcSalePrice(regularPrice,DISCOUNT_PERCENTAGE):
    discount_removed = regularPrice * DISCOUNT_PERCENTAGE
    salePrice = round(regularPrice - discount_removed,2)

    return salePrice

def getRegularPrice():
    userRegularPrice = int(input("Enter the item's regular price: "))

    return userRegularPrice

# The main function.
def main():
# Get the item's regular price.
    regularPrice =getRegularPrice()

    print("Regular item's Price: " + str(regularPrice))

# Calculate the sale price.
    calcSalePrice(regularPrice,DISCOUNT_PERCENTAGE)
# Display the sale price.
    print("Sale Price: " + str(calcSalePrice(regularPrice,DISCOUNT_PERCENTAGE)))

# The get_regular_price function prompts the
# user to enter an item's regular price and it
# returns that value.

if __name__ == '__main__':
    main()
# The discount function accepts an item's price
# as an argument and returns the amount of the
# discount, specified by DISCOUNT_PERCENTAGE.


# Call the main function.

