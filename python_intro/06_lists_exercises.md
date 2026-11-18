# Lists (`list`) — exercises

> Topics: list elements, indexing, slicing, `append()`, `extend()`, `pop()`, `+`, `copy()`, `len()`, `sum()`, `min()`, `max()`, `sorted()`, `count()`, `in`.

### 1. Temperature series.

Six hourly temperatures are `15.2`, `13.8`, `16.1`, `14.0`, `15.7`, and `16.4` °C. Store the series in one object. Calculate the mean without adding each value manually.

### 2. New measurement batch.

Recorded rainfall values are `[3, 0, 7, 2]` mm. A new batch contains `[5, 4]` mm. Add the new readings to the existing main series. Calculate total rainfall.

### 3. Correct a reading.

A temperature series is `[12.1, 13.5, -9999, 14.2, 13.8]`. The third value is corrected to `13.7`. Update the series and calculate the mean.

### 4. Remove an invalid reading.

The final value in `[7.2, 7.4, 7.3, -9999]` is invalid. Remove it from the existing series and calculate the mean.

### 5. Measurement range.

A series is `[21, 18, 26, 19, 24, 17]`. Find the minimum, maximum, and their difference.

### 6. Select image bands.

Available bands are `['B02', 'B03', 'B04', 'B08', 'B11', 'B12']`. Build a new list containing the first three visible bands and the last two SWIR bands, excluding `B08`.

### 7. Combine measurement days.

Day 1 has `[12.0, 13.0, 11.5]`; day 2 has `[14.0, 12.5]`. Build a third series containing all readings in order. Keep both original daily lists unchanged for separate reports. Calculate the combined mean.

### 8. Add one sample.

Five samples have classes `forest`, `water`, `forest`, `urban`, `forest`. Add one new `forest` sample to the end of the existing list. Check whether `forest` is present, `cloud` is absent, and how many samples are `forest`.

### 9. Error ranking.

Error counts for five samples are `[15, 3, 12, 8, 4]`. Create an ascending list for a report. Keep the original measurement order unchanged.

### 10. Independent plans.

A baseline sampling plan is `[10, 20, 30]`. Start an alternative plan with the same values, then change its second value to `25`. Later change the first value of the baseline to `15`. Keep both plans independent.
