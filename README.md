# Spacename
###### *An alternative to dictionaries, built on the argparse Namespace class.*

### Table of contents
[Back to Top](#spacename)

[Table of contents](#table-of-contents)

[Installation](#installation)
- [Using `pip`](#using-pip)
	- [*Nix](#nix)
	- [Windows](#windows)

[Usage](#usage)
- [Creating a Namespace](#creating-a-namespace)


## Installation
Currently, you are only able to install spacename using pip or similar package managers[^1]. However, this is set to change in the near future.

### Using `pip`
To install this package using pip, simply run the following command:

#### *Nix
```bash
pip3 install spacename
```

#### Windows
```cmd
pip install spacename
```


## Usage

### Creating a Namespace

```py
from spacename import Namespace

ns = Namespace(key="val")
print(ns.key)
```
Output:
```py
val
```

### Adding/modifying keys and values to the Namespace

```py
from spacename import Namespace

ns = Namespace(spam="fizz", bacon="buzz")
ns.spam = "foo" # Changing existing value
ns.eggs = "bar" # Creating a key-value pair
del ns.bacon # Deleting a key-value pair

print(ns)
```
Output:
```py
Namespace(spam="foo", eggs="bar")
```

### Converting to dict

```py
from spacename import Namespace

ns = Namespace(spam="foo", eggs="bar", bacon="baz")

print(dict(ns))

# OR

print(ns.to_dict())
```
Output:
```py
{'spam': 'foo', 'eggs': 'bar', 'bacon': 'baz'}
```

### Converting to list

```py
from spacename import Namespace

ns = Namespace(spam="foo", eggs="bar", bacon="baz")

print(list(ns))
```
Output:
```py
[('spam', 'foo'), ('eggs', 'bar'), ('bacon', 'baz')]
```

### Iterating through a Namespace

```py
from spacename import Namespace

ns = Namespace(spam="foo", eggs="bar", bacon="baz")

for k, v in ns:
	print(f"{k}=\"{v}\"")
```
Output:
```py
spam="foo"
eggs="bar"
bacon="baz"
```

### Comparing Namespaces with other Namespaces

```py
from spacename import Namespace

ns1 = Namespace(spam="foo", eggs="bar", bacon="baz")
ns2 = Namespace(foo="spam", bar="eggs", baz="bacon")

print(ns1 == ns2)
```
Output:
```py
False
```

### Checking that a Namespace contains a key

```py
from spacename import Namespace

ns = Namespace(spam="foo", eggs="bar", bacon="baz")

print("spam" in ns)
```
Output:
```py
True
```

[^1]: Supported package managers include, but are not limited to, pip, poetry, and any other package manager that supports the PyPI repository.