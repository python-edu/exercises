# Strings and lists – tasks

Use only the material covered up to and including this chapter.

## Task 1. Coordinate record

A text record contains `450120,5500240,312.5`. Split it into three fields, unpack them and convert the coordinates to integers and the height to a float. Display the resulting coordinate tuple.

## Task 2. Whitespace-separated data

A sensor produces the text `  B02   B03 B04  `. Split it on whitespace and join the resulting band names with semicolons. Also split `B02,,B04` on commas and display the empty field.

## Task 3. Multiline station list

A station list contains three lines: `ST01`, `ST02` and `ST03`. Store the text with newline escape sequences. Split it into lines and join the station IDs with ` | ` as the separator.

## Task 4. File name parsing

Given `L9_20261125_B05_30m.tif`, remove the final extension using slicing. Split the remaining string on underscores and unpack its four fields. Join the sensor, date and band into `L9_20261125_B05`.

## Task 5. Structured labels

Given `DEM:tile:7:12`, split it at the first colon only to separate the product name from the remaining identifier. Then create the label `DEM-007-012` by splitting the remaining identifier, converting the indices to integers, formatting them with three digits and joining the fields with hyphens.
