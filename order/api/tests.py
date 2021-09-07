from django.urls import reverse
from django.test import TestCase, Client


class OrdersViewTests(TestCase):

    def test_if_request_data_is_accessible(self):

        # instantiate the Django test client
        c = Client()

        body = [{
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
        }, {
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
        }, {
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
        }]
        body_ans = ['14300', '10300', '41000']
        for idx, data in enumerate(body):
            response = c.post('/orders/', data, content_type='application/json')
            print(response.content.decode('utf-8'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, body_ans[idx])
