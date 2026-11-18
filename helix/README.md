# Editing text with Helix

**Goal:** create a file, save a copy, navigate, search, replace, duplicate and delete lines.

**Required:** `hx` (Helix), a terminal, `source.txt`.

## Modes — read first

Helix uses different keys for different tasks:

| Mode | Purpose | Enter / exit |
|---|---|---|
| **Normal** | Move and run editing commands | Default; **Esc** returns here |
| **Insert** | Type text | `i` to enter; **Esc** to exit |
| **Select** | Extend a text selection | `v` to enter; **Esc** to exit |
| **Command** | Save, open and quit | `:` from Normal; **Enter** runs the command |

**Important:** In Normal mode, letters are commands, not text. For example, `6G` means press `6` and then **Shift+G**.

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
hx notes-helix.txt
```

1. Press `i` to enter **Insert** mode.
2. Type:

   ```text
   My first text file.
   I am learning to edit text in Helix.
   ```

3. Press **Esc** to return to **Normal** mode.
4. Type `:w` and press **Enter** to save.
5. Type `:q` and press **Enter** to quit.

Check:

```sh
cat notes-helix.txt
```

## 2. Save a working copy

```sh
hx source.txt
```

1. In **Normal** mode, type `:w work-helix.txt` and press **Enter**.
2. Type `:q` and press **Enter**.
3. Open the copy:

   ```sh
   hx work-helix.txt
   ```

Edit **only** `work-helix.txt` in the next steps.

## 3. Move through the text

1. In **Normal** mode, press `6G` to go to line 6.
2. Press `gh` to move to the start of the line; `gl` to the end.
3. Press `w` to move to the next word; `b` to move to the previous word.

Line 6 contains `wooden bridge`.

## 4. Search and replace

1. Press `/`, type `TODO`, and press **Enter**.
2. Press `n` twice to find the next two matches.
3. Press `/`, type `wooden`, and press **Enter**.
4. Press `c` to change the selected word (**Insert** mode starts).
5. Type `stone` and press **Esc**.
6. Press `u` (undo), then `U` (redo).

Expected: `stone bridge`.

## 5. Copy and paste a line

1. In **Normal** mode, press `12G` to go to `Station C: pending`.
2. Press `x` to select the line.
3. Press `y` to copy; `p` to paste the copy after it.
4. Press `;` to clear the line selection. Move to `C` in the new line (arrow keys), then press `rD` to replace it with `D`.

Expected: `Station C: pending` followed by `Station D: pending`.

## 6. Remove a block

1. Press `/`, type `Draft`, and press **Enter**.
2. Press `x` four times to select the `Draft` heading, both `REMOVE` lines, and the empty line after them.
3. Press `d` to delete the selection.

The `Summary` heading must remain.

## 7. Change repeated words

1. In **Normal** mode, press `%` to select the whole document.
2. Press `s`, type `TODO`, and press **Enter** to select all three matches.
3. Press `c`, type `DONE`, and press **Esc**.
4. Press `,` to keep one selection.

Expected: three `DONE` lines.

## 8. Save and check

Type `:wq` and press **Enter** to save and quit.

```sh
cat work-helix.txt
cat source.txt
```

Check `work-helix.txt`:

- `stone bridge`;
- `Station D: pending`;
- three `DONE` entries;
- no `Draft` or `REMOVE` lines.

`source.txt` must remain unchanged.

## Help

From a terminal: `hx --tutor`.

[Helix — usage](https://docs.helix-editor.com/usage.html) · [Helix — keymap](https://docs.helix-editor.com/keymap.html) · [Helix — commands](https://docs.helix-editor.com/commands.html)
