# Dictionaries (`dict`) — exercises

> Topics: named fields, keys, values, lookup, update, insertion, `get()`, `pop()`, `values()`, nested dictionaries. Store object data in dictionaries, not in separate similarly named variables.

### 1. Image metadata.

Image `S2A_01` has `1000` columns, `800` rows, and `10` m pixels. Store its metadata in one record and calculate its ground area in km².

### 2. Station record.

Station `K01` has elevation `245` m and temperature `17.5` °C. Store its data in one record and generate `K01: 17.5 C`.

### 3. Update metadata.

Image `S2A_01` has acquisition date `20260714`. The correct date is `20260715`, and cloud cover is `12%`. Update the existing record.

### 4. Class legend.

Raster class codes `1`, `2`, and `3` mean `water`, `forest`, and `urban`. Create a code-to-name lookup. Read class `2`, then add code `4` for `agriculture`.

### 5. Band resolutions.

Bands `B02`, `B03`, `B04`, and `B08` have `10` m resolution; `B11` has `20` m. Store band-to-resolution mappings. Look up `B11` and check whether `B01` exists.

### 6. Missing metadata.

Image `S2A_02` has only an ID and year `2026`. Read cloud cover, returning `'unknown'` if the field is missing. Do not raise an error.

### 7. Sample pH.

pH values for `P01`, `P02`, `P03` are `6.3`, `7.1`, `6.8`. Correct `P02` to `7.0` and add `P04` with pH `6.5`. Store values by sample ID and calculate the mean pH.

### 8. Remove obsolete metadata.

A record contains `id = S2A_01`, `format = tif`, and `temporary_path = /tmp/image.tif`. Remove the temporary path and view the remaining keys.

### 9. Station with measurements.

Station `K02` has unit `C` and temperature series `[14.0, 15.5, 15.0]`. Add a reading of `16.0`. Keep the series inside the station record and calculate its mean.

### 10. Image archive.

An archive contains `S2A_01` with `12%` cloud cover and `S2A_02` with `35%`. Organize records for lookup by image ID. Check whether the first image has lower cloud cover. Add a `10` m resolution field to that image.
