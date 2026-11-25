# Conditional statements and expressions – tasks

Use only the material covered up to and including this chapter.

## Task 1. Image acceptance

An image is accepted if its cloud cover is at most 20% and its pixel size is at most 10 m. Use `if ... else` to print `Accepted` or `Rejected`. Test the code with cloud cover of 20% and pixel size of 10 m, then change the pixel size to 20 m and test again.

## Task 2. Slope classification

Use `if ... elif ... else` to assign a slope class: `Invalid` outside 0–90°, `Gentle` below 10°, `Moderate` from 10° to below 30°, and `Steep` from 30° to 90°. Use 30° as the test value. Repeat with -2° to verify the invalid case.

## Task 3. Independent quality flags

A DEM has a vertical error of 2.5 m and 12% missing pixels. Print a warning if the absolute vertical error exceeds 2 m, and a separate warning if missing pixels exceed 10%. Use independent `if` statements so that both warnings can appear. Test the given data.

## Task 4. Safe spectral index

Calculate NDVI using `(nir - red) / (nir + red)` only when the denominator is nonzero. Otherwise assign `None`. Use a conditional expression and test it with reflectances 0.6 and 0.2, then with both equal to zero. Display the results, rounding the valid result to three decimal places.

## Task 5. Product dispatch

Use `match ... case` to select a processing action based on a product code. `DEM` and `DSM` select `Elevation analysis`, `RGB` selects `Colour composite`, and any other code selects `Unsupported product`. Use an alternative pattern for DEM and DSM. Test with `DSM` and then with `SAR`.
