# Combined exercises — exercises

> Topics: all previous sections. Choose variables, lists, and dictionaries to match the data. No loops, `if` statements, or user-defined functions.

### 1. Raster parameters.

Image `DEM_01` has `1500 × 1000` pixels, `5` m pixel size, and `4` bytes per pixel. Store metadata in one record. Calculate ground area in km² and raw pixel data size in MiB.

### 2. Station report.

Station `K01` records `[12.5, 13.0, 13.5]` °C. Add a new reading of `14.0` °C. Generate a report string containing the station code and mean temperature.

### 3. Related filenames.

Scene metadata contains satellite `S2A` and date `20260715`. Store both in one record. Generate image filename `S2A_20260715.tif` and mask filename `S2A_20260715_mask.tif`.

### 4. Samples and legend.

Sample class codes are `[1, 2, 2, 3, 2]`. The legend is `1: water`, `2: forest`, `3: urban`. Find the name of class `2` and count its samples.

### 5. RGB composite.

Band files are `B02 → scene_B02.tif`, `B03 → scene_B03.tif`, and `B04 → scene_B04.tif`. RGB channel order is `B04`, `B03`, `B02`. Create a list of filenames in R–G–B order.

### 6. Compare stations.

Station `A` records `[18, 20, 19]` °C; station `B` records `[15, 17, 16]` °C. Store both series under their station codes. Calculate the difference between mean temperatures (`A − B`).

### 7. Measurement log.

Measurements `M01` and `M02` have values `15.2` and `16.4`. Correct `M02` to `16.1`. Store ordered records with their own IDs. Check whether the corrected second value exceeds the first.

### 8. Image collection.

A collection contains `S2A_01` (`12%` cloud cover) and `S2A_02` (`35%`). Add `S2A_03` (`8%`). Keep each image's data together and preserve scene order. Count images and check whether the third has lower cloud cover than the first.

### 9. Image–mask pairs.

Image `A.tif` has mask `A_mask.tif` with classes `[1, 2]`. Image `B.tif` has mask `B_mask.tif` with classes `[1, 3]`. Store both as one collection of records. Add class `4` to the second pair only.

### 10. Classification project.

Project `landcover` contains images `S2A_01` and `S2A_02`, legend `{1: 'water', 2: 'forest'}`, and sample codes `[1, 2, 2, 1, 2]`. Store the project in one structure. Find the name of class `2`, its sample count, and the second image ID.
