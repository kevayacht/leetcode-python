import pytest

from problems.running_sum import running_sum


@pytest.mark.parametrize(
    "set_input_1, set_output",
    (
            (  # test case 1
                    [1, 2, 3, 4],
                    [1, 3, 6, 10],
            ),
            (  # test case 2
                    [1, 1, 1, 1, 1],
                    [1, 2, 3, 4, 5],
            ),
            (  # test case 3
                    [3, 1, 2, 10, 1],
                    [3, 4, 6, 16, 17],
            ),
    )
)
def test_two_sum(set_input_1, set_output):
    result = running_sum(set_input_1)
    assert result == set_output
