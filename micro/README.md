# Text editing — micro

**Goal:** edit text, use keyboard navigation, work with several files.

**Required:** terminal, `micro`, `source.txt`.

**Course keybindings:** `Alt+S` = **Save As**; `Ctrl+J` = **relative line jump**. Both were configured in the previous lesson.

## Prepare

Download `source.txt` from the course repository. In the terminal:

```sh
mkdir -p ~/shell-practice
mv ~/Downloads/source.txt ~/shell-practice/
cd ~/shell-practice
ls
```

**Completion:** Exercise 2 uses `Tab` for words in the file. In filename/command prompts, `Tab` completes names and commands.

**Keyboard note (compact laptops):** `Home`, `End`, `PgUp`, and `PgDn` may need `Fn` + an arrow key. In micro, use `Alt+A` / `Alt+E` for line start/end and `Ctrl+Up` / `Ctrl+Down` for file start/end. **`Ctrl+Left` / `Ctrl+Right` move between words, not lines.**

**Order:** complete Parts I, II, and III in sequence. Keep `source.txt` unchanged; edit `work-micro.txt`.


---


# Part I — Files, tabs, and splits

### 1. Create and save a file

**Goal:** create `notes-micro.txt` with reference words for word completion.

**Keys**
- `Ctrl+S` — save the current file.
- `Ctrl+Q` — close the current file.
- `Ctrl+Shift+V` — paste text in many Linux terminals (or use the terminal's Paste command).

**Steps**
1. Run `micro notes-micro.txt`.
2. **Copy** this text from the README and **paste** it into micro:

   ```text
   Field vocabulary
   forest field flood
   bridge branch brook
   soil slope stone stream
   station status stack
   camera canopy canyon
   ```
3. Press `Ctrl+S`, then `Ctrl+Q`.

**Check:** `notes-micro.txt` contains all reference words. Keep the file for Exercise 2.

### 2. Complete words after 1, 2, and 3 letters

**Goal:** use words already in the file. Compare suggestion lists for different prefixes. No LSP.

**Keys**
- `Ctrl+Down` — end of file.
- `Enter` — new line.
- `Tab` — show and insert a matching word; press again for the next match.
- `Shift+Tab` — previous match.
- `Ctrl+S` / `Ctrl+Q` — save / close.

**Steps**
1. Run `micro notes-micro.txt`. Press `Ctrl+Down`, then `Enter`.
2. Type `Site: s`. Press `Tab`; cycle to **soil**.
3. Press `Enter`. Type `Water: st`. Press `Tab`; cycle to **stream**.
4. Press `Enter`. Type `Place: sta`. Press `Tab`; cycle to **station**.
5. Press `Enter`. Type `Crossing: br`. Press `Tab`; cycle to **bridge**.
6. Save (`Ctrl+S`) and close (`Ctrl+Q`).

**Compare the matches:**

| Prefix | Possible words in the file | Choose |
|---|---|---|
| `s` (1 letter) | soil, slope, stone, stream, station, status, stack | soil |
| `st` (2 letters) | stone, stream, station, status, stack | stream |
| `sta` (3 letters) | station, status, stack | station |
| `br` (2 letters) | bridge, branch, brook | bridge |

**Check:** four new lines contain `soil`, `stream`, `station`, and `bridge`. The full words were selected, not typed.

### 3. Save As

**Goal:** create `work-micro.txt`. Keep `source.txt` unchanged.

**Keys**
- `Alt+S` — **Save As** (course keybinding).
- `Ctrl+E` — command bar; `save FILE` = Save As.

**Steps**
1. Run `micro source.txt`.
2. Press `Alt+S`, enter `work-micro.txt`, press `Enter`.
3. Alternative: `Ctrl+E` → `save work-micro.txt` → `Enter`.
4. Edit **only** `work-micro.txt` in the next tasks.

**Check:** the working copy is named `work-micro.txt`.

### 4. Open another file in the running editor

**Goal:** open `notes-micro.txt` using filename completion; return to the working file.

**Keys**
- `Ctrl+S` — save.
- `Ctrl+O` — open a filename prompt.
- `Tab` / `Shift+Tab` — complete filename / cycle suggestions.
- `Enter` — open the selected filename.

**Steps**
1. Save with `Ctrl+S`.
2. Press `Ctrl+O`. Type `notes` and press `Tab` to complete `notes-micro.txt`. Press `Enter`.
3. Press `Ctrl+O`. Type `work` and press `Tab` to complete `work-micro.txt`. Press `Enter`.

**Check:** `work-micro.txt` is active; each filename was completed rather than typed in full.

### 5. Use tabs without a mouse

**Goal:** open the original file in a separate tab; switch and close tabs.

**Keys**
- `Ctrl+E` — command bar; `Tab` completes commands and filenames.
- `tab FILE` — open a file in a new tab.
- `Alt+,` / `Alt+.` — previous / next tab.
- `Ctrl+Q` — close the active tab.

**Steps**
1. Press `Ctrl+E`. Enter `tab so`; press `Tab` to complete `source.txt`, then `Enter`.
2. Press `Alt+,` to show `work-micro.txt`.
3. Press `Alt+.` to show `source.txt`.
4. Press `Ctrl+Q` to close the `source.txt` tab.

**Check:** `work-micro.txt` remains open.

### 6. Use vertical splits without a mouse

**Goal:** show `work-micro.txt` and `source.txt` side by side.

**Keys**
- `Ctrl+E` — command prompt; `Tab` completes commands and filenames.
- `vsplit FILE` — open a file in a vertical split.
- `Ctrl+W` — switch splits.
- `Ctrl+Q` — close the active view.

**Steps**
1. Press `Ctrl+E`. Type `vs`, press `Tab` to complete `vsplit`.
2. Type ` so`, then press `Tab` to complete `source.txt`; press `Enter`.
3. Press `Ctrl+W` to switch panels; press it again to return.
4. With `source.txt` active, press `Ctrl+Q` to close that view.

**Check:** only `work-micro.txt` remains visible.

**Continue:** return to `work-micro.txt` before Part II.

---


# Part II — One operation at a time

### 7. Move through text

**Goal:** move in a file, line, and word. Do not change text.

**Keys**
- `Ctrl+Up` / `Ctrl+Down` — file start / end.
- `Alt+A` / `Alt+E` — line start / end.
- `Ctrl+Left` / `Ctrl+Right` — previous / next word.
- `Left` / `Right` — one character.
- `PgUp` / `PgDn` — one page up / down.

**Steps**
1. Press `Ctrl+Down`, then `Ctrl+Up`.
2. Press `Down` **five times** to reach `The first observation ...`.
3. Press `Alt+E`, then `Alt+A`.
4. Press `Ctrl+Right` several times; then `Ctrl+Left`.
5. Try `PgDn`, then `PgUp` (`Fn` may be required).

**Check:** no text changed.

### 8. Jump by line number

**Goal:** move to an exact line and then by a relative number of lines.

**Keys**
- `Ctrl+L` — absolute line number.
- `Ctrl+J` — relative line jump (course keybinding).

**Steps**
1. Press `Ctrl+L`, enter `6`, press `Enter`.
2. Press `Ctrl+J`, enter `3`, press `Enter`.
3. Press `Ctrl+J`, enter `-3`, press `Enter`.

**Check:** line 6 → line 9 (`Stations`) → line 6.

### 9. Replace a character — manual position

**Goal:** change `Station X: remove` to `Station Y: remove` without search.

**Keys**
- `Ctrl+L` — jump to a line.
- `Alt+A` — line start.
- `Right` — one character to the right.
- `Shift+Right` — select one character.

**Steps**
1. Press `Ctrl+L`, enter `13`, press `Enter`.
2. Press `Alt+A`.
3. Press `Right` **eight times** to reach the letter `X`.
4. Press `Shift+Right` **once** to select `X`.
5. Type uppercase `Y` to replace it.

**Check:** `Station Y: remove`.

### 10. Search for text

**Goal:** find three `TODO` labels. Do not edit them.

**Keys**
- `Ctrl+F` — search text.
- `Ctrl+N` — next result.
- `Ctrl+P` — previous result.

**Steps**
1. Press `Ctrl+F`, enter `TODO`, press `Enter`.
2. Press `Ctrl+N` twice, then `Ctrl+P` once.

**Check:** three unchanged `TODO` labels.

### 11. Find a character; replace it

**Goal:** return `Station Y: remove` to `Station X: remove` using search.

**Keys**
- `Ctrl+F` — search a string or one character, across the file.
- `Esc` — clear selection.
- `Alt+A` — line start.
- `Ctrl+Right` — move to the next word.
- `Shift+Right` — select a character.

**Steps**
1. Try `Ctrl+F` → `:` → `Enter` to find a single character. Do not edit it.
2. Press `Ctrl+F`, enter `Station Y:`, press `Enter`.
3. Press `Esc`, then `Alt+A`.
4. Press `Ctrl+Right` to reach `Y`.
5. Press `Shift+Right` once; type `X`.

**Check:** `Station X: remove` again.

**Note:** micro has no default `f<char>` motion like Helix. `Ctrl+F` searches the file; `Ctrl+N/P` move between matches.

### 12. Select and replace one word

**Goal:** change `wooden` to `stone`.

**Keys**
- `Ctrl+F` — find and select a word.
- Typing — replace selected text.
- `Ctrl+Shift+Right` — select a whole word from its start (alternative).

**Steps**
1. `Ctrl+F` → `wooden` → `Enter`.
2. The matching word is selected. Type `stone`.

**Check:** `The first observation was near a stone bridge.`

### 13. Select and delete one word

**Goal:** remove `obsolete` from the quality field.

**Keys**
- `Ctrl+F` — find the line.
- `Alt+E` — line end.
- `Ctrl+Shift+Left` — select the word to the left.
- `Backspace` — delete selected text.

**Steps**
1. `Ctrl+F` → `Quality flag:` → `Enter` → `Esc`.
2. Press `Alt+E`, then `Ctrl+Shift+Left` to select `obsolete`.
3. Press `Backspace`.

**Check:** the line contains `Quality flag:` with an empty value.

### 14. Delete one complete line

**Goal:** remove `Station X: remove`, including its line break.

**Keys**
- `Ctrl+F` — find a line.
- `Esc` — clear selection.
- `Ctrl+K` — cut the whole current line.

**Steps**
1. `Ctrl+F` → `Station X: remove` → `Enter` → `Esc`.
2. Press `Ctrl+K` once.

**Check:** `Station X` is gone. `Measurements` remains.

### 15. Duplicate a complete line

**Goal:** create a second `Station C: pending` line.

**Keys**
- `Ctrl+F` — find the line.
- `Esc` — clear selection.
- `Ctrl+D` — duplicate the current line (or selection).

**Steps**
1. `Ctrl+F` → `Station C: pending` → `Enter` → `Esc`.
2. Press `Ctrl+D` **once**.

**Check:** two adjacent `Station C: pending` lines.

### 16. Change a letter in the copied line

**Goal:** change **only the second** `Station C` to `Station D`.

**Keys**
- `Ctrl+Up` — file start.
- `Ctrl+F` / `Ctrl+N` — find first / next match.
- `Alt+A` — line start.
- `Ctrl+Right` — next word.
- `Shift+Right` — select one character.

**Steps**
1. Press `Ctrl+Up`.
2. `Ctrl+F` → `Station C: pending` → `Enter`.
3. Press `Ctrl+N` to reach the **second** match.
4. Press `Esc`, then `Alt+A`, then `Ctrl+Right`.
5. Press `Shift+Right` once; type uppercase `D`.

**Check:** `Station C: pending` and `Station D: pending`.

### 17. Select and delete a block

**Goal:** remove the complete `Draft` section, including its blank line.

**Keys**
- `Ctrl+F` — find the section.
- `Esc` — clear selection.
- `Alt+A` — line start.
- `Shift+Down` — extend selection down.
- `Ctrl+X` — cut selected lines.

**Steps**
1. `Ctrl+F` → `Draft` → `Enter` → `Esc`.
2. Press `Alt+A`.
3. Hold `Shift` and press `Down` **four times**.
4. Press `Ctrl+X`.

**Check:** `Draft` and both `REMOVE` lines are gone; `Summary` remains.

### 18. Replace text inside brackets and quotes

**Goal:** replace values, not the surrounding characters.

**Keys**
- `Ctrl+F` — find and select matching text.
- Typing — replace the found selection.

**Steps**
1. `Ctrl+F` → `3 m` → `Enter`. Type `4 m`.
2. `Ctrl+F` → `2 m` → `Enter`. Type `5 m`.
3. `Ctrl+F` → `cloudy` → `Enter`. Type `sunny`.

**Check:**

```text
Bridge width: (4 m)
Lake depth: [5 m]
Weather: "sunny"
```

**Note:** search selects the **inside value**. You do not need to select each character or remove the brackets.

### 19. Delete only the text inside braces

**Goal:** remove `temporary`; keep `{}`.

**Keys**
- `Ctrl+F` — find and select text.
- `Backspace` — delete the selected text.

**Steps**
1. `Ctrl+F` → `temporary` → `Enter`.
2. Press `Backspace`.

**Check:** `Unused value: {}`.

### 20. Undo and redo

**Goal:** reverse the last edit and restore it.

**Keys**
- `Ctrl+Z` — undo.
- `Ctrl+Y` — redo.

**Steps**
1. Press `Ctrl+Z`: `temporary` returns.
2. Press `Ctrl+Y`: `temporary` disappears again.

**Check:** `Unused value: {}`.

---


# Part III — Combined operations

### 21. Update repeated statuses

**Goal:** update all task and station statuses; finish the quality field.

**Keys**
- `Ctrl+F` — find the first result.
- `Alt+N` — add the next match to the selection (multiple cursors).
- `Alt+C` — return to one cursor.
- `Ctrl+E` / `Tab` — command prompt and command completion (`repl` → `Tab` to choose `replaceall`).
- `Alt+E` — line end.

**Steps**
1. `Ctrl+F` → `TODO` → `Enter`.
2. Press `Alt+N` **twice**. Type `DONE` once. Press `Alt+C`.
3. Press `Ctrl+E`; type `repl` and use `Tab` to choose `replaceall`, then type ` pending checked` → `Enter`.
4. `Ctrl+F` → `Quality flag:` → `Enter` → `Esc`.
5. Press `Alt+E`; type `checked`.

**Check:** three `DONE` labels, four `Station ... checked` lines, `Quality flag: checked`.

### 22. Edit several lines at once

**Goal:** create a bullet list and add ` | GPS` to all four stations.

**Keys**
- `Ctrl+F` / `Esc` — find a start line / clear selection.
- `Alt+A` / `Alt+E` — line start / end.
- `Alt+Shift+Down` — add a cursor on the next line.
- `Alt+C` — remove extra cursors.

**Steps**
1. `Ctrl+F` → `Inspect the bridge.` → `Enter` → `Esc`.
2. Press `Alt+A`, then `Alt+Shift+Down` **twice**.
3. Type `- ` once; press `Alt+C`.
4. `Ctrl+F` → `Station A: checked` → `Enter` → `Esc`.
5. Press `Alt+E`, then `Alt+Shift+Down` **three times**.
6. Type ` | GPS` once; press `Alt+C`.

**Check:** three `- ` checklist lines; all four station lines end in ` | GPS`.

### 23. Create a report from selected lines

**Goal:** copy the completed checklist to a **new file** without retyping it.

**Keys**
- `Ctrl+F` — find the first checklist item.
- `Alt+A` — line start.
- `Shift+Down` — select lines.
- `Ctrl+C` / `Ctrl+V` — copy / paste.
- `Ctrl+T` — create an empty new tab.
- `Alt+S` — save the new tab under a filename (course keybinding).

**Steps**
1. `Ctrl+F` → `- Inspect the bridge.` → `Enter` → `Esc`.
2. Press `Alt+A`; hold `Shift` and press `Down` **three times**.
3. Press `Ctrl+C`.
4. Press `Ctrl+T` to create an empty tab.
5. Type `Field checklist`, press `Enter`, then `Ctrl+V`.
6. Press `Alt+S`. Save once as `report-micro.txt`. Use `Alt+,` to return to `work-micro.txt`.

**Check:** `report-micro.txt` has one heading and three bullet items.

### 24. Compare original and edited files

**Goal:** verify the changes in two panels without changing `source.txt`.

**Keys**
- `Ctrl+S` — save.
- `Ctrl+E` / `Tab` — complete the `vsplit` command and the filename.
- `Ctrl+W` — switch panels.
- `Ctrl+F` — locate matching text.
- `Ctrl+Q` — close the active panel.

**Steps**
1. Save `work-micro.txt` with `Ctrl+S`.
2. Press `Ctrl+E`; type `vs`, `Tab`, ` so`, `Tab`, `Enter` to open `source.txt` in a vertical split.
3. In `work-micro.txt`, search for `stone bridge`.
4. Press `Ctrl+W`; in `source.txt`, search for `wooden bridge`.
5. Check the four stations and the three checklist lines in both files.
6. Close the `source.txt` panel with `Ctrl+Q`. Leave `work-micro.txt` saved.

**Check:** `source.txt` contains the original text; `work-micro.txt` contains the edits.

## Help

`Ctrl+E` → `help defaultkeys` → `Enter`.

**References:** [micro default keys](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md) · [micro commands](https://github.com/micro-editor/micro/blob/master/runtime/help/commands.md)
