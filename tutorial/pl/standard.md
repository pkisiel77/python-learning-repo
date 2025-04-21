- PEP 484
- PEP 8
- PEP 257

W Pythonie można stosować wskazówki typów (type hints) zgodnie z zaleceniami PEP 484 oraz konwencjami PEP 8. To oznacza, że:
## 1.	Typowanie zmiennych i parametrów:

Deklarujesz typy parametrów funkcji oraz wartość zwracaną:

```py
def add_numbers(a: int, b: int) -> int:
    return a + b
```

Typujesz zmienne lokalne:

```py
count: int = 0
names: list[str] = ["Alice", "Bob", "Charlie"]
```

Możesz używać adnotacji z typing (dla wersji poniżej 3.9) lub wbudowanych typów (dla Pythona 3.9+):

```py
from typing import List

def get_even_numbers(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num % 2 == 0]
```

## 2.	Zachowanie czytelności kodu:

Stosujesz odpowiednie wcięcia (4 spacje na poziom).

Używasz czytelnych nazw funkcji i zmiennych (np. calculate_average, a nie calc_avg).

Rozbijasz kod na mniejsze funkcje, jeśli jedna zaczyna robić zbyt wiele.

## 3.	Zgodność z PEP 8:

PEP 8 to oficjalny zbiór wytycznych dotyczących formatowania kodu Pythona.

W skrócie:
- Linijki mają do 79 znaków.
- Jedna pusta linia pomiędzy definicjami funkcji.
- Dwie puste linie pomiędzy definicjami klas.
- Używanie spacji wokół operatorów:

```py
result = x + y
```


Używanie czytelnych konstrukcji warunkowych:

```py
if value is None:
    ...
```

## 4. Dodawanie typów do bardziej złożonych struktur danych:

Przy listach zawierających różne typy:

```py
from typing import Union

data: list[Union[int, str]] = [1, "two", 3]
```

Przy słownikach:

```py
from typing import Dict

settings: Dict[str, int] = {"width": 800, "height": 600}
```

## 5. Stosowanie statycznych narzędzi do sprawdzania zgodności z typami:

Możesz używać narzędzi takich jak mypy, które analizują kod pod kątem zgodności z adnotacjami typów.

Polecenie:

```
mypy your_script.py
```


Pomoże upewnić się, że typowanie jest prawidłowe.

## 6. Dodawanie docstringów (zgodnie z PEP 257):

Dodajesz krótkie opisy funkcji i klas, aby kod był bardziej zrozumiały:

```py
def multiply(a: int, b: int) -> int:
    """
    Multiplies two numbers together.

    :param a: The first number
    :param b: The second number
    :return: The product of a and b
    """
    return a * b
```

Podsumowując, aby zapisać kod zgodny z najlepszymi praktykami i typowaniem, stosujesz się do powyższych zasad, dodajesz odpowiednie wskazówki typów, formatujesz kod zgodnie z PEP 8, a w razie potrzeby korzystasz z narzędzi takich jak mypy, aby zapewnić jego poprawność.
