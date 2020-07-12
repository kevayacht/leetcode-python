import pytest

from problems.longest_substring import length_of_longest_substring


@pytest.mark.parametrize(
    "set_input_1, set_output",
    (
            (  # test case 1
                    "abcabcbb",
                    3,
            ),
            (  # test case 2
                    "bbbbb",
                    1,
            ),
            (  # test case 3
                    "pwwkew",
                    3,
            ),
            (  # test case 4,
                    "abcdefghijklmnopqrstuvwxyza",
                    26,
            ),
            (  # test case 5,
                    "abcdefg*()_a",
                    11,
            ),
            (  # test case 6
                    "aab",
                    2,
            ),
            (  # test case 6
                    "dvdf",
                    3,
            ),
            (  # test case 6
                    "ohvhjdml",
                    6,
            ),
    )  #
)
def test_two_sum(set_input_1, set_output):
    result = length_of_longest_substring(set_input_1)
    assert result == set_output
