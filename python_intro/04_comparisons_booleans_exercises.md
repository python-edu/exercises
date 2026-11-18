# Comparisons and Boolean values — exercises

> Topics: `<`, `<=`, `>`, `>=`, `==`, `!=`, `and`, `or`, `not`. Store each check as `True` or `False`. Do not use `if`.

### 1. Image quality.

An image has `18%` cloud cover and `10` m resolution. Accept it only if cloud cover is at most `20%` and pixel size is at most `10` m. Check whether it passes.

### 2. Sensor range.

A sensor works from `-40` to `60` °C, including both limits. Check readings of `-40` °C and `61` °C.

### 3. Valid measurement.

The value `-9999` means missing data. A valid humidity reading must be different from `-9999` and within `0–100%`. Check `-9999` and `87` separately.

### 4. Image rejection.

Reject an image if cloud cover exceeds `70%` or the camera angle exceeds `30` degrees. For `45%` cloud cover and a `34`-degree angle, check both rejection and acceptance.

### 5. Manual approval.

Accept an image if cloud cover is at most `20%` and pixel size is at most `10` m. Manual approval can also allow the image. Check `35%` cloud cover, `10` m pixels, and manual approval granted.

### 6. Class code.

A pixel has class code `2`. Check whether it equals forest code `2` and differs from water code `1`.

### 7. Resolution limits.

A raster has `20` m pixels. Check whether its pixel size is greater than `10` m and less than `30` m.

### 8. Free disk space.

A job needs at least `8` GiB of free space. The disk has exactly `8` GiB free. Check whether the requirement is met.

### 9. Cloud flag.

A cloud detector sets `cloud_detected = False`. Check whether the image is cloud-free using `not`.

### 10. Data readiness.

A file is ready if it exists and either its quality score is at least `80` or it has manual approval. Check a file that exists, has quality `75`, and has manual approval.
