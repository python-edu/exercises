# Comparison and logical operators – tasks

Use only the material covered up to and including this chapter.

Use Boolean expressions, not conditional statements or loops.

## Task 1. Image selection

An image has 18% cloud cover and a 20 m pixel size. Assign a Boolean result indicating whether it meets both requirements: cloud cover at most 20% and pixel size at most 10 m. Test again after changing the pixel size to 10 m.

## Task 2. Valid slope

A slope measurement is 90°. Test whether it is in the physically valid range from 0° to 90°, inclusive, using a chained comparison. Test whether it is strictly between 5° and 30°. Negate the first comparison to detect an invalid slope.

## Task 3. Survey eligibility

A scene is eligible if it is from Sentinel-2 or Landsat-9 and has less than 10% cloud cover. Store `Sentinel-2` and 15% cloud cover. Write a single Boolean expression using parentheses. Repeat with 5% cloud cover.

## Task 4. Safe division and missing data

A reflectance ratio is usable if the denominator is nonzero and the ratio is greater than 2. Use short-circuit evaluation to test a numerator of 0.6 and denominator of 0. Test again with denominator 0.2. Separately, set a measurement to `None` and test whether it is missing using identity.

## Task 5. Measurement tolerance

Two displacements of 0.1 m and 0.2 m should total 0.3 m. Compare the calculated sum with 0.3 using `==`. Then test whether the absolute difference is within 0.000001 m. Separately, use `or` to select a fallback value of 10 when a stored numeric value is 0, and explain why this is not a valid missing-data test if zero is meaningful.
