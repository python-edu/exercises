# Dictionaries – tasks

Use only the material covered up to and including this chapter.

## Task 1. Class legend

Create a dictionary mapping class codes 1, 2 and 3 to `Water`, `Forest` and `Urban`. Retrieve the label for code 2, add code 4 for `Bare soil`, replace the label for code 3 with `Built-up`, and safely retrieve the label for code 9 using `Unknown` as the default.

## Task 2. Station measurements

Create a dictionary from station IDs `['ST01', 'ST02', 'ST03']` and heights `[120.5, 132.0, 128.5]` using `dict()` and `zip()` with strict length checking. Calculate the mean height from the dictionary values. Separately initialise a dictionary of measurement counts with zero for all three stations.

## Task 3. Processing settings

Default settings are `{'resolution': 10, 'format': 'tif', 'compression': 'none'}`. New settings are `{'resolution': 20, 'compression': 'lzw'}`. Combine them into a new dictionary using `|`. Verify the defaults are unchanged. Then update the defaults in place using `|=` and remove the compression entry with `.pop()`.

## Task 4. Live inventory

An inventory maps `tile01` to 12 and `tile02` to 18 (file sizes in MiB). Store a key view, a value view and a list snapshot of the keys. Add `tile03` with size 25 and replace the size of `tile01` with 15. Display both views and the snapshot; test whether size 25 is present among the values.

## Task 5. Sparse raster

Store pixel values 18, 24 and 31 at `(0, 0)`, `(0, 2)` and `(1, 1)` in a dictionary using tuple keys. Store this dictionary inside a metadata dictionary under `pixels`, together with the raster shape `(2, 3)`. Retrieve the value at `(0, 2)`, change it to 26 and safely retrieve `(1, 2)` with `None` as the default.
