from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    split = split_integer(32, 6)

    assert sum(split) == 32, (
        "The parts returned by split_integer(32, 6) should sum to 32"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    split = split_integer(6, 2)

    assert len(split) == 2 and split == [3, 3], (
        "The parts return by split_integer of (6, 2)"
        "should split into iqual parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    split = split_integer(8, 1)

    assert len(split) == 1, (
        "split_intefer of (8, 1) should split into one part"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5], (
        "The parts returned by split_integer(17, 4) should be sorted"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1], (
        "The function should add zerps when value es less than number of parts"
    )
