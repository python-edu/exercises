# Python intro — exercises

Work in the `python` or `ipython` console. Type commands yourself. Run them one at a time. Check results in the console.

Do not use loops, `if` statements, user-defined functions, or external libraries. Use only the Python features introduced so far.

## 1. Arithmetic operators — 10 exercises

**Topics:** `+`, `-`, `*`, `/`, `//`, `%`, `**`, parentheses. **Do not use variables.**

1. **Recording time.** A recording lasts `367` minutes. How many full hours and remaining minutes is that?
2. **Pixel count.** An image has `1024` columns and `768` rows. Calculate the number of pixels.
3. **Raster size.** A single-band image has `1200 × 800` pixels. Each pixel uses `2` bytes. Calculate its size in bytes and MiB (`1 MiB = 1024²` bytes).
4. **Photo storage.** An archive contains `487` photos. One disc holds `24` photos. How many full discs can be filled? How many photos remain?
5. **Ground area.** A square raster has `4096 × 4096` pixels. Pixel size is `0.5` m. Calculate the ground area in hectares (`1 ha = 10,000 m²`).
6. **Sensor values.** A sensor stores unsigned `12`-bit values. How many distinct values are possible? What is the maximum value?
7. **Mean rainfall.** Five rainfall measurements are `12`, `19`, `11`, `17`, and `21` mm. Calculate the mean.
8. **Percentage increase.** The number of detected objects increased from `80` to `92`. Calculate the percentage increase relative to the original value.
9. **Map distance.** A distance of `7.6` cm is measured on a map at scale `1:25,000`. Calculate the ground distance in kilometres.
10. **End time.** Recording starts at `22:45` and lasts `155` minutes. Calculate the end hour and minute, including the change to the next day.

## 2. Variables and assignment — 10 exercises

**Topics:** variables, `=`, reassignment, `+=`, `-=`, `*=`, calculations using variable names. Use clear names for inputs and results.

1. **Image dimensions.** An image changes from `800 × 600` to `1200 × 900` pixels. Calculate both pixel counts using the same dimension variables and the same formula.
2. **Raster resolution.** A raster has `650` columns, `400` rows, and `10` m pixels. Calculate its ground area in km². Recalculate for `20` m pixels.
3. **Disk usage.** A disk contains `250` GiB of data. Another `18` GiB and `12` GiB are added. Then `5` GiB are deleted. Calculate the final usage.
4. **Equipment budget.** A laboratory has a budget of `3000` PLN. A camera costs `640` PLN, a disk `780` PLN, and a monitor `1150` PLN. Calculate the remaining budget.
5. **Sensor calibration.** A sensor reports a height of `182.4` m. Its positive systematic error is `1.8` m. Calculate the corrected height. The estimated error is then changed to `1.2` m. Recalculate without changing the original measurement.
6. **Travel time.** A route is `42` km long. Calculate travel time at `56` km/h and `70` km/h. How many hours are saved?
7. **Coordinate correction.** A point has coordinates `x = 423500` m and `y = 5547900` m. Corrections are `+12.5` m for `x` and `-8` m for `y`. Calculate corrected coordinates. Change the `x` correction to `+13` m and update the result.
8. **Sampling plan.** A team collects `32` samples per day. Calculate the total for `7` days. Recalculate for a `5`-day campaign.
9. **Multiband image.** An image has `1000` columns, `800` rows, `3` bands, and `2` bytes per pixel per band. Calculate the size in MiB. Recalculate after adding a fourth band.
10. **Stored result.** A square plot has a side length of `35` m. Store its area in a separate variable. Change the side length to `40` m. Check the stored area, then update it.

## 3. Numeric types and conversions — 5 exercises

**Topics:** `int`, `float`, `type()`, `int()`, `float()`, `round()`.

1. **Sampling rate.** A recorder collects `36` samples in `8` seconds. Store the sample count and time as integers. Calculate samples per second and check the result type.
2. **Pixel indices.** Image coordinates are column `125.9` and row `88.4`. Pixel indices must be integers. Convert both values with `int()`. Calculate the discarded fractional parts.
3. **Height correction.** An integer height is `275` m. Add a correction of `0.75` m. Check the types of the original height, correction, and result.
4. **Height report.** A height measurement is `129.7` m. A report needs whole metres. Compare `int()` and `round()`.
5. **Decimal precision.** Add `0.1` and `0.2`. Inspect the result in the console. Store a result rounded to one decimal place.

## 4. Comparisons and Boolean values — 5 exercises

**Topics:** `<`, `<=`, `>`, `>=`, `==`, `!=`, `and`, `or`, `not`. Store each check as `True` or `False`. Do not use `if`.

1. **Image quality.** An image has `18%` cloud cover and `10` m resolution. Accept it only if cloud cover is at most `20%` **and** pixel size is at most `10` m. Check whether it passes.
2. **Sensor range.** A sensor works from `-40` to `60` °C, including both limits. Check readings of `-40` °C and `61` °C.
3. **Valid measurement.** The value `-9999` means missing data. A valid humidity reading must be different from `-9999` and within `0–100%`. Check `-9999` and `87` separately.
4. **Image rejection.** Reject an image if cloud cover exceeds `70%` **or** the camera angle exceeds `30` degrees. For `45%` cloud cover and a `34`-degree angle, check both rejection and acceptance.
5. **Manual approval.** Accept an image if cloud cover is at most `20%` and pixel size is at most `10` m. Manual approval can also allow the image. Check `35%` cloud cover, `10` m pixels, and manual approval granted.

## 5. Strings (`str`) — 10 exercises

**Topics:** string concatenation, `str()`, indexing, slicing, `len()`, `in`, `strip()`, `lower()`, `replace()`, `count()`, `endswith()`.

1. **Scene filename.** Satellite ID is `S2A`. Acquisition date is the string `20260715`. Build the filename `S2A_20260715.tif`.
2. **Station code.** A database contains `'  KrK-03  '`. Convert it to `krk-03`: no surrounding spaces, lowercase only.
3. **Mask filename.** An image is named `scene_07.tif`. Generate the corresponding filename `scene_07_mask.tif` from the image filename.
4. **Date from filename.** Filenames use the format `S2A_20260715_B04.tif`. Extract the eight-digit date.
5. **TIFF extension.** Only TIFF files are accepted. Check whether `DSM_5M.TIF` has the `.tif` extension, ignoring case.
6. **Station label.** Region code is `KRK`, and station number is the integer `12`. Build `KRK-12`.
7. **Remove prefix.** A filename is `raw_dem_10m.tif`. Generate `dem_10m.tif`.
8. **Count occurrences.** A report line is `cloud,cloud,clear,cloud`. Count occurrences of `cloud`.
9. **Check scene ID.** The filename `S2A_20260715_B04.tif` must contain satellite ID `S2A` and band ID `B04`. Check both conditions.
10. **Code length.** The maximum allowed identifier length is `20` characters. Check `S2A_20260715_B04`.

## 6. Lists (`list`) — 10 exercises

**Topics:** list elements, indexing, slicing, `append()`, `extend()`, `pop()`, `+`, `copy()`, `len()`, `sum()`, `min()`, `max()`, `sorted()`, `count()`, `in`.

1. **Temperature series.** Six hourly temperatures are `15.2`, `13.8`, `16.1`, `14.0`, `15.7`, and `16.4` °C. Store the series in one object. Calculate the mean without adding each value manually.
2. **New measurement batch.** Recorded rainfall values are `[3, 0, 7, 2]` mm. A new batch contains `[5, 4]` mm. Add the new readings to the existing main series. Calculate total rainfall.
3. **Correct a reading.** A temperature series is `[12.1, 13.5, -9999, 14.2, 13.8]`. The third value is corrected to `13.7`. Update the series and calculate the mean.
4. **Remove an invalid reading.** The final value in `[7.2, 7.4, 7.3, -9999]` is invalid. Remove it from the existing series and calculate the mean.
5. **Measurement range.** A series is `[21, 18, 26, 19, 24, 17]`. Find the minimum, maximum, and their difference.
6. **Select image bands.** Available bands are `['B02', 'B03', 'B04', 'B08', 'B11', 'B12']`. Build a new list containing the first three visible bands and the last two SWIR bands, excluding `B08`.
7. **Combine measurement days.** Day 1 has `[12.0, 13.0, 11.5]`; day 2 has `[14.0, 12.5]`. Build a third series containing all readings in order. Keep both original daily lists unchanged for separate reports. Calculate the combined mean.
8. **Add one sample.** Five samples have classes `forest`, `water`, `forest`, `urban`, `forest`. Add one new `forest` sample to the end of the existing list. Check whether `forest` is present, `cloud` is absent, and how many samples are `forest`.
9. **Error ranking.** Error counts for five samples are `[15, 3, 12, 8, 4]`. Create an ascending list for a report. Keep the original measurement order unchanged.
10. **Independent plans.** A baseline sampling plan is `[10, 20, 30]`. Start an alternative plan with the same values, then change its second value to `25`. Later change the first value of the baseline to `15`. Keep both plans independent.

## 7. Dictionaries (`dict`) — 10 exercises

**Topics:** named fields, keys, values, lookup, update, insertion, `get()`, `pop()`, `values()`, nested dictionaries. **Store object data in dictionaries, not in separate similarly named variables.**

1. **Image metadata.** Image `S2A_01` has `1000` columns, `800` rows, and `10` m pixels. Store its metadata in one record and calculate its ground area in km².
2. **Station record.** Station `K01` has elevation `245` m and temperature `17.5` °C. Store its data in one record and generate `K01: 17.5 C`.
3. **Update metadata.** Image `S2A_01` has acquisition date `20260714`. The correct date is `20260715`, and cloud cover is `12%`. Update the existing record.
4. **Class legend.** Raster class codes `1`, `2`, and `3` mean `water`, `forest`, and `urban`. Create a code-to-name lookup. Read class `2`, then add code `4` for `agriculture`.
5. **Band resolutions.** Bands `B02`, `B03`, `B04`, and `B08` have `10` m resolution; `B11` has `20` m. Store band-to-resolution mappings. Look up `B11` and check whether `B01` exists.
6. **Missing metadata.** Image `S2A_02` has only an ID and year `2026`. Read cloud cover, returning `'unknown'` if the field is missing. Do not raise an error.
7. **Sample pH.** pH values for `P01`, `P02`, `P03` are `6.3`, `7.1`, `6.8`. Correct `P02` to `7.0` and add `P04` with pH `6.5`. Store values by sample ID and calculate the mean pH.
8. **Remove obsolete metadata.** A record contains `id = S2A_01`, `format = tif`, and `temporary_path = /tmp/image.tif`. Remove the obsolete temporary path field.
9. **Station with measurements.** Station `K02` has unit `C` and temperature series `[14.0, 15.5, 15.0]`. Add a reading of `16.0`. Keep the series inside the station record and calculate its mean.
10. **Image archive.** An archive contains `S2A_01` with `12%` cloud cover and `S2A_02` with `35%`. Organize records for lookup by image ID. Check whether the first image has lower cloud cover. Add a `10` m resolution field to that image.

## 8. Combined exercises — 10 exercises

**Topics:** all previous sections. Choose variables, lists, and dictionaries to match the data. No loops, `if` statements, or user-defined functions.

1. **Raster parameters.** Image `DEM_01` has `1500 × 1000` pixels, `5` m pixel size, and `4` bytes per pixel. Store metadata in one record. Calculate ground area in km² and raw pixel data size in MiB.
2. **Station report.** Station `K01` records `[12.5, 13.0, 13.5]` °C. Add a new reading of `14.0` °C. Generate a report string containing the station code and mean temperature.
3. **Related filenames.** Scene metadata contains satellite `S2A` and date `20260715`. Store both in one record. Generate image filename `S2A_20260715.tif` and mask filename `S2A_20260715_mask.tif`.
4. **Samples and legend.** Sample class codes are `[1, 2, 2, 3, 2]`. The legend is `1: water`, `2: forest`, `3: urban`. Find the name of class `2` and count its samples.
5. **RGB composite.** Band files are `B02 → scene_B02.tif`, `B03 → scene_B03.tif`, and `B04 → scene_B04.tif`. RGB channel order is `B04`, `B03`, `B02`. Create a list of filenames in R–G–B order.
6. **Compare stations.** Station `A` records `[18, 20, 19]` °C; station `B` records `[15, 17, 16]` °C. Store both series under their station codes. Calculate the difference between mean temperatures (`A − B`).
7. **Measurement log.** Measurements `M01` and `M02` have values `15.2` and `16.4`. Correct `M02` to `16.1`. Store ordered records with their own IDs. Check whether the corrected second value exceeds the first.
8. **Image collection.** A collection contains `S2A_01` (`12%` cloud cover) and `S2A_02` (`35%`). Add `S2A_03` (`8%`). Keep each image's data together and preserve scene order. Count images and check whether the third has lower cloud cover than the first.
9. **Image–mask pairs.** Image `A.tif` has mask `A_mask.tif` with classes `[1, 2]`. Image `B.tif` has mask `B_mask.tif` with classes `[1, 3]`. Store both as one collection of records. Add class `4` to the second pair only.
10. **Classification project.** Project `landcover` contains images `S2A_01` and `S2A_02`, legend `{1: 'water', 2: 'forest'}`, and sample codes `[1, 2, 2, 1, 2]`. Store the project in one structure. Find the name of class `2`, its sample count, and the second image ID.
