# Coeus Factory - Database Connector Factory

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/coeusfactory)](https://pypi.python.org/pypi/coeusfactory/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Coverage](https://raw.githubusercontent.com/mamerisawesome/coeusfactory/master/assets/coverage.svg?sanitize=true)](https://github.com/mamerisawesome/coeusfactory)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](mailto:atmalmer23@gmail.com)
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)
[![ForTheBadge powered-by-electricity](http://ForTheBadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)

A Database Connector interface that follows a factory model pattern.

## Installation

```bash
# if using poetry
# highly recommended
poetry add coeusfactory

# also works with standard pip
pip install coeusfactory
```

Then add necessary database interfaces as necessary. Below are the libraries that works with Coeus Factory.

| Database | Python Library | Status            |
|----------|----------------|-------------------|
| **MongoDB**  | *pymongo*      | <span style="color:green">Passed unit tests</span> |
| **DynamoDB** | *boto3*        | <span style="color:yellow">WIP</span>              |

## Getting Started

For every first step for any database, initialization and connections will come first. As long as it is supported in the factory, you can pass the parameters you normally handle in supported databse interfaces.

```python
from coeusfactory import ConnectorFactory
cf = ConnectorFactory(
    interface="<database>",
    db="<database-name>"
    # other config or atuh params for the db
    username="",
    password=""
)

# db init
cf.handler.initialize()
cf.handler.connect()
```

## Connector Methods

### Getting / Creating a model

```python
Users = cf.get_model("Users")
Carts = cf.get_model("Carts")
CustomerReviews = cf.get_model("CustomerReviews")
```

### Retrieval

```python
Users.get_by_id(0)
Users.get({"name": "Test User"})
```

### Insertion

```python
Users.add({"name": "Test User"})
```

### Deletion

```python
Users.delete_by_id(0)
Users.delete({"name": "Test User"})
```

### Modification

```python
Users.update_by_id(0, {"name": "New Name"})
Users.update({"name": "Test User"}, {"name": "New Name"})
```

### Entry Count

```python
Users.count()
```
