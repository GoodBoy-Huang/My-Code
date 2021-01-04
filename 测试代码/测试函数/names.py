from get_name import get_name

print("Enter 'q' at any time to quit.")
while True:
    first_name = input("\nPlease enter your first name:")
    if first_name == "q":
        break
    last_name = input("Please give me a last name:")
    if last_name == "q":
        break

    name = get_name(first_name,last_name)
    print("\tNeatly formatted name: " + name + '.')



