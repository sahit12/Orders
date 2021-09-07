# Orders API

## Instructions to run the code
* `git clone https://github.com/sahit12/Orders.git && cd Orders`

* `python order/manage.py runserver`

* Paste your data in POSTMAN with the request method being a **POST** and API as `http://127.0.0.1:8000/orders/`. Add the data under **Body** tab. (Example data below)

4. **Optional**: To check the API with different datasets, I have added test cases. To run it - `python order/manage.py test api`

## Working Examples

1. **Example data 1**
```json {
    "order_items": [
        {
            "name": "bread",
            "quantity": 2,
            "price": 2200
        },
        {
            "name": "butter",
            "quantity": 1,
            "price": 5900
        }
    ],
    "distance": 1200,
    "offer": {
        "offer_type": "FLAT",
        "offer_val": 1000
    }
}
```
![First Example](images/first_order.png?raw=true)

2. **Example data 2**
```json {
    "order_items": [
        {
            "name": "bread",
            "quantity": 2,
            "price": 2200
        },
        {
            "name": "butter",
            "quantity": 1,
            "price": 5900
        }
    ],
    "distance": 1200,
    "offer": {
        "offer_type": "DELIVERY"
    }
}
```
![Second Example](images/second_order.png?raw=true)

3. **Example data 3**
```json {
    "order_items": [
        {
            "name": "ice-cream",
            "quantity": 4,
            "price": 10000
        },
        {
            "name": "butter",
            "quantity": 1,
            "price": 6000
        }
    ],
    "distance": 5200,
    "offer": {
        "offer_type": "FLAT",
        "offer_val": 10000
    }
}
```
![Third Example](images/third_order.png?raw=true)

## Important Technical Decisions
* Technology used for backend: Django-3.2
* To test API: Postman
* Database not used as it was not required.
* Have assumed the request method to be a **POST** as passing the data content in the request body is safer with POST.
* Django by default use a csrf token for post requests for safety measures. I have removed it for this request to showcase the API easily.
* Not handled the exception case by case for the moment, current scenario doesn't require it, but could be handled better.
* Added the ALLOWED_HOSTS to only **localhost** callback.