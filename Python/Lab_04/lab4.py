def box(title):
    print("\n" + "=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def lines(title):
    print("\n" + "-" * 50)
    print(f"{title:^50}")
    print("-" * 50)


box("DATA CONVERSION UTILITY")

product_name = input("Enter Product Name: ")
price = input("Enter Product Price: ")
quantity = int(input("Enter Product Quantity: "))
total_price = price * quantity
amount_str = str(total_price)


lines("TYPE CASTING SUMMARY")
print("Variable            Value                Python Type")
print("-" * 50)
print(f"Product Name       {product_name}       {type(product_name)}")
print(f"Price              {price}              {type(price)}")
print(f"Quantity           {quantity}           {type(quantity)}")
print(f"Total price        {total_price}        {type(total_price)}")
print(f"Amount Str         {amount_str}         {type(amount_str)}")
print("-" * 50)

lines("TAX INVOICE")

print(f"Product Name: {product_name}")
print(f"Price Per Unit: {price}")
print(f"Quantity: {quantity}")

print("-" * 50)
print(f"Invoice Total: {total_price}")
print("=" * 50)
