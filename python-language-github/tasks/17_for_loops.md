# For loops – tasks

Use only the material covered up to and including this chapter.

## Task 1. Sampling distances

Use `for` and `range()` to generate survey positions at 25 m intervals from 0 to 150 m inclusive. Print each distance with its unit. Then use a loop to print the return positions from 150 m down to 0 m.

## Task 2. Mean elevation error

The signed elevation errors in metres are `[-1.5, 0.5, 2.0, -1.0]`. Use a `for` loop and accumulators to calculate the mean signed error and mean absolute error. Do not use `sum()`.

## Task 3. Valid measurements

A raster sample contains `[-9999, 12, 15, -9999, 18, 20]`, where -9999 denotes missing data. Use a `for` loop with `continue` to skip missing values and append valid values to a new list. Calculate the mean of the valid values.

## Task 4. Numbered image report

Image IDs are `S2_A`, `S2_B` and `S2_C`. Use `enumerate()` with numbering from one to print `01: S2_A`, `02: S2_B` and `03: S2_C`. Separately, convert the list of pixel sizes `[10, 20, 60]` from metres to centimetres in place by iterating over its indices using `range()`.

## Task 5. Storage limit

A dictionary contains tile sizes in MiB in processing order: `{'T01': 120, 'T02': 180, 'T03': 250, 'T04': 90}`. Iterate over key–value pairs and add tiles to a list until the next tile would exceed a 500 MiB storage limit. Stop at that point using `break` (do not skip the tile and continue). Display the accepted IDs and occupied space.
