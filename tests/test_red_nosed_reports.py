from challenges.day_02.red_nosed_reports import (
    is_safe,
    with_tolerance
)


def test_is_safe_empty():
    assert is_safe([]) == 1


def test_is_safe_duplicate():
    assert is_safe([1, 1]) == 0


def test_is_safe_big_step_asc():
    assert is_safe([1, 5]) == 0


def test_is_safe_big_step_desc():
    assert is_safe([10, 3]) == 0


def test_is_safe_asc_desc():
    assert is_safe([1, 4, 3, 2]) == 0


def test_is_safe_desc_asc():
    assert is_safe([4, 3, 5, 6]) == 0


def test_is_safe_back_and_forth():
    assert is_safe([1, 2, 1, 2, 1]) == 0


def test_is_safe_big_step_beginning():
    assert is_safe([1, 10, 11, 13, 14]) == 0


def test_is_safe_big_step_end():
    assert is_safe([10, 11, 13, 14, 25]) == 0


def test_with_tolerance_empty():
    assert with_tolerance([]) == 1


def test_with_tolerance_unsafe():
    assert with_tolerance([1, 2, 7, 8, 9]) == 0


def test_with_tolerance_safe_remove_duplicate():
    assert with_tolerance([8, 6, 4, 4, 1]) == 1


def test_with_tolerance_safe_remove_big_step():
    assert with_tolerance([1, 3, 2, 4, 5]) == 1


def test_with_tolerance_safe_remove_first():
    assert with_tolerance([10, 3, 5, 7, 8]) == 1


def test_with_tolerance_safe_remove_lastst():
    assert with_tolerance([1, 3, 5, 10]) == 1
