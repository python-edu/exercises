import os
import subprocess
from pathlib import Path
from importlib.resources import files
from types import SimpleNamespace


# global varaiables

FD_NAME = "fd.exe" if os.name == "nt" else "fd"
FD_PATH = files("git_repos").joinpath("bin", FD_NAME)



def git_command(*args: str, pth: str = None) -> subprocess.CompletedProcess[str]:
    """Run Git in the given directory and return its output and exit code."""
    command = ['git', *args]
    cwd = pth

    try:
        result = subprocess.run(command,
                                cwd=cwd,
                                capture_output=True,
                                text=True
                                )
    except subprocess.CalledProcessError as er:
        # print(er.stderr, '\n\n')
        result = SimpleNamespace({"returncode": 99, 'stderr': er.stderr})
        return result
    except FileNotFoundError as er:
        result = SimpleNamespace({"returncode": 99, 'stderr': er})
        return result

    return result


def is_repository(pth: Path) -> bool:
    """Check whether the given directory is the top-level Git working tree."""
    args = ("rev-parse", "--show-toplevel")
    info = git_command(*args, pth=pth)

    root = info.stdout.strip()
    if Path(root).resolve() == Path(pth).resolve():
        return True
    else:
        return False


def scan_walk(search_dir: str) -> list[str]:
    """Find Git repositories under a directory using os.walk()."""
    repos = []

    for directory, subdirectories, files in os.walk(search_dir):
        if ".git" in subdirectories:
            if is_repository(directory):
                repos.append(str(directory).strip())
                subdirectories.clear()  # czyści listę

    return sorted(set(repos))


def scan_fd(search_dir: str) -> list[str]:
    """Search a directory with the bundled fd and return verified Git repository paths."""

    arguments = [str(FD_PATH), "-H", "-I", "-g", ".git", "--prune", search_dir]
    res = subprocess.run(arguments,
                         capture_output=True,
                         text=True
                         )
    # breakpoint()
    repos = [str(Path(item.strip()).parent) for item in res.stdout.splitlines()]
    repos = sorted(set(repos))
    repos = [pth for pth in repos if is_repository(pth)]

    return repos


def scan_repos(search_dir: Path | None = None) -> list[str]:
    if search_dir is not None:
        search_dir = str(search_dir).strip()
    else:
        search_dir = str(Path.home())

    try:
        repos = scan_fd(search_dir)
    except OSError as er:
        print('Nie znaleziono progrmu fd! Użyty zostanie os.walk!\n')
        print(er)
        repos = scan_walk(search_dir)

    return repos


def get_status(pth: Path) -> str:
    """Return 'clean' or 'changes' depending on uncommitted Git changes."""
    res = git_command("status", "--porcelain", pth=pth)

    if res.returncode != 0:
        return res.stderr
    else:
        if res.stdout == '':
            return "clean"
        else:
            return "changes"


def has_remote(path: Path) -> bool:
    """Check whether at least one remote repository is configured."""
    pass
