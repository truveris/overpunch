# Overpunch Parser/Formatter

Extract and generate [overpunch](https://en.wikipedia.org/wiki/Signed_overpunch) formatted numbers.

## Examples:

```python
>>> import overpunch
>>> overpunch.format(123.45)
'1234E'
>>> overpunch.extract("1234E")
Decimal('123.45')
```

## Requirements:
* Python 2.7+ or Python 3

## Tests:
Without coverage:

```shell
$ nosetests
```

With coverage:

```shell
$ nosetests --with-coverage --cover-package=overpunch
```

