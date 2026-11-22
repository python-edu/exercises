# Files and directories

  >- Goal: work with directories and text files from the terminal: navigate, create, inspect, copy, move, rename, and remove.
  >- Systems: Windows (PowerShell 7), Linux (Bash), macOS (Zsh).
  >- All practice files and directories will be created inside `~/shell-practice`.
  >- On Windows, use PowerShell aliases where available to keep commands similar to Bash/Zsh.
  >- An alias calls a PowerShell command by another name. Options and output may differ.

---


# 1. Find your starting location

Open **PowerShell 7** on Windows or a terminal on Linux/macOS. Do not change directories yet.

The *command prompt* may show the current directory, but its appearance depends on your shell and its settings.

>- `pwd` means *print working directory*: it displays the directory you are currently working in.
>- In PowerShell, `pwd` is an alias for `Get-Location`.

```sh
pwd
```

Example output if the terminal starts in the home directory:

**Windows — PowerShell 7:**

```text
Path
----
C:\Users\rs_lab
```

**Linux:**

```text
/home/rs_lab
```

**macOS:**

```text
/Users/rs_lab
```

Compare the result with the path, if any, shown in your prompt. Your starting directory may differ.

>- `ls` lists the files and directories in the current location.
>- In PowerShell, `ls` is an alias for `Get-ChildItem`.

```sh
ls
```

Example output (the names and dates depend on your computer):

**Windows — PowerShell 7:**

```text
    Directory: C:\Users\rs_lab

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----                ...                          Documents
d----                ...                          Downloads
-a---                ...                      24  example.txt
```

- `Mode` starting with `d` — directory.
- `Mode` starting with `-` — file. `Length` shows file size in bytes.

**Linux / macOS:**

```text
Documents  Downloads  example.txt
```

Here `ls` shows names without file types. For details, use `ls -l`:

```sh
ls -l
```

Example output:

```text
drwxr-xr-x  ... Documents
drwxr-xr-x  ... Downloads
-rw-r--r--  ... example.txt
```

- `d` at the start — directory; `-` at the start — file.

These items already exist; you have not created any practice files yet.

---

# 2. Create your practice directory

  >- `~` represents your *home directory*.
  >- `cd` (change directory) changes your current location.

```sh
cd ~
# Check: the displayed path should be your home directory.
pwd
```

Expected path: `C:\Users\rs_lab` (Windows), `/home/rs_lab` (Linux), or `/Users/rs_lab` (macOS).

  >- `mkdir` (*make directory*) creates a directory. Create `shell-practice` directly inside your home directory:

```sh
mkdir shell-practice
# Check: shell-practice should appear in the list.
ls
```

Expected: `shell-practice` appears as a directory. Other home-directory items remain.

Now use `cd` to enter the directory you just created:

```sh
cd shell-practice
# Check: the path should end in shell-practice.
pwd
# Check: this newly created directory should be empty.
ls
```

Expected paths:

- Windows: `C:\Users\rs_lab\shell-practice`
- Linux: `/home/rs_lab/shell-practice`
- macOS: `/Users/rs_lab/shell-practice`

Expected `ls` output: **no entries**.

Stay inside `shell-practice` for the rest of this exercise. `mkdir` is available in all three shells, although
PowerShell and Unix implement it differently.

---


# 3. Create directories and navigate

Use `mkdir` again to create two subdirectories:

```sh
mkdir notes
mkdir archive
# Check: both names should appear.
ls
```

Expected directory structure:

```text
shell-practice/
├── archive/
└── notes/
```

`cd notes` enters the `notes` directory. The path `..` means the *parent directory*, so `cd ..` returns one level up.

```sh
cd notes
# Check: the path should end in shell-practice/notes (or use backslashes on Windows).
pwd
cd ..
# Check: you should be back in shell-practice.
pwd
```

Expected path endings: `shell-practice/notes` and `shell-practice` (Windows uses `\`).

Paths such as `notes` and `archive` are *relative paths*: they are interpreted relative to the current directory.

---


# 4. Create a text file

  >- `echo` writes text to the terminal.
  >- In PowerShell, it is an alias for `Write-Output`; in Bash/Zsh, it is normally a shell built-in.

```sh
echo "First field observation"
```

Output:

```text
First field observation
```

  >- `>` redirects the command's output to a file. If that file does not exist, it is created; if it exists, its contents are replaced.

```sh
echo "First field observation" > report.txt
# Check: report.txt should now exist.
ls
```

Expected directory structure:

```text
shell-practice/
├── archive/
├── notes/
└── report.txt
```

`>` writes to the file; it does not print the text in the terminal.

  >- `>>` appends output to the end of an existing file without replacing its contents.

```sh
echo "Second field observation" >> report.txt
```

  >- `cat` displays the contents of a text file.
  >- In PowerShell, it is an alias for `Get-Content`; on Linux/macOS, it is a separate program.

```sh
# Check: the file should contain the two observations, in order.
cat report.txt
```

Output:

```text
First field observation
Second field observation
```

---


# 5. Copy files

  >- `cp SOURCE DESTINATION` copies an item.
  >- In PowerShell, `cp` is an alias for `Copy-Item`; on Linux/macOS, `cp` is a separate program.

Copy `report.txt` into the existing `notes` directory and give the copy a new filename:

```sh
cp report.txt notes/report-copy.txt
# Check: the original should still be here.
ls
# Check: the copy should appear in notes.
ls notes
# Check: the copy should contain both observations.
cat notes/report-copy.txt
```

Expected directory structure:

```text
shell-practice/
├── archive/
├── notes/
│   └── report-copy.txt
└── report.txt
```

`cat notes/report-copy.txt` displays the same two lines as `cat report.txt`.

---


# 6. Rename and move files

  >- `mv SOURCE DESTINATION` moves an item. If the source and destination are in the same directory, it can **rename** the item.
  >- PowerShell provides `mv` as an alias for `Move-Item`; Linux/macOS provide a separate `mv` program.

Rename the original file:

```sh
mv report.txt report-final.txt
# Check: report-final.txt exists and report.txt no longer does.
ls
```

Expected: `report-final.txt` replaces `report.txt` in the listing.

The same command moves a file between directories:

```sh
mv notes/report-copy.txt archive/report-copy.txt
# Check: notes should now be empty.
ls notes
# Check: archive should contain report-copy.txt.
ls archive
```

Expected directory structure:

```text
shell-practice/
├── archive/
│   └── report-copy.txt
├── notes/
└── report-final.txt
```

`ls notes` displays no entries; `ls archive` lists `report-copy.txt`.
---


# 7. Copy a directory

`cp` can also copy a complete directory. It needs the *recursive* option, which has different spelling in PowerShell and Unix shells.

## Windows — PowerShell 7

  >- `-Recurse` copies the directory's contents, including its subdirectories.

```powershell
cp archive backup -Recurse
```

## Linux/macOS

  >- `-R` copies the directory recursively.

```sh
cp -R archive backup
```

**All systems:** verify that `backup` contains the copied file, while `archive` remains unchanged.

```sh
# Check: both directories should contain report-copy.txt.
ls archive
ls backup
# Check: read the copied file.
cat backup/report-copy.txt
```

Expected directory structure:

```text
shell-practice/
├── archive/
│   └── report-copy.txt
├── backup/
│   └── report-copy.txt
├── notes/
└── report-final.txt
```

`cat backup/report-copy.txt` displays both observation lines.

---


# 8. Filter a directory listing

  >- The symbol `|` is a *pipe*: it passes the output of one command to another.
  >- We will list the contents of `~/shell-practice` and display only names containing report.

## Windows — PowerShell 7

  >- `findstr` displays lines containing a given text.

```powershell
ls ~/shell-practice -Name | findstr report
# Check: only report-final.txt should be displayed.
```

Output:

```text
report-final.txt
```

## Linux/macOS

>- `grep` displays lines containing a given text.

```sh
ls ~/shell-practice | grep report
# Check: only report-final.txt should be displayed.
```

Output:

```text
report-final.txt
```

Both examples display only names containing `report`. The files themselves are unchanged.

---



# 9. Remove files and directories

> **Note:** Removal is destructive. Always check your current directory before deleting files. Remove only items created during this exercise.

## Remove a file

  >- `rm` removes a file.
  >- In PowerShell, `rm` is an alias for `Remove-Item`; on Linux/macOS, it is a separate program.

**All systems:**

```sh
# Check: you are still in shell-practice.
pwd

rm archive/report-copy.txt

# Check: archive should now be empty.
ls archive
```

Expected `ls archive` output: **no entries**. The copy in `backup` remains.

## Remove a directory and its contents

  >- `rm -R` removes a directory recursively, including all files and subdirectories.
  >- In PowerShell, `-R` is short for `-Recurse`. On Linux/macOS, `-R` is the recursive option.

**All systems:**

```sh
rm -R backup

# Check: backup should be gone; archive should remain.
ls

# Check: report-final.txt should still contain both observations.
cat report-final.txt
```

Expected directory structure:

```text
shell-practice/
├── archive/
├── notes/
└── report-final.txt
```

Output of `cat report-final.txt`:

```text
First field observation
Second field observation
```

The `shell-practice` directory and the remaining files should be kept for further exercises.


---


# Find help for a command

## Windows PowerShell

  >- `-?` in Windows, PowerShell 7 displays help for PowerShell cmdlets, including when invoked through an alias such
  as `cp`. 
  >- The `help` command is another way to read this help.

```powershell
cp -?
help cp
```

  >- `gal` is an alias for `Get-Alias`. It shows what a PowerShell alias means.

```powershell
gal cp
```

Expected output:

```text
cp -> Copy-Item
```


## Linux / macOs

  >- `man` on Linux/macOS (*manual*) opens a command's manual page. Press `q` to close it.

```sh
man cp
```

  >- `type` to check what the shell runs when you enter a name.

```sh
type cp
```

Example output: `cp is /usr/bin/cp` (Linux) or `cp is /bin/cp` (macOS).

On many Linux distributions, `cp --help` also works. Do not assume that `-h` or `/?` means help on every system.


---


# Find a program

## Windows — PowerShell 7

  >- `where.exe` finds executable files in the directories listed in `PATH`.
  >- Use `where.exe`, not `where` (`where` is a PowerShell alias for `Where-Object`).

Find PowerShell 7:

```powershell
where.exe pwsh
```

Example output:

```text
C:\Program Files\PowerShell\7\pwsh.exe
```

## Linux / macOS

  >- `command -v` shows the command the shell would run.

Find `ls`:

```sh
command -v ls
```

Example output:

```text
/usr/bin/ls
```

On macOS, the path may be `/bin/ls`.

---


# Environment variables

  >- Environment variables provide settings to programs.
  >- `PATH` — directories searched for commands; separated by `;` on Windows and `:` on Linux/macOS.
  >- `EDITOR` — preferred text editor. It may be unset.

## Windows — PowerShell 7

  >- `$env:NAME` displays the value of an environment variable.

```powershell
echo $env:PATH
echo $env:EDITOR
```

Example output (shortened):

```text
C:\Windows\system32;C:\Windows;C:\Program Files\PowerShell\7;...
micro
```

  >- `ls Env:` lists all environment variables.

```powershell
ls Env:
```

## Linux / macOS

  >- `$NAME` reads an environment variable; `echo` displays it.

```sh
echo $PATH
echo $EDITOR
```

Example output (shortened):

```text
/usr/local/bin:/usr/bin:/bin
micro
```

  >- `env` lists all environment variables.

```sh
env
```

If `EDITOR` is not set, its output is empty.

---


# 10. Independent task

Stay in `shell-practice`. Without copying earlier commands, complete the following:

1. Create the directory `reports`.
2. Create `summary.txt` with two lines of text, using `echo`, `>` and `>>`.
3. Copy it to `reports/summary-copy.txt`.
4. Rename `summary.txt` to `final-summary.txt`.
5. Display both files and compare their contents. Use a pipe to filter the listing for `summary` (`findstr` on Windows, `grep` on Linux/macOS).
6. Remove `reports/summary-copy.txt`, then remove the empty `reports` directory.
7. Check your final location and directory contents.

**Expected final directory structure** (the `archive` directory remains empty):

```text
shell-practice/
├── archive/
├── notes/
├── final-summary.txt
└── report-final.txt
```


## References

- [PowerShell aliases](https://learn.microsoft.com/en-us/powershell/scripting/learn/shell/using-aliases)
- [PowerShell Get-Help](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-help)
- [Windows findstr](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/findstr)
- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [PowerShell environment variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables)
- [Windows where command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
