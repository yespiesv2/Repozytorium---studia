print("Hello World!")
print("This is a simple Python script that prints 'Hello World!' and a message to the console.")

while True:
    user_input = input("Type 'exit' to quit the program: ")
    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
    else:
        print(f"You typed: {user_input}. Please type 'exit' to quit.")