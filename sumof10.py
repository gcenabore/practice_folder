total_sum = 0
while True:
    current_sum = 0
    num = 0
    while num < 10:
        entry = int(input("Please enter a number: "))
        num += 1
        current_sum += entry
        print(f"the sum is {current_sum}")

    total_sum += current_sum
        
    retry = input("do you want to retry? y/n: ")

    if retry != "y":
        break

print(f"the total sum is {total_sum}")
    


    
    
    




    

        
