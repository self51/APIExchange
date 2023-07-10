# **APIExchange**

## About
This is a pet-project, it should not be used for commercial purposes!<br/>
APIExchange interacts with the Mexc Exchange API, providing views<br/>
to fetch exchange information, market data, candlestick data, and perform<br/>
actions like placing test orders, and retrieving account and wallet information.<br/>

### Technology stack:
* Python 3.8, Django 3.2;
* HTML & CSS.

### Getting Started

#### 1. Create your '.env' file
* Create '.env' file in the same directory as services.py.
* Declare your environment variables in .env.
* File must contain: API_KEY, API_SECRET. For example: API_KEY=this should be your API key.

#### 2. Set up MEXC API
* Create your API Key on the mexc.com website.
* Copy API_KEY and API_SECRET to '.env'.

#### 3. Install requirements and start the server.
* `$ pip install -r requirements.txt`.
* `$ python manage.py runserver`.

Made by `Self`.
