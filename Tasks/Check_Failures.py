from collections import defaultdict
from sys import stdin
from typing import Dict, List, Tuple

# Index constants
SERIAL_NUM_INDEX = 0
HW_REVISION_INDEX = 1
FW_VERSION_INDEX = 2
LOCATION_INDEX = 3
DAYS_INDEX = 4
FAILURES_INDEX = 5

# Output constants
HW_REVISION_OUTPUT = "Hardware Revision"
FW_VERSION_OUTPUT = "Firmware Version"
LOCATION_OUTPUT = "Location"
NO_FAILURES_OUTPUT = "No failures"


def process_input_data(input_lines: List[str]) -> List[Tuple[str, str, str, str, int, int]]:
    data = []
    seen_serial_numbers = set()

    for line in input_lines:
        parts = [item.strip() for item in line.split(",")]

        serial_number = parts[SERIAL_NUM_INDEX]
        hw_revision = parts[HW_REVISION_INDEX]
        fw_version = parts[FW_VERSION_INDEX]
        location = parts[LOCATION_INDEX].lower()
        days_deployed = int(parts[DAYS_INDEX])
        number_failures = int(parts[FAILURES_INDEX]) if parts[FAILURES_INDEX] else 0

        # Filtering duplicated data
        if serial_number in seen_serial_numbers:
            continue
        seen_serial_numbers.add(serial_number)

        if days_deployed <= 0:
            continue

        data.append((serial_number, hw_revision, fw_version, location, days_deployed, number_failures))

    return data


def calculate_average_failures(data: List[Tuple[str, str, str, str, int, int]]) -> Tuple[Dict[str, float], Dict[str, float], Dict[str, float]]:
    hw_failures = defaultdict(lambda: [0, 0])  # type: Dict[str, List[int]]
    fw_failures = defaultdict(lambda: [0, 0])  # type: Dict[str, List[int]]
    loc_failures = defaultdict(lambda: [0, 0])  # type: Dict[str, List[int]]

    for entry in data:
        _, hw_revision, fw_version, location, days_deployed, number_failures = entry

        hw_failures[hw_revision][0] += number_failures
        hw_failures[hw_revision][1] += days_deployed

        fw_failures[fw_version][0] += number_failures
        fw_failures[fw_version][1] += days_deployed

        loc_failures[location][0] += number_failures
        loc_failures[location][1] += days_deployed

    avg_hw_failures = {k: v[0] / v[1] for k, v in hw_failures.items()}
    avg_fw_failures = {k: v[0] / v[1] for k, v in fw_failures.items()}
    avg_loc_failures = {k: v[0] / v[1] for k, v in loc_failures.items()}

    return avg_hw_failures, avg_fw_failures, avg_loc_failures


def find_highest_failures(avg_hw_failures: Dict[str, float], avg_fw_failures: Dict[str, float], avg_loc_failures: Dict[str, float]) -> List[Tuple[str, str]]:
    max_failures = -1
    max_properties = []

    for property_dict, name in [(avg_hw_failures, HW_REVISION_OUTPUT), (avg_fw_failures, FW_VERSION_OUTPUT), (avg_loc_failures, LOCATION_OUTPUT)]:
        for prop, avg_fail in property_dict.items():
            if avg_fail > max_failures:
                max_failures = avg_fail
                max_properties = [(name, prop)]
            elif avg_fail == max_failures:
                max_properties.append((name, prop))

    return max_properties


def main(input_lines: List[str]) -> None:

    # Filtering form duplication and converting into list of tuples
    data = process_input_data(input_lines)

    # Checking if data exist and valid
    if not data or all(entry[FAILURES_INDEX] == 0 for entry in data):
        print(NO_FAILURES_OUTPUT)
        return

    avg_hw_failures, avg_fw_failures, avg_loc_failures = calculate_average_failures(data)
    max_properties = find_highest_failures(avg_hw_failures, avg_fw_failures, avg_loc_failures)

    if not max_properties:
        print(NO_FAILURES_OUTPUT)
    else:
        for prop in max_properties:
            print(f"{prop[0]} {prop[1].title()}")


# input_lines: List[str] = []
# for line in stdin:
#    input_lines.append(line.strip())







input_lines = [
    "12121212, Rev1, 0.4.1, Saskatoon, 100, 50",
    "16234677, Rev2, 0.1, Saskatoon, 100, 200",
    "12345, Rev2, 0.4.1, SASKATOON, 5, 200",
    "88642, Rev3, 0.1, Vancouver, 1500, 50",
    "561215, Rev3, 0.1, Saskatoon, 100, 100",
    "1268568121, Rev2, 2.0, Vancouver, 3000, 50",
    "212477, Rev1, 0.3, SASKATOON, 300, 100",
    "DE52123A, Rev3, 2.3, Vancouver, 3000, 50",
    "ABC456, R0.1, 0.3, Saskatoon, 500, 500",
    "AC563AH85H, R0.1, 2.3, SASKATOON, 100, 100",
    "113672B, R0.1, 0.3, Vancouver, 3000, 100",
    "7752267SK, R0.1, 2.3, Vancouver, 3005, 100",
    "99785YY, Rev1, 0.4.1, SASKATOON, 250, 100",
    "KT19A6AJ76, Rev1, 0.4.1, Vancouver, 100, 1",
    "QW661AABBCC, Rev3, 0.4.1, Saskatoon, 250, 100",
    "AHTERWWA12, Rev1, 2.0, Vancouver, 50, 0",
    "8856412, Rev1, 2.3, Saskatoon, 600, 500",
    "118822, Rev3, 2.0, SASKATOON, 600, 100",
    "42342882LK, R0.1, 0.1, Saskatoon, 125, 75",
]

main(input_lines)








