
## Test sprawdzający wiedzę

### **🔹 Pytania jednokrotnego wyboru**
1. Co się stanie, jeśli w Pythonie wystąpi wyjątek i nie zostanie obsłużony?

   a) Program zignoruje błąd i będzie działać dalej.

   b) Program zatrzyma się i wyświetli komunikat błędu.

   c) Program samoczynnie poprawi błąd i kontynuuje działanie.

2. Jakie słowo kluczowe w Pythonie służy do obsługi błędów?
   
   a) `catch`

   b) `except`

   c) `handle`

3. Który kod poprawnie obsługuje błąd dzielenia przez zero?
   ```python
   try:
       x = 10 / 0
   except ZeroDivisionError:
       print("Nie można dzielić przez zero!")
   ```

4. Jaki typ wyjątku zostanie podniesiony przez poniższy kod?
   ```python
   lista = [1, 2, 3]
   print(lista[5])
   ```
   
   a) `KeyError`

   b) `IndexError`

   c) `TypeError`

---

### **🔹 Uzupełnij kod**

5. Uzupełnij kod, aby poprawnie obsługiwał wyjątek `ValueError`, gdy użytkownik wpisze niepoprawną wartość.
```python
try:
    liczba = __________(input("Podaj liczbę: "))
except __________:
    print("Błąd! Wprowadź poprawną liczbę.")
```

6. Uzupełnij kod, aby dodać zapis błędów do pliku `errors.log` przy użyciu modułu `logging`.
```python
import logging

logging.basicConfig(filename="errors.log", level=__________)

try:
    wynik = 10 / 0
except ZeroDivisionError as e:
    logging.__________(f"Błąd: {e}")
```

7. Uzupełnij kod, aby użyć `assert` do sprawdzenia, czy liczba jest większa od zera.
```python
def sprawdz_liczbe(n):
    assert _______________, "Liczba musi być dodatnia!"
    print("Liczba jest poprawna.")

sprawdz_liczbe(-5)
```

---

### **🔹 Zadanie otwarte**

8. Napisz funkcję, która prosi użytkownika o wpisanie dwóch liczb i zwraca wynik ich dzielenia. Zastosuj `try-except`, aby obsłużyć `ZeroDivisionError` oraz `ValueError`.
```python
# Twoja funkcja:
```