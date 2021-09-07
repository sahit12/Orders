
def discount(distance):

    DEFAULT_SLAB = {
        '0-10': 50,
        '10-20': 100,
        '20-50': 500,
        '50+': 1000
    }
    
    total_cost = 0

    if distance >= 0 and distance <= 10:
        total_cost += DEFAULT_SLAB['0-10'] * 100
    elif distance > 10 and distance <= 20:
        total_cost += DEFAULT_SLAB['10-20'] * 100
    elif distance > 20 and distance <= 50:
        total_cost += DEFAULT_SLAB['20-50'] * 100
    elif distance > 50 and distance <= 500:
        total_cost += DEFAULT_SLAB['50+'] * 100
    else:
        return 'Invalid Distance'

    return total_cost
