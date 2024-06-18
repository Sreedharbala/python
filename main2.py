# import json
# from collections import Counter
# from typing import List, Tuple
#
#
# def load_data(filename: str) -> List[int]:
#     """Load a list of integers from a JSON file."""
#     # TODO: Implement loading the list of numbers from a JSON file named `filename`.
#     with open('C://Users//Lenovo//Desktop//filename', 'r') as file:
#         data = json.load(file)
#         return data['integers']
#
#
# def calculate_frequency(numbers: List[int]) -> List[Tuple[int, int]]:
#     """Calculate the frequency of each unique number and return sorted by frequency descending."""
#     # TODO: Use collections.Counter to calculate frequency and sort by frequency (descending).
#     counter = Counter(numbers)
#     return sorted(counter.items(), key=lambda x: x[1], reverse=True)
#
#
# def get_third_highest_frequency(frequencies: List[Tuple[int, int]]) -> Tuple[int, int]:
#     """Retrieve the third highest frequency from the list of (number, frequency) tuples."""
#     # TODO: Implement logic to find the third highest frequency or handle case with less unique numbers.
#     if len(frequencies) < 3:
#         return None, None
#     return frequencies[2]
#
# def save_output(data: dict, filename: str) -> None:
#     """Save the given data as JSON in a file."""
#     # TODO: Implement saving the data to a JSON file named `filename`.
#     with open('C://Users//Lenovo//Desktop//filename', 'w') as file:
#         json.dump(data, file, indent=4)
#
# def main():
#     numbers = load_data('filename')
#     frequencies = calculate_frequency(numbers)
#     third_highest_freq = get_third_highest_frequency(frequencies)
#
#     output = {
#         "sorted_frequency_distribution": frequencies,
#         "third_highest_frequency": third_highest_freq
#     }
#
#     save_output(output, 'output.json')
#
#     print("Output saved to output.json")
#
#
# if __name__ == "__main__":
#     main()


import json
from collections import Counter
from typing import List, Tuple


def load_data(filename: str) -> List[int]:
    """Load a list of integers from a JSON file."""
    try:
        with open('C://Users//Lenovo//Desktop//filename', 'r') as file:
            data = json.load(file)
            return data['integers']
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{filename}'.")
        return []


def calculate_frequency(numbers: List[int]) -> List[Tuple[int, int]]:
    """Calculate the frequency of each unique number and return sorted by frequency descending."""
    counter = Counter(numbers)
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)


def get_third_highest_frequency(frequencies: List[Tuple[int, int]]) -> Tuple[int, int]:
    """Retrieve the third highest frequency from the list of (number, frequency) tuples."""
    if len(frequencies) < 3:
        return None, None
    return frequencies[2]


def save_output(data: dict, filename: str) -> None:
    """Save the given data as JSON in a file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    input_filename = 'C://Users//Lenovo//Desktop//filename'  # Change this to the actual filename
    output_filename = 'output.json'  # Output filename

    numbers = load_data('filename')
    frequencies = calculate_frequency(numbers)
    third_highest_freq = get_third_highest_frequency(frequencies)

    output = {
        "sorted_frequency_distribution": frequencies,
        "third_highest_frequency": third_highest_freq
    }

    save_output(output, output_filename)

    print("Output saved to", output_filename)


if __name__ == "__main__":
    main()