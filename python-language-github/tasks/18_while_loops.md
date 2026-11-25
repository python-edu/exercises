# While loops – tasks

Use only the material covered up to and including this chapter.

## Task 1. Battery reserve

A UAV starts with 100% battery. Its battery level decreases by 7 percentage points per minute. Use a `while` loop to count whole minutes until the level first reaches or falls below 30%. Display the elapsed time and remaining battery level.

## Task 2. Image pyramid

An image is 4,096 pixels wide. Each pyramid level halves its width using integer division. Use a `while` loop to generate the widths of successive reduced levels until the width is at most 256 pixels. Store them in a list (exclude the original width). Display the list and number of reduced levels.

## Task 3. Successive approximation

Approximate the square root of 10 using the iteration `x_new = (x + 10 / x) / 2`. Start with `x = 10.0`. Use a `while` loop to repeat the update while the absolute difference between `x ** 2` and 10 exceeds 0.000001. Count the updates and display the approximation rounded to six decimal places.

## Task 4. Processing attempts

Processing attempts are numbered from 1 to 8. Attempt numbers divisible by 3 must be skipped. Use a `while` loop with `continue` to print only the remaining attempt numbers. Update the counter before testing whether an attempt should be skipped.

## Task 5. First acceptable observation

A series of cloud-cover observations is `[85, 70, 40, 15, 5]` percent. Use a `while` loop with an index and `break` to find the first observation at or below 20%. Stop safely if the list is exhausted. Display the index and value, or `None` for both if no observation qualifies. Repeat with `[85, 70]`.
