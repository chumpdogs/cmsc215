
"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

import time


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Check every item in order, beginning with index 0.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # In the worst case, we check all n items,
    # which gives linear search O(n) time complexity.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    # Start by setting the beginning and end of the list.
    left = 0
    right = len(lst) - 1

    # Continue searching while there are values left.
    while left <= right:

        # Find the middle position of the remaining list.
        middle = left + (right - left) // 2

        # Check whether we found the correct value.
        if lst[middle] == target:
            return middle

        elif lst[middle] < target:

            # The target is larger, so discard the lower half.
            left = middle + 1

        else:

            # The target is smaller, so discard the upper half.
            right = middle - 1

    # Dividing the search area in half each time
    # gives binary search O(log n) time complexity.
    return -1


def average_search_time(search_function, values, target, repetitions=100):
    """
    Measures how long each search algorithm takes.
    Repeating the search helps provide an average.
    """

    # Record the starting time.
    start = time.perf_counter()

    # Repeat the search to measure performance.
    for _ in range(repetitions):
        search_function(values, target)

    # Calculate how much time has passed.
    elapsed = time.perf_counter() - start

    # Return the average time in milliseconds.
    return elapsed * 1000 / repetitions


def main():

    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # Create a small sorted list of student scores.
    small_scores = [10, 15, 20, 35, 45, 55, 70, 81, 90, 95]

    # Search for 81, which exists, and 50, which does not.
    for target in [81, 50]:

        linear_result = linear_search(small_scores, target)
        binary_result = binary_search(small_scores, target)

        print(
            f"Score {target}: linear index = {linear_result}, "
            f"binary index = {binary_result}"
        )

        # Both methods should return the same index.
        # Missing scores should return -1.
        assert linear_result == binary_result

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # Create a larger sorted list containing 100,000 scores.
    large_scores = list(range(1, 100001))

    # Search for an existing value and a missing value.
    for target in [100000, 100001]:

        linear_result = linear_search(large_scores, target)
        binary_result = binary_search(large_scores, target)

        print(
            f"Score {target}: linear index = {linear_result}, "
            f"binary index = {binary_result}"
        )

        # Confirm that both methods return the same result.
        assert linear_result == binary_result

    # Linear search has to check every value to find
    # the last item in the list.

    # Binary search only checks a small number of values
    # because it eliminates half the list each time.

    # Compare the average execution time for both searches.
    linear_ms = average_search_time(
        linear_search, large_scores, 100000
    )

    binary_ms = average_search_time(
        binary_search, large_scores, 100000
    )

    print(f"Average linear search time: {linear_ms:.4f} ms")
    print(f"Average binary search time: {binary_ms:.4f} ms")

    print(
        "Binary search is faster here because it cuts "
        "the sorted list in half each step."
    )

    print(
        "Timing depends on the computer; "
        "the results are only an example."
    )

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Test several situations where searches might fail
    # or where the values are at the boundaries.
    edge_cases = [
        ("Empty list", [], 81, -1),
        ("One item, found", [81], 81, 0),
        ("One item, missing", [81], 90, -1),
        ("First position", [10, 20, 30], 10, 0),
        ("Last position", [10, 20, 30], 30, 2),
    ]

    # Run both algorithms against each edge case.
    for description, scores, target, expected in edge_cases:

        linear_result = linear_search(scores, target)
        binary_result = binary_search(scores, target)

        # Verify both searches return the expected result.
        assert linear_result == expected
        assert binary_result == expected

        print(
            f"{description}: linear = {linear_result}, "
            f"binary = {binary_result} (expected {expected})"
        )

    # Empty lists and missing values return -1.
    # Single-element lists return index 0 when found.
    # First and last positions are also handled correctly.

    print("All edge case tests passed.")


if __name__ == "__main__":
    main()
