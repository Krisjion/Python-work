# - master fruit store dictionary
fruits = {"apple": 2, "banana": 1}

# - total purchase cost
running_total = 0

# - ask user which fruit they want until they are ready to purchase by typing 'done'
while True:
    user_fruit = input("Apple or banana? ")
    
    if user_fruit in fruits:
        running_total += fruits[user_fruit]
        print(fruits[user_fruit])
        
    elif user_fruit == 'done':
        break
        
    elif user_fruit not in fruits:
        print("Fruit not found, try again.")
        
print(f"Your total today is {running_total}")

