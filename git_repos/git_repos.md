# Exercise

Build **`gitrepos`** — a terminal application that uses the external tool `fd` to find local Git repositories and
display their status.


| Command | Result |
|---|---|
| `gitrepos` | Scan the home directory, display repositories and select an ID for details |
| `gitrepos --full-paths` | Display absolute paths |
| `gitrepos --help` | Show help |

Example output:

```text
ID  Repository                                 Status   Remote
1   ~/python_course/projects/example_repo1     clean    no
2   ~/python_course/projects/git_repos          changes  no
3   ~/other/example_repo2                      clean    yes

Select repository ID (Enter to quit): 2
```

**Where:**

   >- `ID`- repository's position in the current list
   >- `Status` indicates uncommitted changes
   >- `Remote` indicates whether a remote repository is configured (not necessarily reachable)


### fd
The project uses `fd` to search for files and directories. Some features of `fd` (from the [project website](https://github.com/sharkdp/fd)):

- Supports regular expressions (default) and glob patterns.
- Fast searching using parallel directory traversal.
- Ignores hidden files and directories by default.
- Ignores patterns from `.gitignore` by default.
- The command name is **50% shorter** than `find` :-).


### Supplementary materials

Additional information is available in:

- [subprocess_intro.md](subprocess_intro.md) — running external programs in Python.
- [binary_distribution.md](binary_distribution.md) — including executable files and their licenses in a Python package.

---


# Contents

1. [Project](#1-project)
2. [pyproject.toml](#2-pyprojecttoml)
3. [main.py](#3-mainpy)
   - [`main()`](#main)
   - [Install for development](#install-for-development)
4. [myargs.py](#4-myargspy)
   - [`parse_arguments()`](#parse_arguments)
5. [repos.py](#5-repospy)
   - [`git_command()`](#git_command)
   - [`is_repository()`](#is_repository)
   - [`scan_walk()`](#scan_walk)
   - [`scan_fd()`](#scan_fd)
   - [`scan_repos()`](#scan_repos)
   - [`get_status()` and `has_remote()`](#get_status-and-has_remote)
   - [`show_repos()` and `show_status()`](#show_repos-and-show_status)
   - [`select_repository()`](#select_repository)
6. [Build and install](#6-build-and-install)

---

# 1. Project

## src structure

Create a project named `git_repos` with the `src` layout:

```text
git_repos/                      # project's root directory
├── pyproject.toml
├── LICENSE                     # common text file: gitrepos license
├── src/
│   └── git_repos/              # package directory
│       ├── __init__.py
│       ├── main.py
│       ├── myargs.py
│       ├── repos.py
│       ├── bin/
│       │   └── fd              # binary file: fd.exe on Windows
│       └── licenses/
│           └── LICENSE_fd      # common text file: fd MIT license text
└── ...
```

## Create src

Create the project structure using:

- `projgen` - if already created (see the [repository](https://github.com/python-edu/02python-packaging))
- terminal commands (Windows PowerShell / Linux / macOS):

    ```bash
    mkdir git_repos
    cd git_repos
    mkdir src
    mkdir src/git_repos
    ```


**Notes**

>This project structure differs from the basic structure used earlier in the course:
>- `bin/` stores the `fd` executable; `licenses/` stores its license files.

## Files

- `pyproject.toml` - see below
- License files: see [Binary distribution](binary_distribution.md).
- `fd` executable: see [Binary distribution](binary_distribution.md).
- `main.py` - only `main()`, its invocation and imports
- `myargs.py` - command-line arguments
- `repos.py` - all application functions
- `__init__.py` - empty

---


# 2. pyproject.toml

## Backend: setuptools

```toml
[build-system]
requires = ["setuptools>=80"]
build-backend = "setuptools.build_meta"

[project]
name = "git_repos"
version = "0.1.0"

[project.scripts]
gitrepos = "git_repos.main:main"

[tool.setuptools.package-data]
git_repos = ["bin/*", "licenses/*"]
```

- Automatically finds Python packages in `src/` and includes their `.py` files.
- Does not automatically include all other files inside a package.
- `[tool.setuptools.package-data]` selects additional files for the wheel:
  - `bin/*` - the `fd` executable.
  - `licenses/*` - the `fd` license files.

## Backend: hatchling

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "git_repos"
version = "0.1.0"

[project.scripts]
gitrepos = "git_repos.main:main"
```

- Automatically finds `src/git_repos/` when the package directory matches the project name (`git_repos`).
- Includes `.py` files and other files inside this package and its subdirectories, unless excluded by ignore rules.
- Includes `bin/fd` (or `bin/fd.exe`) and `licenses/` files without additional file patterns.
- If the package directory has a different name, specify it using `packages` in `[tool.hatch.build.targets.wheel]`.


---


# 3. main.py

### main()

1. Function:

   ```python
   def main() -> None:
       """Scan once, display repositories and handle interactive ID selection."""
       print("gitrepos is running")

   if __name__ == "__main__":
       main()
   ```

2. Steps:

   - Activate the virtual environment.
   - Install `ipython` to develop and test functions.
   - Install the application (see below).
   - Run the first test.
   - Implement the next functions and update `main()` step by step.


### Install for development

After creating `pyproject.toml`, `src/git_repos/__init__.py` and `src/git_repos/main.py`, install the project in the
active virtual environment:

Windows (PowerShell):

```powershell
.\env\Scripts\activate
```

Linux / macOS:

```bash
source env/bin/activate
```

Install IPython and the project:

```bash
python -m pip install ipython
python -m pip install -e .
```

- `-e` - editable installation. Python uses the project source files, so changes to `.py` files do not require reinstallation.
- Implement and test the functions one by one.
- Reinstall after changing installation settings such as `[project.scripts]`.

Test the entry point:

```bash
gitrepos
```

Expected output: `gitrepos is running`.


---

# 4. myargs.py

### parse_arguments()

1. Function:

   ```python
   def parse_arguments() -> argparse.Namespace:
       """Read the --full-paths option and return the parsed arguments."""
       pass
   ```

2. Script arguments:

   - Create an `ArgumentParser`.
   - Add one optional flag:

   ```python
   parser.add_argument("-f", "--full-paths", action="store_true")
   ```

   - Return the result of `parser.parse_args()`.

3. Tests:

   With `main()` calling `parse_arguments()`:

   ```bash
   gitrepos -h
   ```


---


# 5. repos.py

### git_command()

>Read [subprocess_intro.md](subprocess_intro.md) file!

1. Function:

   ```python
   def git_command(*arguments: str, pth: str | None = None) -> subprocess.CompletedProcess[str]:
       """Run Git in pth (or the current directory) and return its result."""
       pass
   ```

2. Command:

   ```python
   command = ["git", *arguments]
   ```

   - `git` - run the Git program.
   - `*arguments` - additional Git arguments.

3. Steps:

   - Use `pth` as `cwd`; if `pth` is `None`, use `Path.cwd()`.
   - Run `command` using `subprocess.run()`.
   - Capture output as text (`capture_output=True`, `text=True`).
   - Return the `CompletedProcess` object. Its `returncode` indicates success or failure.

---

### is_repository()

1. Function:

   ```python
   def is_repository(path: Path) -> bool:
       """Check whether the given directory is the top-level Git working tree."""
       pass
   ```

2. Git command:

   ```text
   rev-parse --show-toplevel
   ```

   - `rev-parse` - query Git repository information.
   - `--show-toplevel` - print the path to the top-level working-tree directory.

3. Steps:

   - Check whether `.git` exists in `path`. It may be a directory or a file (Git worktrees).
   - Run the command using `git_command()`.
   - Check that Git succeeded (`returncode == 0`).
   - Use `stdout.strip()` to remove the newline from the returned directory.
   - Compare the returned directory with `path` (use `Path.resolve()`).
   - Return `True` only when both paths match. A subdirectory of another repository is not a separate repository.

---

### scan_walk()

1. Function:

   ```python
   def scan_walk(search_dir: Path) -> set[Path]:
       """Find Git repositories under a directory using os.walk()."""
       pass
   ```

2. Steps:

   - Use `os.walk(search_dir)` to visit directories.
   - Look for `.git` in both subdirectory names and file names.
   - Do not search inside `.git` directories:

   ```python
   for directory, subdirectories, files in os.walk(search_dir):
       if ".git" in subdirectories:
           repos.append(directory)
           subdirectories.clear()  # empty []
   ```

   - For each candidate directory (with a `.git` directory or file), call `is_repository()`.
   - Return a `set` of `Path` objects (no duplicates).

3. Test in IPython:

   ```python
   from pathlib import Path
   from git_repos.repos import scan_walk

   scan_walk(Path.home())
   ```

---

### scan_fd()

>Read [binary_distribution.md](binary_distribution.md) file!

Before defining `scan_fd()`, locate the bundled `fd`. - to zdanie nie jest jane ze względu na bundled! Add these lines at the beginning of `repos.py`, outside any function:

```python
import os
from importlib.resources import files

FD_NAME = "fd.exe" if os.name == "nt" else "fd"
FD_PATH = files("git_repos").joinpath("bin", FD_NAME)
```

- `FD_NAME` - executable name for the current operating system.
- `FD_PATH` - location of `fd` inside the installed package; set when `repos.py` is imported.
- See [Binary distribution](binary_distribution.md) for an explanation of `files()` and `joinpath()`.

1. Function:

   ```python
   def scan_fd(search_dir: Path) -> set[Path]:
   tutaj też opis z budnled nie jest jasny
       """Search a directory with the bundled fd and return verified Git repository paths."""
       pass
   ```

   - `search_dir` - directory to search, for example `Path.home()`.

2. Prepare `fd`:

   - Download the executable for the target platform.
   - Extract the archive and copy `fd` or `fd.exe` into `src/git_repos/bin/`.
   - Copy the MIT license to `src/git_repos/licenses/LICENSE_fd`.
   - Test the executable.
   - See [Binary distribution](binary_distribution.md).

3. Search command:

   ```python
   arguments = [str(FD_PATH), "-H", "-I", "-g", ".git", str(search_dir)]
   ```

4. Steps:

   - Run `arguments` using `subprocess.run()` and capture output as text.
   - Use `check=True` so a nonzero exit code raises `subprocess.CalledProcessError`.
   - Split the output into paths to `.git` files or directories.
   - For each result, take the parent directory and check it using `is_repository()`.
   - Return a `set` of verified repository paths. No matches means an empty set, not an error.

---

### scan_repos()

1. Function:

   ```python
   def scan_repos(search_dir: Path) -> set[Path]:
   ten docstring jest niezrozumiały!!!
       """Find Git repositories with the bundled fd or fall back to os.walk()."""
       pass
   ```

2. Steps:

   - Call `scan_fd(search_dir)` inside `try` and return its result. It uses the module-level `FD_PATH`.
   - Catch `OSError` if `fd` cannot start, or `subprocess.CalledProcessError` if it fails.
   - On failure, print `Warning: fd unavailable; using slower os.walk().` and return `scan_walk(search_dir)`.

3. Test in IPython:

   ```python
   from pathlib import Path
   from git_repos.repos import scan_repos

   scan_repos(Path.home())
   ```

---

### get_status() and has_remote()

1. Function:

   ```python
   def get_status(path: Path) -> str:
       """Return 'clean' or 'changes' depending on uncommitted Git changes."""
       pass

   def has_remote(path: Path) -> bool:
       """Check whether at least one remote repository is configured."""
       pass
   ```
  > Zauważ: Obie funkcje uruchamiają komendy git w wybranym repozytorium (see subprocess_intro#Run Git in a selected directory)

2. Short status:
  
   - In `get_status()`, run `git_command("status", "--porcelain")`.
   - Return `clean` if the output is empty; otherwise return `changes`.
   - In `has_remote()`, run `git_command("remote")`.
   - Return `True` if the output contains a remote name; otherwise return `False`.
   - Check `returncode` before interpreting the output. A failed Git command does not mean `clean` or `no`.

3. Git commands:

   | Arguments passed to `git_command()` | Meaning |
   |---|---|
   | `status --porcelain` | Empty output: `clean`; otherwise: `changes` |
   | `remote` | Empty output: `no`; otherwise: `yes` |

   `--porcelain` produces a stable format for programs. A configured remote does not mean that it is reachable.

---

### show_repos() and show_status()

1. Function:

   ```python
   def show_repos(paths: list[Path], full_paths: bool = False) -> None:
       """Display numbered repositories with their paths and short Git statuses."""
       pass

   def show_status(path: Path) -> None:
       """Display Git changes and remote addresses for one selected repository."""
       pass
   ```

2. Repository list - `show_repos()`:

   - Use `enumerate(paths, start=1)` to assign IDs.
   - Display `ID`, `Repository`, `Status` and `Remote`.
   - For each path, call `get_status()` and `has_remote()`.
   - Display `~/` for paths inside the home directory, unless `full_paths` is `True`.

3. Detailed report - `show_status()`:

   - Display the selected repository path.
   - Run `git status` and display its output: current branch, committed/uncommitted state and changed or untracked files.
   - Run `git remote -v` and display remote names and URLs. If there is no remote, display `No remote configured.`

   The report can use the Git output directly; no custom parsing of detailed changes is needed.

---

### select_repository()

1. Function:

   ```python
   def select_repository(paths: list[Path]) -> Path | None:
       """Read an ID and return its repository path, or None to quit."""
       pass
   ```

2. Interactive selection:

   ```text
   Select repository ID (Enter to quit):
   ```

   - Read input using `input()` and remove surrounding spaces with `strip()`.
   - If the input is empty, return `None`.
   - Convert the input to an integer and check that `1 <= ID <= len(paths)`.
   - For a valid ID, return `paths[ID - 1]`.
   - For invalid input, display a message and ask again.

---


# 6. Build and install

>Read [binary_distribution.md](binary_distribution.md) file!

1. Build the wheel (`.whl` file):

   ```bash
   python -m build --wheel
   ```

2. Install the `wheel` tool and set the platform tag:

   ```bash
   python -m pip install wheel
   python -m wheel tags --platform-tag=PLATFORM_TAG --remove dist/FILE.whl
   ```

   - Select `PLATFORM_TAG` for the `fd` executable included in the wheel.
   - `FILE.whl` is the filename produced by the build command.
   - See [Binary distribution](binary_distribution.md) for platform tags.

3. Check the wheel contents:

   ```bash
   python -m zipfile -l dist/TAGGED_FILE.whl
   ```

   - Check for `git_repos/bin/fd` (or `fd.exe`) and `git_repos/licenses/LICENSE_fd`.
   - See [Binary distribution](binary_distribution.md) for the wheel format and `zipfile`.

4. Leave the project virtual environment and install the wheel with `pipx`:

   ```bash
   pipx install dist/TAGGED_FILE.whl
   gitrepos
   ```
