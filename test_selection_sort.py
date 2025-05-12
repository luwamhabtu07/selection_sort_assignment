from selection_sort import selection_sort

def run_tests():
    test_cases = [
        {"name": "Random array", "input": [64, 25, 12, 22, 11]},
        {"name": "Already sorted", "input": [1, 2, 3, 4, 5]},
        {"name": "Descending order", "input": [5, 4, 3, 2, 1]},
        {"name": "All elements same", "input": [7, 7, 7, 7, 7]},
        {"name": "Empty array", "input": []},
        {"name": "Single element", "input": [42]}
    ]

    for case in test_cases:
        original = case["input"]
        result = selection_sort(original.copy())
        print(f"{case['name']}:\n  Input: {original}\n  Output: {result}\n")

if __name__ == "__main__":
    run_tests()
