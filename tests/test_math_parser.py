import pytest
from ..math_parser import get_valid_pairs, convert_obsidian_math
from .test_cases import delimiter_pairing_tests

@pytest.mark.parametrize("case", delimiter_pairing_tests)
def test_delimiter_pairing(case):
    single, double = get_valid_pairs(case["input"])
    output = convert_obsidian_math(case["input"])
    assert single == case["expected_single_pairs"], f"FAIL (single): {case['description']}"
    assert double == case["expected_double_pairs"], f"FAIL (double): {case['description']}"
    assert output == case["output"], f"FAIL (double): {case['description']}"
