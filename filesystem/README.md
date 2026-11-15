# 01 — Files and directories

**Goal:** work with directories and text files from the terminal: navigate, create, inspect, copy, move, rename, and remove.

**Systems:** Windows (PowerShell 7), Linux (Bash), macOS (Zsh).

Use the same terminal window throughout the exercise. **All practice files and directories will be created inside `~/shell-practice`. Do not delete that directory at the end.**

## 1. Find your starting location

Open **PowerShell 7** on Windows or a terminal on Linux/macOS. Do not change directories yet.

The *command prompt* may show the current directory, but its appearance depends on your shell and its settings.

`pwd` means *print working directory*: it displays the directory you are currently working in.

```sh
pwd
```

Compare the result with the path, if any, shown in your prompt.

`ls` lists the files and directories in the current location.

```sh
ls
```

These items already exist; you have not created any practice files yet.

**Why do these short commands work on different systems?** In PowerShell, `pwd` and `ls` are *aliases* (short names) for `Get-Location` and `Get-ChildItem`. In Bash/Zsh, the same names invoke different shell commands or programs. The names are similar, but the implementations differ.

## 2. Create your practice directory

`~` represents your *home directory*. The command `cd` (*change directory*) changes your current location.

```sh
cd ~
# Check: the displayed path should be your home directory.
pwd
```

`mkdir` (*make directory*) creates a directory. Create `shell-practice` directly inside your home directory:

```sh
mkdir shell-practice
# Check: shell-practice should appear in the list.
ls
```

Now use `cd` to enter the directory you just created:

```sh
cd shell-practice
# Check: the path should end in shell-practice.
pwd
# Check: this newly created directory should be empty.
ls
```

Stay inside `shell-practice` for the rest of this exercise. `mkdir` is available in all three shells, although PowerShell and Unix implement it differently.

## 3. Create directories and navigate

Use `mkdir` again to create two subdirectories:

```sh
mkdir notes
mkdir archive
# Check: both names should appear.
ls
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

Paths such as `notes` and `archive` are *relative paths*: they are interpreted relative to the current directory.

## 4. Create a text file

`echo` writes text to the terminal. In PowerShell, it is an alias for `Write-Output`; in Bash/Zsh, it is normally a shell built-in.

```sh
echo "First field observation"
```

The symbol `>` redirects the command's output to a file. If that file does not exist, it is created; if it exists, its contents are replaced.

```sh
echo "First field observation" > report.txt
# Check: report.txt should now exist.
ls
```

The symbol `>>` appends output to the end of an existing file without replacing its contents.

```sh
echo "Second field observation" >> report.txt
```

`cat` displays the contents of a text file. In PowerShell, it is an alias for `Get-Content`; on Linux/macOS, it is a separate program.

```sh
# Check: the file should contain the two observations, in order.
cat report.txt
```

### Create an empty file

A file can also be created without adding text. The commands for this differ between platforms; no custom alias or shell function is needed.

**Windows — PowerShell 7:** `New-Item` creates an item; `-ItemType File` specifies a file rather than a directory.

```powershell
New-Item -ItemType File empty.txt
```

**Linux/macOS:** `touch` creates a file if it does not already exist (for an existing file it updates its timestamp).

```sh
touch empty.txt
```

**All systems:** check the result with `ls`. `empty.txt` should appear alongside `report.txt`.

```sh
ls
```

## 5. Copy files

`cp SOURCE DESTINATION` copies an item. The original remains in place. In PowerShell, `cp` is an alias for `Copy-Item`; on Linux/macOS, `cp` is a separate program.

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

### Find help for a command

**Windows — PowerShell 7:** `-?` displays help for PowerShell cmdlets, including when invoked through an alias such as `cp`. The `help` command is another way to read this help.

```powershell
cp -?
help cp
```

To discover what an alias means, use `Get-Alias`:

```powershell
Get-Alias cp
```

**Linux/macOS:** `man` (*manual*) opens a command's manual page. Press `q` to close it.

```sh
man cp
```

To check what the shell runs when you enter a name, use `type`:

```sh
type cp
```

On many Linux distributions, `cp --help` also works. Do not assume that `-h` or `/?` means help on every system.

## 6. Rename and move files

`mv SOURCE DESTINATION` moves an item. If the source and destination are in the same directory, it can **rename** the item. PowerShell provides `mv` as an alias for `Move-Item`; Linux/macOS provide a separate `mv` program.

Rename the original file:

```sh
mv report.txt report-final.txt
# Check: report-final.txt exists and report.txt no longer does.
ls
```

The same command moves a file between directories:

```sh
mv notes/report-copy.txt archive/report-copy.txt
# Check: notes should now be empty.
ls notes
# Check: archive should contain report-copy.txt.
ls archive
```

## 7. Copy a directory

`cp` can also copy a complete directory. It needs the *recursive* option, which has different spelling in PowerShell and Unix shells.

**Windows — PowerShell 7:** `-Recurse` copies the directory's contents, including its subdirectories.

```powershell
cp archive backup -Recurse
```

**Linux/macOS:** `-R` copies the directory recursively.

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

## 8. Filter a directory listing

The symbol `|` is a *pipe*: it passes the output of one command to another. Here, we will filter the names displayed by `ls` without changing any files.

**Windows — PowerShell 7:** `findstr` displays lines containing a given text. The `-Name` option makes `ls` output just the file and directory names.

```powershell
ls -Name | findstr report
# Check: only report-final.txt should be displayed.
```

**Linux/macOS:** `grep` displays lines containing a given text.

```sh
ls | grep report
# Check: only report-final.txt should be displayed.
```

Both examples display only names containing `report`. The files themselves are unchanged.

## 9. Remove files and directories

**Removal is destructive.** Check `pwd` before running any removal command. Remove only items created in `shell-practice`.

`rm` removes a file. In PowerShell it is an alias for `Remove-Item`; on Linux/macOS it is a separate program.

```sh
# Check: you are still in shell-practice.
pwd
rm archive/report-copy.txt
# Check: archive should be empty.
ls archive
```

`rmdir` removes an **empty directory** (in PowerShell it is an alias for `Remove-Item`). Since `notes` is empty, remove it:

```sh
rmdir notes
# Check: notes should no longer appear.
ls
```

To remove a directory **together with its contents**, use a recursive option. Remove only `backup`.

**Windows — PowerShell 7:**

```powershell
rm backup -Recurse
```

**Linux/macOS:**

```sh
rm -R backup
```

**All systems:** inspect what remains.

```sh
# Check: backup should be gone; archive should remain.
ls
# Check: report-final.txt should still have both observations.
cat report-final.txt
```

## 10. Independent task

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
├── empty.txt
├── final-summary.txt
└── report-final.txt
```

**Do not remove `shell-practice`.** You may use it for later terminal exercises.

## References

- [PowerShell aliases](https://learn.microsoft.com/en-us/powershell/scripting/learn/shell/using-aliases)
- [PowerShell Get-Help](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-help)
- [Windows findstr](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/findstr)
- [GNU Coreutils manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)
