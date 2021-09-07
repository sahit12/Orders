import json
from .delivery import discount
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def orders(request):

    total_cost = 0

    if request.method == 'POST':

        try:

            # Getting the request data content that was passed with the POST request
            data = json.loads(request.body)

            # Adding the total order cost each items
            for order in data['order_items']:
                total_cost += order['price'] * order['quantity']

            # Adding the delivery cost
            distance = data['distance']
            _distance = distance / 1000
            d = discount(_distance)

            # if the distance passed is not in the range of 0-500(km),
            # discount function will return Invalid Distance json response
            if d == 'Invalid Distance':
                return JsonResponse({'message': 'Invalid Distance'}, status=500)
            else:
                total_cost += d

            # Adding discount if possible

            # If the discount's offer type is DELIVERY, it will just
            # remove the above accounted delivery charge from the total cost.

            if 'offer' in data:
                if data['offer']['offer_type'] == 'FLAT':
                    total_cost -= data['offer']['offer_val']
                if data['offer']['offer_type'] == 'DELIVERY':
                    total_cost -= d

            # Return the total cost response
            return JsonResponse({'order_total': total_cost}, safe=False)

        except Exception as e:
            print(e)
    else:
        return JsonResponse({'message': 'Invalid Request'}, status=403)
