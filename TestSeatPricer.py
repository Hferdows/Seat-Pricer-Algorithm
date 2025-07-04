from SeatPricer import compute_seat_price  
import math

#theater configuration
total_rows = 10
total_cols = 12
base_price = 10.0

#test cases
test_cases = [
    {
        "name": "Best seat (front-center)",
        "row": 0,
        "col": 6,
        "expected_min": 10.5,
        "expected_max": 12.0
    },
    {
        "name": "Worst seat (back-left corner)",
        "row": 9,
        "col": 0,
        "expected_min": 7.5,
        "expected_max": 8.5
    },
    {
        "name": "Legroom seat (back-center)",
        "row": 9,
        "col": 6,
        "expected_min": 11.5,
        "expected_max": 13.5
    },
    {
        "name": "Aisle seat (middle-left)",
        "row": 5,
        "col": 0,
        "expected_min": 8.5,
        "expected_max": 10.5
    },
    {
        "name": "Off-center front seat",
        "row": 0,
        "col": 2,
        "expected_min": 8.0,
        "expected_max": 9.5
    }
]

def run_tests():
    passed = 0
    for test in test_cases:
        actual = compute_seat_price(
            row=test["row"],
            col=test["col"],
            total_rows=total_rows,
            total_cols=total_cols,
            base_p=base_price
        )

        print(f"Test: {test['name']}")
        print(f"Seat: row {test['row']}, col {test['col']}")
        print(f"Price: ${actual} (Expected: ${test['expected_min']} to ${test['expected_max']})")

        if test["expected_min"] <= actual <= test["expected_max"]:
            print("Passed\n")
            passed += 1
        else:
            print("Failed\n")

    print(f"{passed}/{len(test_cases)} tests passed.")

if __name__ == "__main__":
    run_tests()