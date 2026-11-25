# Hashable objects – tasks

Use only the material covered up to and including this chapter.

## Task 1. Hashable measurement values

Inspect whether the following values can be hashed: `42`, `42.0`, `True`, `None`, and `ST-01` as a string. Use `hash()` on each value and test that repeated hashing of the same value gives an equal result. Do not record the numeric string hash as an identifier.

## Task 2. Equal numeric values

Test whether the class code `5` and numeric value `5.0` are equal. Compare their hashes. Repeat for `1` and `True`. Explain the relationship between equality and hashing.

## Task 3. Pixel coordinates

Pixel coordinates are initially stored in a list `[12, 35]`. Try to hash the list and identify the error. Convert the list to a tuple and verify that its hash equals the hash of `(12, 35)`.

## Task 4. Nested records

Consider the records `('ST01', (450120, 5500240))` and `('ST01', [450120, 5500240])`. Test their hashability. Change the second record into a hashable structure without changing its coordinate values.

## Task 5. Stable identifiers

Two records have the same station ID `ST-14` and coordinate tuple `(12, 8)`. Construct an identifier from the station ID and coordinates using a tuple. Verify equality and equal hashes for independently constructed identifiers. Which should be saved in a file as a persistent identifier: the tuple or its numeric hash?
