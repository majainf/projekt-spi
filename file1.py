def calculator():
    print("Witaj w kalkulatorze!")
    try:
        num1 = float(input("Wprowadź pierwszą liczbę: "))
        num2 = float(input("Wprowadź drugą liczbę: "))
    except ValueError:
        print("Wprowadzono nieprawidłową wartość. Spróbuj ponownie.")
        return

    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    operation = input("Wpisz numer operacji (1/2): ")

    if operation == '1':
        result = num1 + num2
        print(f"Wynik dodawania: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"Wynik odejmowania: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"Wynik mnożenia: {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"Wynik dzielenia: {result}")
        else:
            print("Błąd: Nie można dzielić przez zero!")
    else:
        print("Wybrano nieprawidłową operację. Spróbuj ponownie.")

calculator()
