print("Cześć! Witaj w prostym skrypcie Pythona, który wypisuje 'Hello World!' i wiadomość na konsoli.")

while True:
    user_input = input("Wpisz 'exit' aby wyjść z programu: ")
    if user_input.lower() == 'exit':
        print("Wychodzenie z programu. Do widzenia!")
        break
    else:
        print(f"Wpisałeś: {user_input}. Proszę wpisać 'exit' aby wyjść.")

    while True:
        nested_input = input("Wpisz 'back' aby wrócić do menu głównego: ")
        if nested_input.lower() == 'back':
            print("Wraca do menu głównego.")
            break
        else:
            print(f"Wpisałeś: {nested_input}. Proszę wpisać 'back' aby wrócić do menu głównego.")
