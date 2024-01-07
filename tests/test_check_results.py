import numpy as np
import pytest

from speed_benchmark.speed_benchmark import check_results


@pytest.mark.parametrize(
    "x, y, expected_result",
    [
        (5, "5", False),  # x and y are of different types
        ((1, 2, 3), (1, 2), False),  # x and y are tuples of different lengths
        (
            {"a": 1, "b": 2},
            {"a": 1, "c": 3},
            False,
        ),  # x and y are dictionaries with different keys
        (
            np.array([1, 2, 3]),
            np.array([1, 2, 4]),
            False,
        ),  # x and y are numpy arrays with different values
        (0.1, 0.2, False),  # x and y are floats with different values
        (5, 5, True),  # x and y are equal
    ],
)
def test_check_results_parametrized(x, y, expected_result):
    assert check_results(x, y) == expected_result
