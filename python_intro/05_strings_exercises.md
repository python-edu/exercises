# Strings (`str`) — exercises

> Topics: string concatenation, `str()`, indexing, slicing, `len()`, `in`, `strip()`, `lower()`, `replace()`, `count()`, `endswith()`.

### 1. Scene filename.

Satellite ID is `S2A`. Acquisition date is the string `20260715`. Build the filename `S2A_20260715.tif`.

### 2. Station code.

A database contains `'  KrK-03  '`. Convert it to `krk-03`: no surrounding spaces, lowercase only.

### 3. Mask filename.

An image is named `scene_07.tif`. Generate the corresponding filename `scene_07_mask.tif` from the image filename.

### 4. Date and satellite ID.

A filename is `S2A_20260715_B04.tif`. Extract the eight-digit date and the first character of the satellite ID.

### 5. TIFF extension.

Only TIFF files are accepted. Check whether `DSM_5M.TIF` has the `.tif` extension, ignoring case.

### 6. Station label.

Region code is `KRK`, and station number is the integer `12`. Build `KRK-12`.

### 7. Remove prefix.

A filename is `raw_dem_10m.tif`. Generate `dem_10m.tif`.

### 8. Count occurrences.

A report line is `cloud,cloud,clear,cloud`. Count occurrences of `cloud`.

### 9. Check scene ID.

The filename `S2A_20260715_B04.tif` must contain satellite ID `S2A` and band ID `B04`. Check both conditions.

### 10. Code length.

The maximum allowed identifier length is `20` characters. Check `S2A_20260715_B04`.
