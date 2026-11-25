"""Part 10: your own tests for parse_walk. The README says what to write here.

We grade this file by running it against a correct walks.py, where every test must pass,
and against versions of walks.py with a bug planted in parse_walk, where your tests should fail.
"""

import pytest

from walks import Walk, parse_walk


@pytest.fixture
def good_row() -> dict[str, str]:
    """Provided: one good row, as csv.DictReader gives it. Each test gets its own new copy."""
    return {"date": "2026-11-16", "steps": "4200", "place": "Lumphini Park"}


def test_core_example_a_good_row_becomes_a_walk(good_row):
    """Provided: an example that uses the fixture. Write your own tests below it."""
    assert parse_walk(good_row) == Walk("2026-11-16", 4200, "Lumphini Park")


# Your tests go here.
def test_parse_walk_strips_spaces_around_date_steps_and_place(good_row):
    good_row.update(date=" 2026-11-16 ", steps=" 3100 ", place=" campus ")
    assert parse_walk(good_row) == Walk("2026-11-16", 3100, "campus")


def test_parse_walk_does_not_change_the_row(good_row):
    good_row["place"] = " campus "
    before = dict(good_row)
    parse_walk(good_row)
    assert good_row == before


def test_parse_walk_steps_are_an_int(good_row):
    assert type(parse_walk(good_row).steps) is int


def test_parse_walk_accepts_zero_steps(good_row):
    good_row["steps"] = "0"
    assert parse_walk(good_row).steps == 0


def test_parse_walk_rejects_minus_one_step(good_row):
    good_row["steps"] = "-1"
    with pytest.raises(ValueError):
        parse_walk(good_row)


def test_parse_walk_accepts_one_step(good_row):
    good_row["steps"] = "1"
    assert parse_walk(good_row).steps == 1


@pytest.mark.parametrize("steps", ["", "   ", "abc", "12.5", "-300", "-1", "1e3", "4 200"])
def test_parse_walk_rejects_bad_steps(good_row, steps):
    good_row["steps"] = steps
    with pytest.raises(ValueError):
        parse_walk(good_row)


@pytest.mark.parametrize("date", ["", " ", "   "])
def test_parse_walk_rejects_an_empty_date(good_row, date):
    good_row["date"] = date
    with pytest.raises(ValueError):
        parse_walk(good_row)


def test_parse_walk_accepts_an_empty_place(good_row):
    good_row["place"] = ""
    assert parse_walk(good_row).place == ""
