# Editing text with micro

  >- **Goal:** create and save a text file; move through a document; select, replace, and delete text; edit repeated words.
  >- Systems:Windows, Linux, macOS.
  >- **Required:** the `micro` editor.

  >- We will use the `shell-practice` directory created during the previous exercise.
  >- All files created or edited during this exercise will remain in `shell-practice`.

---


# Prepare the working directory 

>- Open your terminal and check whether `shell-practice` exists in your home directory:

```sh
ls 
```

If `shell-practice` does not exist, create it:

```sh
mkdir ~/shell-practice
```

---


# Download `source.txt` file

The repository contains a practice file, `source.txt`, with sample text.

1. Open `source.txt` on GitHub.
2. Click **Download raw file** to download it.
3. Open your terminal.

Check that the file was downloaded to your `Downloads` directory:

```sh
ls ~/Downloads
```

Move the file to the `shell-practice` directory created during the previous exercise:

```sh
mv ~/Downloads/source.txt ~/shell-practice/
```

Go to the working directory:

```sh
cd ~/shell-practice

# Check that source.txt is available.
ls
```

Open the file in micro:

```sh
micro source.txt
```

---


# 1. Create and save a file

The command `micro notes.txt` opens the text editor. Because `notes.txt` is a new filename, you start with an empty document. The file is written to disk when you save it.

```sh
micro notes.txt
```

Type:

```text
My first text file.
I am learning to edit text in micro.
```

Press **Ctrl+S** to save, then **Ctrl+Q** to close micro.

`cat` displays the saved text in the terminal:

```sh
# Check: the two lines should appear.
cat notes.txt
```

---


# 2. Open a document and save it under another name

The repository includes `source.txt`, an original practice text available under CC0 1.0. Open it:

```sh
micro source.txt
```


### Save the file as `work.txt` - using the command bar

1. Press **Ctrl+E** to open the command bar at the bottom of micro.
2. Type `save work.txt` and press **Enter**.


### Save the file as `work.txt` - using a keyboard shortcut (if configured earlier)

1. Press **Alt+S** to open the **Save As** prompt.
2. Type `work.txt` in the `Filename:` field and press **Enter**.

Both methods save the document as `work.txt`.

---


# 3. Move the cursor

**Ctrl+L** opens a prompt for a line number. Enter `6` and press **Enter**. You should reach:

```text
The first observation was near a wooden bridge.
```

Move to the beginning of that line with **Home**, then to its end with **End**.

If your keyboard requires **Fn** for Home/End, use it. In micro, **Alt+A** also moves to the beginning of a line and **Alt+E** to its end (provided the terminal passes Alt keystrokes to micro).

Line numbers are normally shown on the left. To enable them if they are hidden, press **Ctrl+E**, enter `set ruler true`, and press **Enter**. To show the distance from the current line instead, enter `set relativeruler true` in the same way.

Now try a **relative jump**. Starting on line 6:

1. Press **Ctrl+E**, enter `jump 3`, and press **Enter**. You should reach line 9 (`Stations`).
2. Press **Ctrl+E**, enter `jump -3`, and press **Enter**. You should return to line 6.

`Ctrl+L` goes to an **absolute** line number; `jump` moves **relative** to the current line. To restore ordinary line numbers, use **Ctrl+E** → `set relativeruler false`.

Use **Ctrl+L** again to jump to line `15`, then return to line `6`.

---


# 4. Select and replace text

On line 6, replace `wooden` with `stone`:

1. Double-click `wooden` to select the word, or select it using **Shift+Arrow**.
2. Type `stone` to replace the selection.
3. Press **Ctrl+Z** to undo; press **Ctrl+Y** to redo.

The line should now contain `stone bridge`.

---


# 5. Remove several lines

The `Draft` section contains two outdated lines. Remove both, but leave the `Draft` heading:

1. Press **Ctrl+L** and enter `20`.
2. Move the cursor to the very beginning of the `REMOVE: Temporary comment.` line (with **Home**, **Alt+A**, or the mouse).
3. Hold **Shift** and press **Down** twice to select both lines and their line endings.
4. Press **Ctrl+X** to cut the selected text.

The `Draft` heading remains, and the two `REMOVE` lines disappear.

**Ctrl+C** copies a selection; **Ctrl+V** pastes. Press **Ctrl+Z** to undo the removal if you need to retry.

---


# 6. Change repeated words at once

The `Tasks` section contains three lines beginning with `TODO`.

1. Double-click the first `TODO` to select it.
2. Press **Alt+N** twice to add the next two occurrences to the selection.
3. Type `DONE` once. All three occurrences should change.
4. Press **Alt+C** to return to a single cursor.

If the terminal intercepts Alt combinations, complete the replacements one at a time with normal selection. Multi-cursor editing is an additional technique, not a prerequisite for saving your work.

---


# 7. Save and check

Press **Ctrl+S** and then **Ctrl+Q**.

```sh
# Check: your edited working copy.
cat work.txt
# Check: the original is unchanged.
cat source.txt
```

In `work.txt`, expect `stone bridge`, three `DONE` entries, and no lines starting with `REMOVE`. The original `source.txt` should still contain the initial text.

## Help

Inside micro, press **Ctrl+E**, type `help defaultkeys`, and press **Enter** to see built-in shortcuts. For instructions about customizing them, use `help keybindings`.

**Terminal note:** Some keyboards or terminals do not send Home, End, or Alt key combinations correctly. The `raw` command in micro (**Ctrl+E** → `raw`) shows the key sequences the editor receives.

## References

- [Micro: quick start](https://github.com/micro-editor/micro/blob/master/runtime/help/help.md)
- [Micro: default keys](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md)
- [Micro: keybindings](https://github.com/micro-editor/micro/blob/master/runtime/help/keybindings.md)
- [Micro: commands](https://github.com/micro-editor/micro/blob/master/runtime/help/commands.md)
- [Micro: options](https://github.com/micro-editor/micro/blob/master/runtime/help/options.md)
