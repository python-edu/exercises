# Basic built-in functions – tasks

Use only the material covered up to and including this chapter.

## Task 1. Measurement report

Store a station ID `ST-12` and an elevation of 284.5 m. Use `print()` to display `ST-12: 284.5 m` using `sep` and `end` (do not use string formatting).

## Task 2. Text measurements

The row count is supplied as text `2048` and the pixel size as text `0.25`. Convert them to an integer and a float. Calculate the image height in metres. Convert the result to text and inspect its type.

## Task 3. Boolean conversion

A sensor reports the values `0`, `-9999`, `None`, an empty string and the text `False`. Convert each value to a Boolean using `bool()`. Explain why the text `False` and the missing-data code -9999 both produce true.

## Task 4. Elevation error

A DEM reports an elevation of 217.384 m, while a reference measurement is 219.125 m. Calculate the signed error (DEM minus reference) to three decimal places, the absolute error rounded to two decimal places, and the squared error rounded to three decimal places using `pow()`.

## Task 5. Grid blocks and integer conversion

A raster line contains 2,590 pixels. Use `divmod()` to determine the number of full 256-pixel blocks and remaining pixels. Then use `int()` and `round()` separately on each of the values 12.5 and -13.5 to compare truncation and rounding.
