import monitoring
import analysis


LAST_NAME = "JANDUSAY"
SEED_NUM = 4
FAVORITE_ARTIST = "RINI"


telemetry = monitoring.telemetry_generator(
    LAST_NAME,
    SEED_NUM,
    FAVORITE_ARTIST
)

readings = list(telemetry)

valid_readings = []
invalid_readings = []

for value in readings:
    try:
        monitoring.validate_reading(value)
        valid_readings.append(value)
    except ValueError:
        invalid_readings.append(value)


processed = []

for value in valid_readings:
    processed.append(monitoring.process_reading(value))


filtered = analysis.filter_values(processed)

average = analysis.calculate_average(processed)

abnormal_count = analysis.recursive_check(processed)


print("=" * 40)
print("INTELLIGENT EQUIPMENT MONITORING")
print("=" * 40)

print("Student:", LAST_NAME)
print("Seed:", SEED_NUM)
print("Favorite Artist:", FAVORITE_ARTIST)

print("Generated Telemetry:", readings)
print("Valid Readings:", valid_readings)
print("Invalid Readings:", invalid_readings)
print("Processed Results:", processed)
print("Filtered Results:", filtered)
print("Average:", round(average, 2))
print("Abnormal Conditions:", abnormal_count)

if abnormal_count > 0:
    status = "Abnormal"
else:
    status = "Normal"

print("Overall Equipment Status:", status)
print("=" * 40)