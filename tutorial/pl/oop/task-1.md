### Zadanie 1: Klasa Samochód

**Cel:** Stwórz klasę w Pythonie reprezentującą samochód z podstawowymi funkcjonalnościami.

**Wymagania:**
1. Klasa `Samochod` powinna mieć następujące atrybuty:
   - `marka` (np. "Toyota")
   - `model` (np. "Corolla")
   - `rok_produkcji` (np. 2020)
   - `przebieg` (w kilometrach, domyślnie 0)
2. Klasa powinna zawierać następujące metody:
   - `przejedz_dystans(kilometry)` – zwiększa przebieg o podaną liczbę kilometrów.
   - `opis()` – zwraca string w formacie: "marka model (rok_produkcji), przebieg: przebieg km".
   - `czy_stary()` – zwraca `True`, jeśli samochód ma więcej niż 10 lat (na podstawie roku 2025), w przeciwnym razie `False`.

**Przykładowy kod:**
```python
class Samochod:
    def __init__(self, marka, model, rok_produkcji, przebieg=0):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg
    
    def przejedz_dystans(self, kilometry):
        self.przebieg += kilometry
    
    def opis(self):
        return f"{self.marka} {self.model} ({self.rok_produkcji}), przebieg: {self.przebieg} km"
    
    def czy_stary(self):
        return (2025 - self.rok_produkcji) > 10

# Test
samochod = Samochod("Toyota", "Corolla", 2018)
samochod.przejedz_dystans(15000)
print(samochod.opis())
print(samochod.czy_stary())
```

**Zadanie do wykonania:**
- Stwórz instancję klasy dla swojego ulubionego samochodu.
- Dodaj 10 000 km przebiegu i wyświetl opis.

---

### Zadanie 2: Zapis danych do pliku

**Cel:** Rozszerz klasę `Samochod` o możliwość zapisu danych do pliku.

**Wymagania:**
1. W metodzie `przejedz_dystans(kilometry)` dodaj zapis aktualnych danych samochodu do pliku `samochod_dane.txt` w formacie CSV (np. "marka,model,rok_produkcji,przebieg").
2. Użyj kontekstu `with` do obsługi pliku.

**Przykładowy kod:**
```python
class Samochod:
    def __init__(self, marka, model, rok_produkcji, przebieg=0):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg
    
    def przejedz_dystans(self, kilometry):
        self.przebieg += kilometry
        with open("samochod_dane.txt", "w") as plik:
            plik.write(f"{self.marka},{self.model},{self.rok_produkcji},{self.przebieg}")
    
    def opis(self):
        return f"{self.marka} {self.model} ({self.rok_produkcji}), przebieg: {self.przebieg} km"
    
    def czy_stary(self):
        return (2025 - self.rok_produkcji) > 10

# Test
samochod = Samochod("Honda", "Civic", 2019)
samochod.przejedz_dystans(5000)
print(samochod.opis())
```

**Zadanie do wykonania:**
- Stwórz instancję samochodu i dodaj 5000 km przebiegu.
- Sprawdź zawartość pliku `samochod_dane.txt` po wykonaniu operacji.

---

### Zadanie 3: Pobieranie danych, dodawanie, usuwanie, edycja

**Cel:** Rozszerz klasę `Samochod` o zarządzanie danymi w pliku (CRUD: Create, Read, Update, Delete).

**Wymagania:**
1. Dodaj metodę `wczytaj_z_pliku()`, która odczytuje dane z pliku `samochod_dane.txt` i aktualizuje atrybuty obiektu.
2. Rozszerz zapis tak, aby obsługiwał wiele samochodów (np. każda linia w pliku to jeden samochód).
3. Dodaj metody:
   - `dodaj_do_pliku()` – zapisuje dane samochodu jako nową linię w pliku.
   - `usun_z_pliku(marka, model)` – usuwa samochód o podanej marce i modelu z pliku.
   - `edytuj_w_pliku(stary_marka, stary_model)` – edytuje dane samochodu w pliku.

**Przykładowy kod:**
```python
class Samochod:
    def __init__(self, marka, model, rok_produkcji, przebieg=0):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg
    
    def przejedz_dystans(self, kilometry):
        self.przebieg += kilometry
        self.edytuj_w_pliku(self.marka, self.model)
    
    def opis(self):
        return f"{self.marka} {self.model} ({self.rok_produkcji}), przebieg: {self.przebieg} km"
    
    def czy_stary(self):
        return (2025 - self.rok_produkcji) > 10
    
    def wczytaj_z_pliku(self):
        try:
            with open("samochod_dane.txt", "r") as plik:
                dane = plik.read().splitlines()
                for linia in dane:
                    marka, model, rok, przebieg = linia.split(",")
                    if marka == self.marka and model == self.model:
                        self.rok_produkcji = int(rok)
                        self.przebieg = int(przebieg)
                        break
        except FileNotFoundError:
            print("Plik nie istnieje.")
    
    def dodaj_do_pliku(self):
        with open("samochod_dane.txt", "a") as plik:
            plik.write(f"{self.marka},{self.model},{self.rok_produkcji},{self.przebieg}\n")
    
    def usun_z_pliku(self, marka, model):
        try:
            with open("samochod_dane.txt", "r") as plik:
                linie = plik.read().splitlines()
            with open("samochod_dane.txt", "w") as plik:
                for linia in linie:
                    dane = linia.split(",")
                    if dane[0] != marka or dane[1] != model:
                        plik.write(linia + "\n")
        except FileNotFoundError:
            print("Plik nie istnieje.")
    
    def edytuj_w_pliku(self, stara_marka, stary_model):
        self.usun_z_pliku(stara_marka, stary_model)
        self.dodaj_do_pliku()

# Test
samochod1 = Samochod("Toyota", "Corolla", 2018)
samochod1.dodaj_do_pliku()
samochod2 = Samochod("Honda", "Civic", 2019)
samochod2.dodaj_do_pliku()

samochod1.przejedz_dystans(5000)  # Edycja w pliku
samochod2.usun_z_pliku("Honda", "Civic")  # Usunięcie
print(samochod1.opis())
```

**Zadanie do wykonania:**
- Dodaj dwa samochody do pliku.
- Edytuj przebieg jednego z nich o 3000 km.
- Usuń drugi samochód z pliku.
- Wczytaj dane pierwszego samochodu i wyświetl jego opis.
