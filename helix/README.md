# Text editing — Helix

**Goal:** edit text, use keyboard navigation, work with several files.

**Required:** terminal, `hx`, `source.txt`.

## Modes — read first

| Mode | Purpose | Enter / exit |
|---|---|---|
| **Normal** | Move, select, edit | Default; `Esc` returns here |
| **Insert** | Type text | `i` enters; `Esc` exits |
| **Select** | Extend a selection | `v` enters; `Esc` exits |
| **Command** | Save, open, quit | `:` opens; `Enter` runs |

> In Normal mode, letters are commands! For example:
>- `w` moves to the next word **and selects text**
>- `;` removes the selection but keeps the cursors
>- `,` keeps only the main cursor.


> Command prompts use `:` only for short save/new-file commands:
>- type the first letters and use `Tab` / `Shift+Tab` to choose from suggestions.
>- `Enter` runs the command
>- `:w` (write) and `:q` (quit) are short forms


>`Pickers`: type a few letters to filter
>- `Tab` / `Down` = next item, `Shift+Tab` / `Up` = previous item, `Enter` = open, `Ctrl+v` = open in a vertical split, `Esc` = cancel.

## Prepare

Download `source.txt` from the course repository. In the terminal:

```sh
mkdir -p ~/shell-practice
mv ~/Downloads/source.txt ~/shell-practice/
cd ~/shell-practice
ls
```

**Order:** complete Parts I, II, and III in sequence. Keep `source.txt` unchanged; edit `work-helix.txt`.


---


# Part I — Files, tabs, and splits

### 1. Create and save a file

**Goal:** create `notes-helix.txt` with reference words for word completion.

**Keys**
- `i` — enter Insert mode.
- `Esc` — return to Normal mode.
- `:w` / `:q` — save / close.
- `Ctrl+Shift+V` — paste text in many Linux terminals (or use the terminal's Paste command).

**Steps**
1. Run `hx notes-helix.txt`.
2. Press `i`. **Copy** this text from the README and **paste** it into Helix:

   ```text
   Field vocabulary
   forest field flood
   bridge branch brook
   soil slope stone stream
   station status stack
   camera canopy canyon
   ```
3. Press `Esc`; run `:w` → `Enter`, then `:q` → `Enter`.

**Check:** `notes-helix.txt` contains all reference words. Keep the file for Exercise 2.

### 2. Complete words after 1, 2, and 3 letters

**Goal:** use words from the buffer. Compare suggestion lists for different prefixes. No LSP.

**Keys**
- `ge` — go to end of file (Normal mode).
- `o` — open a line below and enter Insert mode.
- `Ctrl+x` — show suggestions manually in Insert mode (also after 1 or 2 letters).
- `Ctrl+n` / `Ctrl+p` — select the next / previous suggestion.
- `Enter` — accept the selected suggestion.
- `Esc` — return to Normal mode.
- `:w` / `:q` — save / close.

**Steps**
1. Run `hx notes-helix.txt`; press `ge`, then `o`.
2. Type `Site: s`; press `Ctrl+x`. Choose **soil**, then `Enter`.
3. Press `Enter` for a new line. Type `Water: st`; press `Ctrl+x`. Choose **stream**, then `Enter`.
4. Press `Enter` for a new line. Type `Place: sta`. With `trigger-length = 3`, suggestions should appear automatically.
   Choose **station**, then `Enter`.
5. Press `Enter` for a new line. Type `Crossing: br`; press `Ctrl+x`. Choose **bridge**, then `Enter`.
6. Press `Esc`; save with `:w` → `Enter`; close with `:q` → `Enter`.

**Compare the matches:**

| Prefix | Possible words in the buffer | Choose |
|---|---|---|
| `s` (1 letter) | soil, slope, stone, stream, station, status, stack | soil |
| `st` (2 letters) | stone, stream, station, status, stack | stream |
| `sta` (3 letters) | station, status, stack | station |
| `br` (2 letters) | bridge, branch, brook | bridge |

**Check:** four new lines contain `soil`, `stream`, `station`, and `bridge`. The full words were selected, not typed.

**Note:** this course uses Helix `master` with `trigger-length = 3`. `Ctrl+x` works manually with shorter prefixes.

### 3. Save As

**Goal:** create `work-helix.txt`. Keep `source.txt` unchanged.

**Keys**
- `:w FILE` — save under a new filename (short `write` command).
- `Tab` / `Shift+Tab` — select command suggestions after `:`.
- `:q` — close the current view.

**Steps**
1. Run `hx source.txt`.
2. Press `:` and check the suggested commands. Use `w` (short form of `write`), type ` work-helix.txt`, then press `Enter`.
3. Enter `:q` → `Enter`.
4. Run `hx work-helix.txt`.

**Check:** edit **only** `work-helix.txt` in the next tasks.

### 4. Open another file in the running editor

**Goal:** open `notes-helix.txt` without typing its full name. Return to the working copy.

**Keys**
- `:w` — save (short command; `Tab` lists command suggestions after `:`).
- `Space e` — file explorer in the workspace directory.
- `Space f` — fuzzy file picker; type part of a filename to filter.
- `Up` / `Down` or `Shift+Tab` / `Tab` — choose an entry.
- `Enter` — open the selected file.

**Steps**
1. Save `work-helix.txt` with `:w` → `Enter`.
2. Press `Space`, then `e`. The file explorer opens.
3. Type `notes` to filter the list. Use `Up` / `Down` if needed. Select `notes-helix.txt` with `Enter`.
4. Press `Space`, then `f`. Type `work` (not the full filename).
5. Select `work-helix.txt` with `Tab` / `Down`, then `Enter`.

**Check:** `work-helix.txt` is active. No `:open` command was used.

**Try:** `Space e` also shows directories. Select a directory and press `Enter` to open it. `Space f` searches for files recursively and filters results as you type.

### 5. Use buffers (tab-like navigation)

**Goal:** open `source.txt`; switch between loaded documents.

**Keys**
- `Space e` — explore files without entering paths.
- `Space b` — select an already open buffer; filter by name.
- `ga` — switch to the last used buffer.
- `gn` / `gp` — next / previous open buffer.
- `Tab` / `Shift+Tab`, `Enter` — choose and open a buffer.

**Steps**
1. Press `Space e`; filter with `source`; select `source.txt` and press `Enter`.
2. Press `ga` to return to `work-helix.txt`; press `ga` again for `source.txt`.
3. Press `gn`, then `gp`. Check the filename after each move.
4. Press `Space b`; type `work` to filter the buffer list. Select `work-helix.txt` and press `Enter`.

**Check:** `work-helix.txt` is active.

**Note:** Helix uses **buffers**. `gn` / `gp` switch buffers without a mouse; `Space b` filters them by name. A buffer list is not displayed as tabs by default.

### 6. Open a file in a vertical split

**Goal:** show `work-helix.txt` and `source.txt` side by side, without typing `:vsplit`.

**Keys**
- `Space f` — find a file by part of its name.
- `Ctrl+v` **in the picker** — open the selected file in a vertical split.
- `Ctrl+w v` — another method: split the current file into two views.
- `Ctrl+w h` / `Ctrl+w l` — move left / right.
- `Ctrl+w q` — close the focused split.

**Steps**
1. With `work-helix.txt` active, press `Space f`.
2. Type `source`. Select `source.txt` from the filtered list.
3. Press `Ctrl+v` **instead of Enter**. `source.txt` opens in a right-hand split.
4. Press `Ctrl+w h` (left), then `Ctrl+w l` (right).
5. With `source.txt` active, press `Ctrl+w q` to close that view.

**Check:** only `work-helix.txt` remains visible.

**Alternative:** `Ctrl+w v` creates a vertical split of the current file. Then use `Space f` → `source` → `Enter` in the new view.

**Continue:** return to `work-helix.txt` before Part II.

---


# Part II — One operation at a time

### 7. Move through text

**Goal:** move in a file, line, and word. Do not change text.

**Keys**
- `gg` / `ge` — file start / end.
- `gh` / `gl` — line start / end.
- `w` / `b` — next / previous word start; `w` may select traversed text.
- `e` — word end.
- `;` — collapse a selection to one cursor.
- `h` / `l` — one character left / right.

**Steps**
1. Press `ge`, then `gg`.
2. Press `5j` to reach `The first observation ...`.
3. Press `gl`, then `gh`.
4. Press `w`, inspect the selection, then press `;`.
5. Press `w`, `b`, and `e` to move between word boundaries.

**Check:** no text changed.

### 8. Jump by line number

**Goal:** move to an exact line and then by a relative number of lines.

**Keys**
- `6G` — go to line 6 (number + uppercase `G`).
- `3j` / `3k` — move three lines down / up.

**Steps**
1. Press `6G`.
2. Press `3j`, then `3k`.

**Check:** line 6 → line 9 (`Stations`) → line 6.

### 9. Replace a character — manual position

**Goal:** change `Station X: remove` to `Station Y: remove` without search.

**Keys**
- `13G` — go to line 13.
- `gh` — line start.
- `l` — one character right.
- `r` + character — replace the character under the cursor.

**Steps**
1. Press `13G`, then `gh`.
2. Press `l` **eight times** to reach `X`.
3. Press `r`, then uppercase `Y`.

**Check:** `Station Y: remove`.

### 10. Search for text

**Goal:** find three `TODO` labels. Do not edit them.

**Keys**
- `/` — search forward.
- `n` / `N` — next / previous result.

**Steps**
1. Press `/`, enter `TODO`, press `Enter`.
2. Press `n` twice, then `N` once.

**Check:** three unchanged `TODO` labels.

### 11. Find a nearby character; replace it

**Goal:** learn local character motions; return `Station Y` to `Station X`.

**Keys**
- `f` + character — jump **to** the next character (selects it).
- `t` + character — jump **before** the next character.
- `F` + character — jump **to** the previous character.
- `T` + character — jump **after** the previous character.
- `;` — collapse the selection to its cursor.
- `r` + character — replace one selected character.

**Steps**
1. `/Bridge width:` → `Enter`, then `gh`.
2. Press `f(`; then `;`. Press `F:`; then `;`.
3. Press `t(`; then `;`. Press `gl`, then `T:`; then `;`.
4. `/Station Y:` → `Enter`, then `gh`.
5. Press `fY`, then `rX`.

**Check:** `Station X: remove` again.

**Note:** unlike a full-file search (`/`), `f` / `t` move to a nearby character. They may cross a line boundary.

### 12. Select and replace one word

**Goal:** change `wooden` to `stone`.

**Keys**
- `/` — find a word.
- `miw` — select the word under the cursor.
- `c` — change selection; enter Insert mode.
- `Esc` — Normal mode.

**Steps**
1. `/wooden` → `Enter`.
2. Press `miw`; the full word is selected.
3. Press `c`, type `stone`, press `Esc`.

**Check:** `The first observation was near a stone bridge.`

### 13. Select and delete one word

**Goal:** remove `obsolete` from the quality field.

**Keys**
- `/` — find a word.
- `miw` — select a whole word.
- `d` — delete selection.

**Steps**
1. `/obsolete` → `Enter`.
2. Press `miw`, then `d`.

**Check:** the line contains `Quality flag:` with an empty value.

### 14. Delete one complete line

**Goal:** remove `Station X: remove`, including its line break.

**Keys**
- `/` — search.
- `x` — select a complete line.
- `d` — delete selection.

**Steps**
1. `/Station X: remove` → `Enter`.
2. Press `x`, then `d`.

**Check:** `Station X` is gone. `Measurements` remains.

### 15. Duplicate a complete line

**Goal:** create a second `Station C: pending` line.

**Keys**
- `/` — search.
- `x` — select the current line.
- `y` — copy selection.
- `p` — paste after selection.

**Steps**
1. `/Station C: pending` → `Enter`.
2. Press `x`, then `y`, then `p`.

**Check:** two adjacent `Station C: pending` lines.

### 16. Change a letter in the copied line

**Goal:** change **only the second** `Station C` to `Station D`.

**Keys**
- `gg` — file start.
- `/` / `n` — find first / next match.
- `gh` — line start.
- `f` + character — jump to a letter.
- `r` + character — replace one letter.

**Steps**
1. Press `gg`; `/Station C: pending` → `Enter`.
2. Press `n` to select the **second** match.
3. Press `gh`, then `fC`, then `rD`.

**Check:** `Station C: pending` and `Station D: pending`.

### 17. Select and delete a block

**Goal:** remove the complete `Draft` section, including its blank line.

**Keys**
- `/` — find a section.
- `x` — select a full line; repeat to extend selection down.
- `d` — delete selection.

**Steps**
1. `/Draft` → `Enter`.
2. Press `x` **four times**.
3. Press `d`.

**Check:** `Draft` and both `REMOVE` lines are gone; `Summary` remains.

### 18. Replace text inside brackets and quotes

**Goal:** replace values, not the surrounding characters.

**Keys**
- `/` — find the value.
- `mi(` / `mi[` / `mi"` — select only text **inside** parentheses / brackets / quotes.
- `c` — replace selection and enter Insert mode.
- `Esc` — Normal mode.

**Steps**
1. `/3 m` → `Enter`; press `mi(`, then `c`, type `4 m`, press `Esc`.
2. `/2 m` → `Enter`; press `mi[`, then `c`, type `5 m`, press `Esc`.
3. `/cloudy` → `Enter`; press `mi"`, then `c`, type `sunny`, press `Esc`.

**Check:**

```text
Bridge width: (4 m)
Lake depth: [5 m]
Weather: "sunny"
```

### 19. Delete only the text inside braces

**Goal:** remove `temporary`; keep `{}`.

**Keys**
- `/` — find the value.
- `mi{` — select only text inside `{ }`.
- `d` — delete selection.

**Steps**
1. `/temporary` → `Enter`.
2. Press `mi{`, then `d`.

**Check:** `Unused value: {}`.

### 20. Undo and redo

**Goal:** reverse the last edit and restore it.

**Keys**
- `u` — undo.
- `U` — redo.

**Steps**
1. Press `u`: `temporary` returns.
2. Press `U`: `temporary` disappears again.

**Check:** `Unused value: {}`.

---


# Part III — Combined operations

### 21. Update repeated statuses

**Goal:** update all task and station statuses; finish the quality field.

**Keys**
- `%` — select the whole file.
- `s` — select all matches in the selection.
- `c` — change all selected matches; enter Insert mode.
- `Esc` — Normal mode.
- `,` — remove extra cursors/selections.
- `/` — search.
- `A` — insert at the end of a line.

**Steps**
1. Press `%`, then `s`; type `TODO` → `Enter`.
2. Press `c`, type `DONE`, press `Esc`, then `,`.
3. Press `%`, then `s`; type `pending` → `Enter`.
4. Press `c`, type `checked`, press `Esc`, then `,`.
5. `/Quality flag:` → `Enter`; press `A`, type `checked`, press `Esc`.

**Check:** three `DONE` labels, four `Station ... checked` lines, `Quality flag: checked`.

### 22. Edit several lines at once

**Goal:** create a bullet list and add ` | GPS` to all four stations.

**Keys**
- `/` — search for the first line.
- `gh` — line start.
- `C` — copy the cursor/selection to the line below.
- `I` / `A` — insert at the start / end of all selected lines.
- `Esc` — Normal mode.
- `,` — keep only the main cursor.

**Steps**
1. `/Inspect the bridge.` → `Enter`, then `gh`.
2. Press `C` **twice**; press `I`; type `- ` once; press `Esc`, then `,`.
3. `/Station A: checked` → `Enter`, then `gh`.
4. Press `C` **three times**; press `A`; type ` | GPS` once; press `Esc`, then `,`.

**Check:** three `- ` checklist lines; all four station lines end in ` | GPS`.

### 23. Create a report from selected lines

**Goal:** copy the completed checklist to a **new file** without retyping it.

**Keys**
- `/` — find the first checklist item.
- `gh` — line start.
- `x` — select full lines.
- `y` / `p` — copy / paste.
- `:new` — create an empty buffer (choose it from `:` suggestions with `Tab`).
- `:w FILE` — save as a new filename (short `write` command).
- `Space b` — return to a buffer by choosing it from the list.

**Steps**
1. `/Inspect the bridge.` → `Enter`, then `gh`.
2. Press `x` **three times**, then `y`.
3. Press `:`; type `ne`. Use `Tab` to select `new`, then `Enter`. Press `p` to paste the three lines.
4. Press `gg`, then uppercase `O`; type `Field checklist`; press `Esc`.
5. Type `:w report-helix.txt` → `Enter`. The new filename is entered only once.
6. Press `Space b`, filter with `work`, select `work-helix.txt`, press `Enter`.

**Check:** `report-helix.txt` has one heading and three bullet items.

### 24. Compare original and edited files

**Goal:** verify the changes in two panels without changing `source.txt`.

**Keys**
- `:w` — save (short command; `Tab` shows suggestions in the `:` prompt).
- `Space f` → `Ctrl+v` — find a file and open it in a vertical split.
- `Ctrl+w h` / `Ctrl+w l` — focus left / right panel.
- `/` — find text.
- `Ctrl+w q` — close a panel.

**Steps**
1. Save `work-helix.txt` with `:w` → `Enter`.
2. Press `Space f`, type `source`, select `source.txt`, press `Ctrl+v`.
3. In `work-helix.txt`, search for `stone bridge`.
4. Switch to `source.txt`; search for `wooden bridge`.
5. Check the four stations and the three checklist lines in both files.
6. Close the `source.txt` panel with `Ctrl+w q`. Leave `work-helix.txt` saved.

**Check:** `source.txt` contains the original text; `work-helix.txt` contains the edits.

## Help

From the terminal: `hx --tutor`.

**References:** [Helix master keymap](https://docs.helix-editor.com/master/keymap.html) · [Pickers](https://docs.helix-editor.com/master/pickers.html) · [Word completion](https://docs.helix-editor.com/master/editor.html#editorword-completion-section)
