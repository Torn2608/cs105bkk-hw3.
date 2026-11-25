# HW3 notes

Answer each question in a few sentences. Be specific: name the function, the error or the command.

## What did you try?

 For part 10 I wrote tests for `parse_walk` that use the `good_row` fixture, including `@pytest.mark.parametrize` tests with `pytest.raises(ValueError)`.

## What broke, and how did you fix it?

 In `saved_safely` I close the `.tmp` file before calling `unlink()` or `replace()`, because deleting or renaming an open file fails on Windows. In `write_report` I call `best_day` before opening the file, so an empty week raises `ValueError` .

## What would you do differently next time?

I would run the tests after each function. I would also run my own tests against a deliberately broken `parse_walk` (for example, changing `< 0` to `<= 0`) to check that at least one test fails.
