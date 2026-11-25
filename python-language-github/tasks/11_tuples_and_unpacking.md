# Tuples and unpacking – tasks

Use only the material covered up to and including this chapter.

## Task 1. Image dimensions

Store the fixed dimensions of a raster (1,024 rows, 2,048 columns, 4 bands) as a tuple. Use unpacking to assign each dimension to a separate variable. Calculate the total number of samples. Extract the spatial dimensions as a tuple using slicing.

## Task 2. Coordinate displacement

Two points have coordinates `(450120, 5500200)` and `(450150, 5500240)` in metres. Unpack each point into coordinate variables. Pack the differences (second minus first) into a displacement tuple and calculate its length.

## Task 3. Fixed band configuration

Convert `['B02', 'B03', 'B04']` to a tuple. Create a new tuple by adding `B08` as a one-item tuple. Verify that the original tuple is unchanged. Convert the new tuple to a list.

## Task 4. Measurement record

A record is `('ST-03', 18.2, 18.4, 18.1)`. Use starred unpacking to assign the station ID to one variable and all measurements to another. Inspect the type of the measurements and calculate their mean rounded to two decimal places.

## Task 5. Coordinate order

A point is supplied in northing–easting order as `(5500200, 450120)`. Unpack it into two variables. Swap their values using simultaneous assignment and pack the result in easting–northing order. Separately, use `divmod()` and unpack its result to find the complete 256-pixel blocks and remaining pixels in a 1,050-pixel row.
