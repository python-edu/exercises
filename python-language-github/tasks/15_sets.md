# Sets – tasks

Use only the material covered up to and including this chapter.

## Task 1. Unique class codes

A classified raster sample has codes `[2, 1, 2, 3, 1, 4, 4]`. Create a set of unique codes. Count the distinct classes. Test whether code 3 occurs and code 0 is absent.

## Task 2. Tile coverage

The first survey covers tiles `T01`, `T02`, `T03` and `T04`; the second covers `T03`, `T04` and `T05`. Use set operators to find the combined coverage, common tiles, tiles only in the first survey and tiles covered by exactly one survey.

## Task 3. Band availability

Available bands are `B02`, `B03`, `B04` and `B08`. An analysis requires `B04`, `B08` and `B11`. Test whether all required bands are available and identify the missing bands. Add `B11`, discard `B99` without raising an error, and repeat the availability test. Test whether the required bands and `B01`, `B02` have no elements in common.

## Task 4. Inventory comparison

Two inventories are `{'A': 10, 'B': 20, 'C': 30}` and `{'B': 25, 'C': 30, 'D': 40}`. Use set operations directly on dictionary views to find common IDs, IDs missing from the first inventory and identical ID–value pairs.

## Task 5. Unordered band combinations

Two processing configurations contain bands `['B04', 'B08']` and `['B08', 'B04']`. Convert both to immutable sets, test their equality and use them as keys in a dictionary. First assign `NDVI` to the first key, then assign `Vegetation index` to the second. Display the dictionary and count its entries.
