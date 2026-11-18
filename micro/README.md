# Editing text with micro

**Goal:** create a file, save a copy, navigate, search, replace, duplicate and delete lines.

**Required:** `micro`, a terminal, `source.txt`.

## Prepare

1. Download `source.txt` from the repository (**Download raw file** on GitHub).
2. Use the `shell-practice` directory from the previous exercise. Create it if needed:

   ```sh
   mkdir ~/shell-practice
   ```

3. Move the downloaded file and open the directory:

   ```sh
   mv ~/Downloads/source.txt ~/shell-practice/
   cd ~/shell-practice
   ls
   ```

## 1. Create a file

```sh
micro notes-micro.txt
```

Type:

```text
My first text file.
I am learning to edit text in micro.
```

- **Ctrl+S** — save.
- **Ctrl+Q** — quit.

Check:

```sh
cat notes-micro.txt
```

## 2. Save a working copy

```sh
micro source.txt
```

1. Press **Ctrl+E** (command bar).
2. Type `save work-micro.txt` and press **Enter**.
3. Press **Ctrl+Q**.
4. Open the copy:

   ```sh
   micro work-micro.txt
   ```

Edit **only** `work-micro.txt` in the next steps.

## 3. Move through the text

1. Press **Ctrl+L**, type `6`, and press **Enter**.
2. Press **Home** and **End** to move to the start and end of the line.
3. Use **Ctrl+Right** and **Ctrl+Left** to move between words.

Line 6 contains `wooden bridge`.

## 4. Search and replace

1. Press **Ctrl+F**, type `TODO`, and press **Enter**.
2. Press **Ctrl+N** twice to find the next two matches.
3. Press **Ctrl+F**, search for `wooden`, and press **Enter**.
4. Select `wooden` (double-click or **Shift+Arrow**). Type `stone`.
5. Press **Ctrl+Z** (undo), then **Ctrl+Y** (redo).

Expected: `stone bridge`.

## 5. Duplicate a line

1. Press **Ctrl+L** and go to line `12` (`Station C: pending`).
2. Press **Ctrl+D** to duplicate the line.
3. In the new line, select `C` and type `D`.

Expected: `Station C: pending` followed by `Station D: pending`.

**Ctrl+C** copies selected text; **Ctrl+V** pastes it.

## 6. Remove a block

1. Press **Ctrl+F**, search for `Draft`, and press **Enter**.
2. Press **Home** to move to the start of the heading.
3. Hold **Shift** and press **Down** four times: select `Draft`, both `REMOVE` lines, and the empty line after them.
4. Press **Ctrl+X** to cut the block.

The `Summary` heading must remain.

## 7. Change repeated words

1. Find the first `TODO` and double-click it to select the word.
2. Press **Alt+N** twice to select the next two occurrences.
3. Type `DONE` once.
4. Press **Alt+C** to return to one cursor.

Expected: three `DONE` lines.

## 8. Save and check

Press **Ctrl+S**, then **Ctrl+Q**.

```sh
cat work-micro.txt
cat source.txt
```

Check `work-micro.txt`:

- `stone bridge`;
- `Station D: pending`;
- three `DONE` entries;
- no `Draft` or `REMOVE` lines.

`source.txt` must remain unchanged.

## Help

**Ctrl+E** → `help defaultkeys` → **Enter**.

[Micro — default keys](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md) · [Micro — commands](https://github.com/micro-editor/micro/blob/master/runtime/help/commands.md)
