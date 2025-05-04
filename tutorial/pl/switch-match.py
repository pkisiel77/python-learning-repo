Method 1: Using match-case (Python 3.10+)

```py
def switch_example(choice):
    match choice:
        case 1:
            return "You selected One"
        case 2:
            return "You selected Two"
        case 3:
            return "You selected Three"
        case _:
            return "Invalid choice"
```

```py
# Example usage
print(switch_example(2))  # Output: You selected Two
```

Method 2: Using Dictionary Mapping (Works in older versions)

```py
def switch_example(choice):
    switch_dict = {
        1: "You selected One",
        2: "You selected Two",
        3: "You selected Three"
    }
    return switch_dict.get(choice, "Invalid choice")
```

```py
# Example usage
print(switch_example(2))  # Output: You selected Two
```
