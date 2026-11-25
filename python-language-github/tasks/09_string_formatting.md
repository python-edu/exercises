# String formatting – tasks

Use only the material covered up to and including this chapter.

## Task 1. Accuracy report

An assessment gives an accuracy of 0.93758. Use an f-string to display `Accuracy: 93.76%`. Use `format()` to represent the same value with three decimal places. Show that formatting does not change the stored value.

## Task 2. Tile identifiers

A tile has row index 7 and column index 23. Use an f-string to generate `tile_r007_c023.tif` with three digits for each index. Reproduce the same name using `str.format()`.

## Task 3. Signed displacements

Two vertical displacements are 0.04321 m and -0.01876 m. Use f-strings to display both in millimetres with an explicit sign and one decimal place, followed by ` mm`.

## Task 4. Numeric presentation

A raster contains 12500000 pixels. A wavelength is 0.00000065 m. Use `format()` to display the pixel count with comma grouping and the wavelength in scientific notation with two digits after the decimal point. Display the class code 255 in hexadecimal with its `0x` prefix.

## Task 5. Aligned report

Create a two-column report using `str.format()`. Left-align the labels in a field of width 12 and right-align the values in a field of width 8 with two decimal places. Use the labels `Minimum` and `Maximum` and values 12.3 and 245.678. Reuse one format template.
