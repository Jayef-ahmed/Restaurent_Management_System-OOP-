from User import Admin,Customer,Employee
from food_items import FoodItem
from restaurent import Restaurent
from menu import Menu
from orders import Order

mamar_restaurent = Restaurent("Mamar Restaurent")
def customer_menu():
    name = input('Enter Your Name : ')
    email = input('Enter Your Email : ')
    phone = input('Enter Your Phone_Number : ')
    address = input('Enter Your Address : ')
    customer = Customer(name=name, phone=phone, email=email,address=address)

    while(True):
        print(f'\n****Welcome {customer.name}!!****')
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            customer.view_menu(mamar_restaurent)

        elif choice == 2:
            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter item Quantity : "))
            customer.add_to_cart(mamar_restaurent, item_name, item_quantity)

        elif choice == 3:
            customer.view_cart()

        elif choice == 4:
            customer.pay_bill()

        elif choice == 5:
            break

        else:
            print("Invalid input")
        
def admin_menu():
    name = input('Enter Your Name : ')
    email = input('Enter Your Email : ')
    phone = input('Enter Your Phone_Number : ')
    address = input('Enter Your Address : ')
    admin = Admin(name=name, phone=phone, email=email,address=address)

    while(True):
        print(f'\n****Welcome {admin.name}!!****')
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Items")
        print("6. Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            item_name = input("Enter Item Name : ")
            item_price = int(input("Enter Item Price : "))
            item_quantity = int(input("Enter Item quantity : "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_restaurent, item)

        elif choice == 2:
            name = input("Enter Employee Name : ")
            phone = input("Enter Employee Phone_no : ")
            email = input("Enter Employee Email : ")
            address = input("Enter Employee Email : ")
            designation = input("Enter Employee Designation : ")
            age = int(input("Enter Employee Age : "))
            salary = int(input("Enter Employee Salary : "))
            emp = Employee(name, phone, email, address, age, designation, salary)
            admin.add_employee(mamar_restaurent, emp)

        elif choice == 3:
            admin.view_employee(mamar_restaurent)

        elif choice == 4:
            admin.view_menu(mamar_restaurent)

        elif choice == 5:
            item_name = input("Enter item name : ")
            admin.remove_item(mamar_restaurent, item_name)

        elif choice == 6:
            break

        else:
            print("Invalid input")


while True:
    print("*****Welcome!*****")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        admin_menu()
    elif choice == 2:
        customer_menu()
    elif choice == 3:
        break
    else:
        print("***Invalid Input!!***")