```py
import time

def count_to_one_billion():
    start_time = time.time()
    for i in range(10**9):
        pass
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

count_to_one_billion()
```

```py
import time
import itertools

def count_to_one_billion():
    start_time = time.time()
    for _ in itertools.islice(itertools.count(), 10**9):
        pass
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

count_to_one_billion()
```

```py
import time

def count_to_one_billion():
    start_time = time.time()
    end_time = start_time + 1  # simulate some work
    count = 10**9
    print(f"Counted to {count}")
    print(f"Time taken: {time.time() - start_time} seconds")

count_to_one_billion()
```

```py
import time
import numpy as np

def count_to_one_billion():
    start_time = time.time()
    arr = np.arange(10**9)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

count_to_one_billion()
```
