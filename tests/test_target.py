import pytest
import target


# =====================================================
# 1. Test is_adult()
# =====================================================

@pytest.mark.parametrize(
    "age, expected",
    [
        (0, False),
        (1, False),
        (17, False),
        (18, True),
        (19, True),
        (100, True),
    ],
)
def test_is_adult_valid_ages(age, expected):
    assert target.is_adult(age) is expected


def test_is_adult_negative_age():
    with pytest.raises(ValueError, match="age cannot be negative"):
        target.is_adult(-1)


def test_is_adult_wrong_type():
    with pytest.raises(TypeError):
        target.is_adult("18")


# =====================================================
# 2. Test celsius_to_fahrenheit()
# =====================================================

@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (37, 98.6),
        (25.5, 77.9),
    ],
)
def test_celsius_to_fahrenheit(celsius, expected):
    result = target.celsius_to_fahrenheit(celsius)
    assert result == expected
    assert isinstance(result, float)


def test_celsius_to_fahrenheit_wrong_type():
    with pytest.raises(TypeError):
        target.celsius_to_fahrenheit("25")


# =====================================================
# 3. Test count_vowels()
# =====================================================

@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello", 2),
        ("AEIOU", 5),
        ("Python", 1),
        ("rhythm", 0),
        ("", 0),
        ("Education", 5),
        ("a e i o u", 5),
    ],
)
def test_count_vowels_valid(text, expected):
    assert target.count_vowels(text) == expected


def test_count_vowels_wrong_type():
    with pytest.raises(TypeError, match="text must be a string"):
        target.count_vowels(123)


# =====================================================
# 4. Test invert()
# =====================================================

@pytest.mark.parametrize(
    "flag, expected",
    [
        (True, False),
        (False, True),
    ],
)
def test_invert_valid(flag, expected):
    assert target.invert(flag) is expected


@pytest.mark.parametrize(
    "value",
    [1, 0, "True", None],
)
def test_invert_wrong_type(value):
    with pytest.raises(TypeError, match="flag must be True or False"):
        target.invert(value)


# =====================================================
# 5. Test greet()
# =====================================================

@pytest.mark.parametrize(
    "name, expected",
    [
        (None, "Hello, Guest!"),
        ("", "Hello, Guest!"),
        ("   ", "Hello, Guest!"),
        ("Sazzad", "Hello, Sazzad!"),
        ("  Rahman  ", "Hello, Rahman!"),
    ],
)
def test_greet_valid(name, expected):
    assert target.greet(name) == expected


def test_greet_wrong_type():
    with pytest.raises(AttributeError):
        target.greet(123)


# =====================================================
# 6. Test find_max()
# =====================================================

@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 3),
        ([-10, -5, -20], -5),
        ([7], 7),
        ([0, 0, 0], 0),
        ([1.5, 9.2, 3.4], 9.2),
    ],
)
def test_find_max_valid(numbers, expected):
    assert target.find_max(numbers) == expected


def test_find_max_empty_list():
    with pytest.raises(ValueError, match="list is empty"):
        target.find_max([])


def test_find_max_wrong_type():
    with pytest.raises(TypeError):
        target.find_max(None)


# =====================================================
# 7. Test get_price()
# =====================================================

def test_get_price_existing_item():
    prices = {"pen": 10, "book": 100}
    assert target.get_price(prices, "pen") == 10


def test_get_price_zero():
    assert target.get_price({"free": 0}, "free") == 0


def test_get_price_missing_item():
    with pytest.raises(KeyError, match="pencil not found"):
        target.get_price({"pen": 10}, "pencil")


def test_get_price_wrong_type():
    with pytest.raises(TypeError):
        target.get_price(None, "pen")


# =====================================================
# 8. Test swap()
# =====================================================

@pytest.mark.parametrize(
    "pair, expected",
    [
        ((1, 2), (2, 1)),
        (("a", "b"), ("b", "a")),
        ((None, 5), (5, None)),
        ((1, 1), (1, 1)),
        ([10, 20], (20, 10)),
    ],
)
def test_swap_valid(pair, expected):
    assert target.swap(pair) == expected


@pytest.mark.parametrize(
    "pair",
    [
        (),
        (1,),
        (1, 2, 3),
    ],
)
def test_swap_wrong_length(pair):
    with pytest.raises(ValueError, match="pair must have exactly 2 values"):
        target.swap(pair)


def test_swap_wrong_type():
    with pytest.raises(TypeError):
        target.swap(None)


# =====================================================
# 9. Test common_items()
# =====================================================

def test_common_items_with_overlap():
    assert target.common_items({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_common_items_no_overlap():
    assert target.common_items({1, 2}, {3, 4}) == set()


def test_common_items_identical_sets():
    assert target.common_items({1, 2}, {1, 2}) == {1, 2}


def test_common_items_empty_set():
    assert target.common_items(set(), {1, 2}) == set()


def test_common_items_wrong_type():
    with pytest.raises(TypeError):
        target.common_items([1, 2], {1, 2})


# =====================================================
# 10. Test is_leap_year()
# =====================================================

@pytest.mark.parametrize(
    "year, expected",
    [
        (1, False),
        (4, True),
        (100, False),
        (400, True),
        (1900, False),
        (2000, True),
        (2023, False),
        (2024, True),
        (2028, True),
    ],
)
def test_is_leap_year_valid(year, expected):
    assert target.is_leap_year(year) is expected


def test_is_leap_year_zero():
    with pytest.raises(ValueError, match="year must be 1 or more"):
        target.is_leap_year(0)


def test_is_leap_year_negative():
    with pytest.raises(ValueError, match="year must be 1 or more"):
        target.is_leap_year(-1)


def test_is_leap_year_wrong_type():
    with pytest.raises(TypeError):
        target.is_leap_year("2024")


# =====================================================
# 11. Test to_int()
# =====================================================

@pytest.mark.parametrize(
    "value, expected",
    [
        ("123", 123),
        ("-5", -5),
        (10.9, 10),
        (0, 0),
        ("0", 0),
    ],
)
def test_to_int_valid(value, expected):
    result = target.to_int(value)
    assert result == expected
    assert isinstance(result, int)


@pytest.mark.parametrize("value", [True, False])
def test_to_int_boolean(value):
    with pytest.raises(TypeError, match="bool is not allowed"):
        target.to_int(value)


def test_to_int_invalid_string():
    with pytest.raises(ValueError):
        target.to_int("hello")


def test_to_int_none():
    with pytest.raises(TypeError):
        target.to_int(None)


# =====================================================
# 12. Test divide()
# =====================================================

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5.0),
        (9, 3, 3.0),
        (-10, 2, -5.0),
        (10, -2, -5.0),
        (0, 5, 0.0),
        (1, 4, 0.25),
    ],
)
def test_divide_valid(a, b, expected):
    result = target.divide(a, b)
    assert result == expected
    assert isinstance(result, float)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="cannot divide by zero"):
        target.divide(10, 0)


def test_divide_wrong_type():
    with pytest.raises(TypeError):
        target.divide("10", 2)


# =====================================================
# 13. Test power()
# =====================================================

@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (2, 3, 8),
        (5, 0, 1),
        (10, 1, 10),
        (2, -1, 0.5),
        (-2, 2, 4),
        (-2, 3, -8),
        (0, 3, 0),
    ],
)
def test_power_valid(base, exponent, expected):
    assert target.power(base, exponent) == expected


def test_power_wrong_type():
    with pytest.raises(TypeError):
        target.power("2", 3)


# =====================================================
# 14. Test square_root()
# =====================================================

@pytest.mark.parametrize(
    "x, expected",
    [
        (0, 0.0),
        (1, 1.0),
        (4, 2.0),
        (9, 3.0),
        (2, 2 ** 0.5),
        (2.25, 1.5),
    ],
)
def test_square_root_valid(x, expected):
    assert target.square_root(x) == pytest.approx(expected)


def test_square_root_negative():
    with pytest.raises(
        ValueError,
        match="cannot take the square root of a negative number",
    ):
        target.square_root(-1)


def test_square_root_wrong_type():
    with pytest.raises(TypeError):
        target.square_root("4")


# =====================================================
# 15. Test factorial()
# =====================================================

@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (5, 120),
        (10, 3628800),
    ],
)
def test_factorial_valid(n, expected):
    assert target.factorial(n) == expected


def test_factorial_negative():
    with pytest.raises(
        ValueError,
        match="factorial is not defined for negative numbers",
    ):
        target.factorial(-1)


def test_factorial_wrong_type():
    with pytest.raises(TypeError):
        target.factorial(2.5)


# =====================================================
# 16. Test average()
# =====================================================

@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 2.0),
        ([10], 10.0),
        ([0, 0, 0], 0.0),
        ([-1, 0, 1], 0.0),
        ([1, 2], 1.5),
        ([1.5, 2.5], 2.0),
    ],
)
def test_average_valid(numbers, expected):
    assert target.average(numbers) == pytest.approx(expected)


def test_average_empty_list():
    with pytest.raises(ValueError, match="list is empty"):
        target.average([])


def test_average_wrong_type():
    with pytest.raises(TypeError):
        target.average([1, "two"])
