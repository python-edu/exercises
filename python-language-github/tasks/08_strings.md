# Strings – tasks

Use only the material covered up to and including this chapter.

## Task 1. File identifier

Create the string `S2_20261125_B08.tif`. Use indexing and slicing to extract the first character, the date `20261125`, the band `B08` and the extension `.tif`. Calculate the string length.

## Task 2. Windows path

Represent `C:\new\tiles\dem.tif` as an ordinary string with escaped backslashes and as a raw string. Print both paths and test whether they are equal.

## Task 3. Metadata lines

Use one string literal with escape sequences to display the following two lines, with a tab between each label and its value: `Sensor` / `Landsat-9` and `Band` / `B05`. Create the same text using a triple-quoted string with tab escapes and compare the strings.

## Task 4. Standardising labels

A band label is stored as `  nir  ` (two spaces at each end). Remove surrounding spaces and convert it to uppercase. Use the result to create `B08_NIR.tif` by concatenation. Test whether the file name begins with `B08`, ends with `.tif` and contains `NIR`.

## Task 5. Revising a file name

Given `tile_07_raw.tif`, create `tile_07_mask.tif` by replacing `raw` with `mask`, keeping the original unchanged. Use repetition to display a separator of 16 hyphens, then print the new file name. Show that the original string is unchanged.
