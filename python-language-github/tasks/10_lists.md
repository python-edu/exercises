# Lists – tasks

Use only the material covered up to and including this chapter.

## Task 1. Sampling positions

Create a list of station indices from 1 to 6 using `range()` and `list()`. Extract the first three indices, the last two indices and every second index starting at the first. Display the list in reverse order without changing it.

## Task 2. Band selection

Start with `['B02', 'B03', 'B04']`. Append `B08`, insert `B01` at the beginning, extend the list with `B11` and `B12`, then remove `B03`. Remove and return the last band with `.pop()`. Display the final list.

## Task 3. Temperature measurements

Store the measurements 12.5, 14.0, 11.5, 14.0 and 13.0 °C in a list. Calculate their minimum, maximum and mean. Count the occurrences of 14.0 and find its first index. Create a sorted list without changing the original.

## Task 4. Raster row correction

Represent a two-row raster with `[[12, 15, 18], [20, 25, 30]]`. Read the pixel in the second row and third column. Replace the middle pixel of the first row with 16. Replace the last two pixels of the second row with 24 and 28 using slice assignment. Display the corrected raster.

## Task 5. Independent calibration values

Start with `[1.0, 1.1, 0.9]`. Assign it to a second variable and create a separate copy in a third variable. Change the first value through the second variable to 1.2. Compare the three lists. Sort the copy in place, then reverse it and display it.
