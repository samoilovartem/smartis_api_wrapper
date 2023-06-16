# SmartisAPI

A Python wrapper for the Smartis API.

## Description

The `smartis_api` package provides a simple way to interact with the Smartis API. It's designed to make it easier to work with the API's endpoints, providing clear, Pythonic methods for all the API's functions.

## Requirements

- Python 3.9+

## Installation

As this package is local and not published to PyPI, you can install it directly from the local directory:

```sh
pip install .
```

In case you use poetry just simple do:
```sh
poetry install
```

## Usage
The package provides classes for different components of the API.

For instance, to use the ReportsAPI:

```sh
from smartis_api.reports import ReportsAPI

api = ReportsAPI('<your-api-key>')

report_data = {
    # your report data
}

response = api.get_report(report_data)
```
Each API class provides methods that map to the corresponding endpoints of the Smartis API. Check the docstrings for each method for details on usage and parameters.

## Development
We're actively developing additional features for this package. If you encounter any bugs or have feature requests, please file an issue in our GitHub repository.

## License
This project is licensed under the terms of the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
