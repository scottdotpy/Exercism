# Exercism.io Solutions
## Python
#### Hello World

```python
def hello():
    return 'Hello, World!'

print(hello())
```

#### Leap

```python
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
```
