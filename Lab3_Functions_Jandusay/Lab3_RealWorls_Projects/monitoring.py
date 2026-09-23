def telemetry_generator(last_name, seed_num, artist):
    base = len(last_name) + seed_num + len(artist)

    for i in range(6):
        yield base + (i * seed_num)


def validate_reading(value):
    if value < 0:
        raise ValueError("Invalid telemetry value")
    return True


def process_reading(value):
    return value * 2