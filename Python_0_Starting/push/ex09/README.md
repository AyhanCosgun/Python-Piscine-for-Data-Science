# ft_package

A small sample Python package for Python Piscine exercise 09.

## Installation

Build the package:

```bash
python3 -m build
```

Install from the generated wheel:

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

Or install from the source distribution:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
```

Output:

```text
2
0
```

## License

MIT

## Uninstall

Remove the installed package from the current Python environment:

```bash
python3 -m pip uninstall ft_package
```

Check that it was removed:

```bash
python3 -m pip show ft_package
```

## Clean Build Files

Remove generated build artifacts:

```bash
rm -rf dist build ft_package.egg-info
find . -type d -name "__pycache__" -exec rm -rf {} +
```
