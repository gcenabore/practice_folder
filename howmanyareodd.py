while True:
    odd_count = 0

    for i in range(10):
        num = int(input("Please enter a number: "))

        if num % 2 != 0:
            odd_count += 1

    print(f"the number of odd numbers is {odd_count}")

    retry = input("Do you want to try again? y/n: ")

    if retry != "y":
        break
    