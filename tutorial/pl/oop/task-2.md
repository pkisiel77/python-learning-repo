# Zadanie 2 – Dziedziczenie, specjalizacja i obsługa plików

W tym zadaniu będziesz kontynuować pracę z klasami i obiektami w Pythonie. Zaimplementujesz dziedziczenie, nadpisywanie metod, dodatkowe pola i metody w klasach potomnych oraz podstawową obsługę plików.

## Cel

- Ćwiczenie dziedziczenia klas w Pythonie
- Tworzenie metod `__str__()` i `make_sound()`
- Praca z atrybutami klas
- Zapisywanie i odczytywanie danych z pliku tekstowego

## Wymagania

1. Stwórz klasę `Animal`, która zawiera:
   - atrybuty: `name` (str), `age` (int)
   - metodę `make_sound()`, która wypisuje:  
     ```
     Generic animal sound
     ```
   - metodę `__str__`, która zwraca:  
     ```
     Animal: {name}, age: {age}
     ```

2. Stwórz klasę `Dog`, która dziedziczy po `Animal`. Dodaj:
   - atrybut `breed` (str)
   - nadpisz metodę `make_sound()` tak, aby wypisywała:  
     ```
     Woof!
     ```
   - nadpisz metodę `__str__`, aby zwracała:  
     ```
     Dog: {name}, age: {age}, breed: {breed}
     ```

3. Stwórz klasę `Cat`, która również dziedziczy po `Animal`. Dodaj:
   - atrybut `is_lazy` (bool)
   - nadpisz metodę `make_sound()` tak, aby wypisywała:  
     ```
     Meow!
     ```
   - nadpisz metodę `__str__`, aby zwracała:  
     ```
     Cat: {name}, age: {age}, lazy: yes/no
     ```

4. Dodaj funkcje do zapisu i odczytu zwierząt:
   - Funkcja `save_animals_to_file(animals, filename)` zapisuje dane zwierząt do pliku tekstowego (po jednej linii na zwierzę).
   - Funkcja `load_animals_from_file(filename)` wczytuje dane z pliku i tworzy odpowiednie obiekty klas `Animal`, `Dog` lub `Cat`.

   Plik powinien zawierać dane w formacie:
```
Animal;SomeAnimal;4
Dog;Rex;5;German Shepherd
Cat;Mittens;3;True
```

## Przykład działania

```python
a = Animal("SomeAnimal", 4)
d = Dog("Rex", 5, "German Shepherd")
c = Cat("Mittens", 3, True)

animals = [a, d, c]

for animal in animals:
 animal.make_sound()
 print(animal)

save_animals_to_file(animals, "animals.txt")

loaded = load_animals_from_file("animals.txt")
print("\nLoaded from file:")
for animal in loaded:
 animal.make_sound()
 print(animal)
