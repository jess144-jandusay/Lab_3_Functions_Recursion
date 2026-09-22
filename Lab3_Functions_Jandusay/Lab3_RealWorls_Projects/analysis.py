def filter_values(values):
    return list(filter(lambda x: x >= 50, values))


def monitor(func):
    def wrapper(*args, **kwargs):
        print("Monitoring:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@monitor
def calculate_average(values):
    if not values:
        return 0
    return sum(values) / len(values)


def recursive_check(values, index=0):
    if index >= len(values):
        return 0

    abnormal = 1 if values[index] >= 80 else 0
    return abnormal + recursive_check(values, index + 1)