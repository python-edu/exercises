# `subprocess` — Running External Programs

`subprocess` ([see Python documentation](https://docs.python.org/3/library/subprocess.html)) is part of the Python standard library. It allows Python to run external programs, such as `git` and `fd`.

**`subprocess.run()` is the recommended function** for running a program and waiting for it to finish. More advanced tasks may require `subprocess.Popen()`.

In [`gitrepos`](git_repos.md), we use `subprocess` to:

- run Git commands and read their results
- run `fd` to find Git repositories
- detect failures of external programs

## 1. `subprocess.run()`

Basic example:

```python
import subprocess

result = subprocess.run(["git", "--version"])
```

- `run()` starts the program and waits until it finishes.
- The first list element is the program name; the following elements are its arguments.
- Without output capture, Git prints its result directly in the terminal.
- `result` is a `CompletedProcess` object.

### Main arguments

| Argument | Meaning |
|---|---|
| `args` | Program name and arguments, usually as a list, e.g. `["git", "--version"]` |
| `capture_output=True` | Capture normal output and error output instead of displaying them |
| `text=True` | Read captured output as strings instead of bytes |
| `cwd=directory` | Set the working directory of the external program |
| `check=True` | Raise an exception if the program ends with a nonzero exit code |
| `timeout=seconds` | Stop waiting after the specified number of seconds |

- Only `args` is required. Other arguments are optional.
- Pass commands as lists, **not** joined strings. This also handles paths containing spaces.
- The default is `shell=False`; we do not need `shell=True` for `git` or `fd`.

## 2. Capture the output

```python
result = subprocess.run(
    ["git", "--version"],
    capture_output=True,
    text=True,
)

print(result.stdout)
print(result.stderr)
print(result.returncode)
```

| Result attribute | Meaning |
|---|---|
| `result.stdout` | Normal output of the program |
| `result.stderr` | Error output of the program |
| `result.returncode` | Exit code: usually `0` for success |

TU trzeba podkreślić bo chyba nie ma tego nigdzie indziej jak i do czego użyć returncode i dlaczego jest napisane usually a nie zawsze gdy jest ok?

Use `strip()` to remove whitespace at the beginning and end of a string, including the final newline:

```python
print(result.stdout.strip())
```

**Try:** Remove `text=True` and inspect the type of `result.stdout`.

## 3. Check the result

Run Git with an invalid option:

```python
result = subprocess.run(
    ["git", "--invalid-option"],
    capture_output=True,
    text=True,
)

print(result.returncode)
print(result.stderr)
```

- Git starts, but the command fails.
- A nonzero `returncode` does **not** raise an exception by default.
- Check `returncode` before using the output when success is required.

**Try:** Add an `if/else` statement that prints `stdout` on success and `stderr` on failure.

## 4. Run Git in a selected directory

Run this example from inside a Git repository:

```python
from pathlib import Path

repo_dir = Path.cwd()

result = subprocess.run(
    ["git", "status", "--porcelain"],
    cwd=repo_dir,
    capture_output=True,
    text=True,
)

print(result.stdout)
```

- `Path.cwd()` returns Python's current working directory.
- `cwd` sets the working directory of the **external program**. It does not change Python's working directory.
- `git status --porcelain` lists changed and untracked files. Empty output means no such changes.

**Try:** Change `repo_dir` to the path of another Git repository and run the command again.

## 5. Build commands from arguments

A function may need to run different Git commands. A tuple can hold arguments that will be added to a command list:

```python
git_args = ("--version",)
command = ["git", *git_args]

print(command)
```

- `*git_args` inserts the elements of the tuple into the list.

**Try:** Change `git_args` to run `git status --porcelain`. Run the command in a selected repository using `cwd`.

## 6. Handle errors

A Python **exception** reports a problem during execution. If it is not handled, the program stops.

- `try` — execute code that may raise an exception.
- `except` — handle a specified type of exception.
- `as error` — assign the exception object to a variable so its message can be read.

Possible exceptions are described in the [subprocess documentation](https://docs.python.org/3/library/subprocess.html) and [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html).

### 6.1. The program cannot start

Run this example in Python or IPython:

```python
try:
    result = subprocess.run(["program_that_does_not_exist"])
except OSError as error:
    print(type(error).__name__)
    print(error)
```

- `FileNotFoundError` — the program was not found.
- `PermissionError` — the program could not start because of permissions.
- Both are subclasses of `OSError`, so `except OSError` handles them.

### 6.2. The program starts but fails

By default, `run()` returns a result when the external program ends with an error. With `check=True`, a nonzero exit code raises `subprocess.CalledProcessError`:

```python
try:
    result = subprocess.run(
        ["git", "--invalid-option"],
        capture_output=True,
        text=True,
        check=True,
    )
except subprocess.CalledProcessError as error:
    print(error.stderr)
```

- `OSError` — a problem starting the program.
- `subprocess.CalledProcessError` — the program started, but returned a nonzero exit code with `check=True`.
- `subprocess.TimeoutExpired` — the process exceeded `timeout`, if that option was used.

**Try:** Remove `check=True`. Does the `except` block still run? Check `result.returncode`.

## 7. Git in `gitrepos`

Run the following commands inside a Git repository. In Python, select the repository directory first:

```python
from pathlib import Path

repo_dir = Path.cwd()
```

### Find the repository root

Terminal:

```bash
git rev-parse --show-toplevel
```

Python:

```python
result = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"],
    cwd=repo_dir,
    capture_output=True,
    text=True,
)
print(result.stdout.strip())
```

- `rev-parse` — read Git repository information.
- `--show-toplevel` — print the top-level working directory.

### Check for uncommitted changes

Terminal:

```bash
git status --porcelain
```

Python:

```python
result = subprocess.run(
    ["git", "status", "--porcelain"],
    cwd=repo_dir,
    capture_output=True,
    text=True,
)
print(result.stdout)
```

- Empty output — no uncommitted changes or untracked files.
- Non-empty output — changes are present.

### Check for remote repositories

Terminal:

```bash
git remote
```

Python:

```python
result = subprocess.run(
    ["git", "remote"],
    cwd=repo_dir,
    capture_output=True,
    text=True,
)
print(result.stdout)
```

- Empty output — no remote is configured.
- Non-empty output — at least one remote is configured.

### Show detailed status

Terminal:

```bash
git status
```

Python:

```python
result = subprocess.run(
    ["git", "status"],
    cwd=repo_dir,
    capture_output=True,
    text=True,
)
print(result.stdout)
```

Shows the current branch, staged changes, unstaged changes and untracked files.

### Show remote addresses

Terminal:

```bash
git remote -v
```

Python:

```python
result = subprocess.run(
    ["git", "remote", "-v"],
    cwd=repo_dir,
    capture_output=True,
    text=True,
)
print(result.stdout)
```

Shows configured remote names and URLs.

## 8. fd in `gitrepos`

Search for `.git` entries inside the home directory.

Terminal (Bash, Zsh or PowerShell):

```bash
fd -H -I -g .git "$HOME"
```

Python (with `fd` available on `PATH`):

```python
search_dir = Path.home()

result = subprocess.run(
    ["fd", "-H", "-I", "-g", ".git", str(search_dir)],
    capture_output=True,
    text=True,
)
print(result.stdout)
```

- `-H` — include hidden files and directories.
- `-I` — do not apply ignore rules.
- `-g .git` — find entries named `.git`.
- `search_dir` — directory to search.
- `result.stdout.splitlines()` — list of matching paths.
- `result.returncode` — check whether the command succeeded.

In `gitrepos`, use the path to the bundled `fd` executable instead of the name `fd`.
