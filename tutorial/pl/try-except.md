# **Obsługa błędów w Pythonie – try-except, debugowanie, logging i assert**

## **Cele lekcji:**
1. **Poznanie wyjątków w Pythonie i ich obsługi za pomocą `try-except-else-finally`.**
2. **Nauka skutecznego debugowania kodu przy użyciu `??print()🫣??` oraz `logging`.**
3. **Zastosowanie asercji (`assert`) do wykrywania błędów na wczesnym etapie.**
4. **Praktyczne wykorzystanie poznanych technik w zadaniach.**

---

## **I. Wprowadzenie**

### **Co to są błędy w Pythonie?**
- **Błędy składniowe (SyntaxError)** – np. brak średnika `:` po `if`.
- **Wyjątki (Exceptions)** – błędy w czasie działania programu, np. `ZeroDivisionError`, `ValueError`.

### **Przykłady popularnych wyjątków:**
```python
# ZeroDivisionError - dzielenie przez zero
print(10 / 0)

# ValueError - błąd konwersji
int("abc")

# IndexError - dostęp do nieistniejącego indeksu w liście
lista = [1, 2, 3]
print(lista[5])

# KeyError - brakujący klucz w słowniku
slownik = {"name": "Jan"}
print(slownik["wiek"])
```

---

## **II. Obsługa błędów try-except**

### **Podstawowy try-except:**
```python
try:
    wynik = 10 / 0
except ZeroDivisionError:
    print("Błąd: nie można dzielić przez zero!")
```

### **Obsługa różnych wyjątków:**
```python
try:
    liczba = int(input("Podaj liczbę: "))
    wynik = 10 / liczba
except ZeroDivisionError:
    print("Nie dziel przez zero!")
except ValueError:
    print("Niepoprawna wartość!")
except Exception as e:
    print(f"Niespodziewany błąd: {e}")
```

### **Blok `else` i `finally`:**
```python
try:
    x = int(input("Podaj liczbę: "))
    wynik = 10 / x
except ZeroDivisionError:
    print("Błąd: dzielenie przez zero.")
else:
    print(f"Wynik: {wynik}")
finally:
    print("Koniec działania programu.")
```

---

## **III. Debugowanie kodu – print() i logging**

### **Używanie `print()` do śledzenia błędów:**

Wyjasnienie dlaczego print() od debag to bardzo zły pomysł 😱

```python
def dzielenie(a, b):
    print(f"a = {a}, b = {b}")
    return a / b

print(dzielenie(10, 2))
```

### **Zastosowanie `logging` do monitorowania błędów:**
```python
import logging

logging.basicConfig(level=logging.ERROR, filename="errors.log")

try:
    x = int(input("Podaj liczbę: "))
    wynik = 10 / x
except Exception as e:
    logging.error(f"Błąd: {e}")
    print("Coś poszło nie tak! Sprawdź logi.")
```

---

## **IV. Asercje (`assert`) – wykrywanie błędów wcześnie**

```python
def sprawdz_dane(wiek):
    assert wiek >= 0, "Wiek nie może być ujemny!"
    print(f"Podany wiek: {wiek}")

sprawdz_dane(-5)  # Błąd: AssertionError
```
---

## **VI. Podsumowanie**
- `try-except` – jak obsługiwać błędy?
- **debugowanie** – ~~print()~~ vs. `logging`.
- `assert` – jak wykrywać błędy wcześnie?
- Czy `assert` powinno być używane w kodzie produkcyjnym?
- Jakie są inne narzędzia do debugowania?

---
## 📌 Dodatkowe materiały

- Oficjalna dokumentacja Pythona: https://docs.python.org/3/library/exceptions.html

- https://www.w3schools.com/python/python_try_except.asp

- Kurs logging: https://realpython.com/python-logging/

