# store-manager-api

[![Build Status](https://travis-ci.com/danielotieno/store-manager-api.svg?branch=ch-api-161336932)](https://travis-ci.com/danielotieno/store-manager-api)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a6389889a33c56eb0160/test_coverage)](https://codeclimate.com/github/danielotieno/store-manager-api/test_coverage)
[![codecov](https://codecov.io/gh/danielotieno/store-manager-api/branch/ch-api-161336932/graph/badge.svg)](https://codecov.io/gh/danielotieno/store-manager-api)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/00b0e64ca606433e86c2a51ba46439c4)](https://www.codacy.com/app/danielotieno/store-manager-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=danielotieno/store-manager-api&amp;utm_campaign=Badge_Grade)

Store Manager is a web application that helps store owners manage sales and product inventory records.

## Application Demo

Deployed Link [store-manager-api](https://store-manager-app-v1.herokuapp.com)

## API Endpoints

| EndPoint                    | Functionality                    |
| --------------------------- | -------------------------------- |
| GET  /products              | Get all the products.            |
| GET  /products/<product_id> | Fetch a specific product         |
| POST /products              | Add a new product.               |
|                             |
| GET  /sales/                | Get all sales record             |
| GET  /sales/<sale_id>       | Fetch a specific sale record     |
| POST /sales/                | Create a new sale order          |
|                             |
| POST /signup                | Register a new user              |
| POST /login                 | Enables registered user to login |

### Technologies used to build the application

[Python 3.6](https://docs.python.org/3.6/)

[Pytest](https://docs.pytest.org/en/latest/)

[Pylint](https://docs.pylint.org/en/1.6.0/installation.html)

[Flask](http://flask.pocoo.org/)

[Flask Restful](https://flask-restful.readthedocs.io/en/latest/)

[Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/latest/index.html)

#### How should this be manually tested

Fork the repo here [Fork me](https://github.com/danielotieno/store-manager-api/tree/api)

`git clone the forked repo in your machine`

#### Create a virtual environment

`python3 -m venv venv`

#### Activate the virtual environment

`source venv/bin/activate`

#### Install dependencies

`pip install -r requirements.txt`
`pip install pylint`

#### Change directory to develop branch

`cd api`

#### Then run the command below to start the application

`python run.py`

#### Running Tests

`pytest -v`

#### Running Pylint

`pylint app`
`pylint run.py`

### Users

#### User registration

Send a `POST` request to `/api/v1/auth/signup` endpoint with the payload in `JSON`

#### User Login

Send a `POST` request to `/api/v1/auth/login` endpoint with the payload in `JSON`

#### Get list of all products

Send a `GET` request to `/api/v1/products`

#### Featch a specific product

Send a `GET` request to `/api/v1/products/<product_id>`

#### Place/Create a product

Send a `POST` request to `/api/v1/products` endpoint with the payload in `JSON`

#### Get list of all sales record

Send a `GET` request to `/api/v1/sales`

#### Featch a specific sale record

Send a `GET` request to `/api/v1/sales/<sale_id>`

#### Place/Create a sale order

Send a `POST` request to `/api/v1/sales` endpoint with the payload in `JSON`
