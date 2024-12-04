import pytest

from challenges.day_03.mull_it_over import (
    mul,
    scan,
    REGEX,
)


def test_mul():
    assert 8 == mul('mul(2,4)')


def test_mul_raises_TypeError():
    with pytest.raises(TypeError):
        mul('')


def test_get_instructions():
    memory = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    assert 161 == scan(memory, REGEX)


def test_get_instructions_nums_bigger_3_digits():
    memory = 'xmul(2,4321)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8765,5))'
    assert 113 == scan(memory, REGEX)
