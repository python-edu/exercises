# Environment management — exercises

> Topics: `venv`, `pip`, `requirements.txt`, shell history, Git.
> Use only `ipython`. Do not install other packages.

# 1. Inspect `proj1`

- Activate `~/python_course/projects/proj1/env`.
- Check the Python and pip versions.
- List installed packages.
- Find the IPython version and installation directory.
- Deactivate the environment.

**Check:** IPython is installed in `~/python_course/projects/proj1/env`.

# 2. Create `proj2`

- Create `~/python_course/projects/proj2`.
- Create `env` with `--prompt proj2` and `--upgrade-deps`.
- Activate the environment.
- Check the pip version and installed packages.
- Check whether IPython is installed.

**Check:** `~/python_course/projects/proj2/env` is independent of `~/python_course/projects/proj1/env`.

# 3. Create two requirements files

In `~/python_course/projects/proj1`:

- Create `requirements.txt` manually. Enter only `ipython`, without a version.
- Save the installed packages and exact versions to `requirements_frozen.txt` using `pip freeze`.
- Compare both files.

**Check:** `requirements.txt` has one line. The frozen file also contains dependencies.

# 4. Install packages from a file

In `~/python_course/projects/proj2`, with `env` active:

- Install packages from `~/python_course/projects/proj1/requirements.txt`.
- Check the IPython installation.
- List packages and check dependencies.

**Check:** IPython works in `~/python_course/projects/proj2/env`.

# 5. Compare environments

- Open two terminal tabs.
- Activate `~/python_course/projects/proj1/env` in the first and `~/python_course/projects/proj2/env` in the second.
- Compare Python and pip versions and installed packages.
- Uninstall IPython only from `~/python_course/projects/proj2/env`.
- Check whether IPython remains installed in `~/python_course/projects/proj1/env`.
- Restore IPython in `~/python_course/projects/proj2/env` from `requirements.txt`.

**Check:** changing one environment does not change the other.

---

# Document your work

Use your **`student-work` Git repository** for course results. Store tasks by lab (`lab1`, `lab2`, ...), not by Python project. Keep Python projects in `projects/`.

For this exercise, save in `lab2/`:

- `results.txt` — terminal commands used in the exercise.
- `requirements.txt` — the manually selected packages.
- `requirements_frozen.txt` — installed packages with versions.

The shell's `history` shows commands, **not command results**. It records the current terminal session; other tabs have their own history.

## 1. Prepare the archive

In the **Archive terminal**, open the course repository and its `lab2` directory:

```sh
cd ~/python_course/student-work
ls ~/python_course/student-work/lab2
```

## 2. Save terminal history

In the terminal used for the exercises, display the command history:

**Windows PowerShell 7 / Linux Bash:**

```sh
history
```

**macOS Zsh:** `history 1` shows the full available history (plain `history` normally shows only the last 16 entries).

```sh
history 1
```

Save the history from the working terminal. These paths work from any current directory:

**Windows — PowerShell 7:** `(history).CommandLine` saves full commands without table columns.

```powershell
(history).CommandLine > ~/python_course/student-work/lab2/results.txt
```

**Linux — Bash:**

```bash
history > ~/python_course/student-work/lab2/results.txt
```

**macOS Zsh:**

```sh
history 1 > ~/python_course/student-work/lab2/results.txt
```

If you used a second terminal for Exercise 5, **append** its history to the same file. These paths also work from any current directory:

**Windows — PowerShell 7:**

```powershell
(history).CommandLine >> ~/python_course/student-work/lab2/results.txt
```

**Linux — Bash:**

```bash
history >> ~/python_course/student-work/lab2/results.txt
```

**macOS Zsh:**

```sh
history 1 >> ~/python_course/student-work/lab2/results.txt
```

In the **Archive terminal**, open `~/python_course/student-work/lab2/results.txt` in your editor. Keep the commands related to the exercises. Remove unrelated entries.

## 3. Save requirements

In the **Archive terminal**, copy both files from `proj1` to the archive:

```sh
cp ~/python_course/projects/proj1/requirements.txt ~/python_course/student-work/lab2/requirements.txt
cp ~/python_course/projects/proj1/requirements_frozen.txt ~/python_course/student-work/lab2/requirements_frozen.txt
```

## 4. Commit the results

In the **Archive terminal**, save the three files in Git:

```sh
cd ~/python_course/student-work
git status
git add lab2/results.txt lab2/requirements.txt lab2/requirements_frozen.txt
git commit -m "lab2: environment management exercises 1-5"
# or
git commit --message "lab2: environment management exercises 1-5"
```

Run **one** commit command. Do not add environment directories to Git.

Git paths such as `lab2/results.txt` are relative to `~/python_course/student-work`.

## 5. Check the archive

Show the commits for this exercise:

```sh
cd ~/python_course/student-work
git log --oneline -- lab2/
```

Show the saved command history. In `git show`, `lab2/results.txt` is a path inside the commit, not a system path:

```sh
cd ~/python_course/student-work
git show HEAD:lab2/results.txt
```

The files stay in `~/python_course/student-work/lab2`. Later tasks may overwrite `results.txt`; Git keeps earlier versions.
