order_amount = float(input("Enter the order amount: Rs."))
membership = input("Are you a member? (yes/no): ").strip().lower()

if order_amount < 0 or order_amount > 100000:
    print("Invalid order amount.")
    print("Order amount must be between ₹0 and ₹1,00,000.")

else:
    if order_amount >= 5000:
        discount_percentage = 15
        eligibility = "Eligible for 15% discount"

    elif order_amount >= 2000 and order_amount < 5000 and membership == "yes":
        discount_percentage = 10
        eligibility = "Eligible for 10% discount"

    else:
        discount_percentage = 0
        eligibility = "Not eligible for a discount"

    discount_amount = order_amount * discount_percentage / 100
    final_amount = order_amount - discount_amount

    print("Original amount: Rs.", order_amount)
    print("Discount percentage:", discount_percentage, "%")
    print("Discount amount: Rs.", discount_amount)
    print("Final payable amount: Rs.", final_amount)
    print("Eligibility status:", eligibility)
