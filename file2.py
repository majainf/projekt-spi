def calculate_average():
    print("Obliczanie średniej ocen.")
    
    grades = []
    
    while True:
        try:
            grade = input("Wprowadź ocenę od 1 do 6 (lub wpisz '-', aby zakończyć): ")
            if grade.lower() == '-':
                break
            grade = float(grade)
            if 0 <= grade <= 6:
                grades.append(grade)
            else:
                print("Ocena musi być w zakresie od 0 do 6. Spróbuj ponownie.")
        except ValueError:
            print("Nieprawidłowa wartość. Wprowadź liczbę lub '-'.")
    
    if grades:
        average = sum(grades) / len(grades)
        print(f"Średnia ocen to: {average:.2f}")
    else:
        print("Nie wprowadzono żadnych ocen.")

calculate_average()
