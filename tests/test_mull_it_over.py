import pytest

from challenges.day_03.mull_it_over import (
    filter_instructions,
    mul,
    scan,
    REGEX_MUL,
    REGEX_ENABLE
)


def test_mul():
    assert 8 == mul('mul(2,4)')


def test_mul_raises_TypeError():
    with pytest.raises(TypeError):
        mul('')


def test_get_instructions():
    memory = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    assert 161 == scan(memory, REGEX_MUL)


def test_get_instructions_nums_bigger_3_digits():
    memory = 'xmul(2,4321)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8765,5))'
    assert 113 == scan(memory, REGEX_MUL)


def test_regex():
    expected = r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)'
    assert expected == REGEX_ENABLE


def test_filter_instructions_simple():
    memory = 'xmul(2,4)&mul[3,7]!^dont()_mul(5,5)+mul(32,64](mul(11,8)undo(]?mul(8,5))'
    expected = ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']

    assert expected == list(filter_instructions(memory, REGEX_ENABLE))


def test_filter_instructions_enabled():
    memory = 'xmul(2,4)&mul[3,7]!^dont()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'
    expected = ['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']

    assert expected == list(filter_instructions(memory, REGEX_ENABLE))


def test_filter_instructions_disabled():
    memory = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo(]?mul(8,5))'
    assert ['mul(2,4)'] == list(filter_instructions(memory, REGEX_ENABLE))


def test_filter_instructions():
    memory = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'
    expected = ['mul(2,4)', 'mul(8,5)']

    assert expected == list(filter_instructions(memory, REGEX_ENABLE))
