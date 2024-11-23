# print even number from 100
"""for i in range(100):
    if i % 2 != 0:
        continue
    print(i)""" 


# print odd number fromm 100 
"""odd_count = 0
while odd_count <= 100:
    if odd_count % 2 != 0:
        print(odd_count)
    odd_count += 1"""

# print all numbers from 1-100 except those numbers that ends with 0 and 5
"""for i in range(101):
    if i % 10 != 5 and i % 10 != 0:
        print(i)"""

# def function practice argument
"""
def what_is_my_name(first_name, second_name):
    full_name = first_name + " " + second_name
    print("hello", full_name, "how are you doing?")

first_name = input("Please enter your first name: ")
second_name = input("Plese enter your second name: ")

what_is_my_name(first_name, second_name)"""

# print all the numbers from between

def print_numbers_between():
    while True:
        num1 = int(input("Please enter a number: "))
        num2 = int(input("pleaseee enter another number: "))

        if num1 > num2:
            print(f"the numbers between {num2} and {num1}: ")
            number = num2 + 1

            while number < num1:
                print(number)
                number += 1

        else:
            print("Invalid: the first number must be greater than the second.") 
        retry = input("Do you want to try again? y/n: ")
        if retry != "y":
            print("ogey edi wag!")
            break
if __name__ == '__main__':
    print_numbers_between()
 



