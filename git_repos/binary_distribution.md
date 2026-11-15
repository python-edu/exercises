# Binary distribution

The `gitrepos` application uses a private copy of [`fd`](https://github.com/sharkdp/fd). The executable is included in
the Python `wheel`, so users do not need to install `fd` separately.

# 1. Terms

| Term | Meaning |
|---|---|
| Binary / executable | A compiled program, such as `fd` or `fd.exe` |
| Precompiled binary | An executable already built for a specific operating system and processor |
| Private executable | A program started using its file path; it does not need to be on `PATH` |
| Wheel (`.whl`) | A ZIP-format Python package archive installed by `pip` or `pipx` |
| Package data | Files other than Python modules included inside a Python package |
| `site-packages` | Directory containing installed Python packages, e.g. `env/Lib/site-packages/` on Windows or `env/lib/python3.13/site-packages/` on Linux (depends on the environment) |
| Project root | Directory containing `pyproject.toml` and `src/` |
| `dist/` | Directory containing files created during packaging |
| Platform tag | Part of a wheel filename that identifies a supported system and processor |

---

# 2. Download `fd`

1. **Check the target platform.** A *platform* means the operating system (Windows, Linux or macOS) and the processor architecture (such as x86-64).

   Python provides this information through the [`platform`](https://docs.python.org/3/library/platform.html) module:

   ```bash
   python -c "import platform; print(platform.system(), platform.machine())"
   ```

   - `platform.system()` — operating system.
   - `platform.machine()` — processor architecture (`AMD64` on many Windows computers, `x86_64` on Linux/macOS).

2. Open [fd releases](https://github.com/sharkdp/fd/releases/latest) and expand **Assets**.
3. Choose the precompiled archive for the target platform (x86-64 examples):

   | System | Archive name |
   |---|---|
   | Windows | `fd-VERSION-x86_64-pc-windows-msvc.zip` |
   | Linux | `fd-VERSION-x86_64-unknown-linux-musl.tar.gz` |
   | macOS (Intel) | `fd-VERSION-x86_64-apple-darwin.tar.gz` |

   - `VERSION` — replace with the chosen release number (e.g. `10.5.2`).
   - `x86_64` — 64-bit Intel/AMD processor (also called x64).
   - `musl` — the Linux build selected here for easier use across Linux systems. Compatibility still needs testing.
   **Notes:**

   - An *archive* is a file containing other files. `.zip` and `.tar.gz` are archive formats. `.tar.gz` combines a TAR archive with gzip compression. Both formats can be extracted on Windows, Linux and macOS; the `fd` releases use different formats for different platforms.
   - `.deb` files are installation packages for Debian/Ubuntu. They install software into the operating system. Use `.tar.gz` here because the project needs the executable **inside the Python package**, not installed system-wide.

4. Extract the downloaded archive and locate `fd` or `fd.exe`. Run the commands in the directory containing the archive:

   ```text
   # Windows (PowerShell)
   Expand-Archive -Path .\fd-vVERSION-x86_64-pc-windows-msvc.zip -DestinationPath .\fd_extracted
   Get-ChildItem .\fd_extracted -Recurse -Filter fd.exe

   # Linux (Bash)
   mkdir fd_extracted
   tar -xzf fd-vVERSION-x86_64-unknown-linux-musl.tar.gz -C fd_extracted
   find fd_extracted -type f -name fd

   # macOS (Zsh)
   mkdir fd_extracted
   tar -xzf fd-vVERSION-x86_64-apple-darwin.tar.gz -C fd_extracted
   find fd_extracted -type f -name fd
   ```

   Replace `VERSION` with the version in the downloaded filename. The executable may be inside a subdirectory of the extracted archive.

5. Copy the executable to `src/git_repos/bin/` from the project root:

   - Windows (PowerShell):

     ```powershell
     $fd = Get-ChildItem .\fd_extracted -Recurse -Filter fd.exe | Select-Object -First 1
     cp $fd.FullName .\src\git_repos\bin\fd.exe
     ```

   - Linux / macOS (Bash / Zsh):

     ```bash
     fd_file=$(find fd_extracted -type f -name fd -print -quit)
     cp "$fd_file" src/git_repos/bin/fd
     ```

   - `fd` / `fd_file` stores the source file found in the extracted archive.
   - `cp` copies the file to the project's `bin/` directory (`cp` is an alias in PowerShell).

6. On Linux and macOS, give the copied file permission to run:

   ```bash
   chmod +x src/git_repos/bin/fd
   ```

7. Test the executable from the project root:

   ```text
   # Windows (PowerShell)
   .\src\git_repos\bin\fd.exe --version

   # Linux / macOS (Bash / Zsh)
   ./src/git_repos/bin/fd --version
   ```

---

# 3. License

`fd` is available under **MIT OR Apache-2.0**. This project uses the [MIT license](https://github.com/sharkdp/fd/blob/master/LICENSE-MIT).

The MIT license allows using, modifying and redistributing `fd`, including in commercial applications.

1. Download the original `LICENSE-MIT` from the `fd` repository (preferably from the version used for the executable).
2. Save its text **without changes** as `src/git_repos/licenses/LICENSE_fd`.
3. Include this file in the wheel together with `fd`:
   - **Hatchling** — includes files inside `src/git_repos/` automatically, unless excluded by ignore rules.
   - **setuptools** — includes `licenses/*` and `bin/*` through `[tool.setuptools.package-data]` in the main exercise.

> The wheel must contain both `git_repos/bin/fd` (or `fd.exe`) and `git_repos/licenses/LICENSE_fd`.

---

# 4. Locating the bundled executable

Python provides [`importlib.resources`](https://docs.python.org/3/library/importlib.resources.html) to access files belonging to a Python package.

- With `pip install -e .`, Python uses the package in `src/git_repos/`.
- After installing a wheel with `pipx`, the package is stored in the `site-packages` directory of the `pipx` environment.
- The installation path can differ between operating systems and Python environments. Do not write it directly in the program.

Set `FD_PATH` **at the beginning of `repos.py`, outside any function**, before defining `scan_fd()`.

1. Import the required modules:

   ```python
   import os
   from importlib.resources import files
   ```

2. Select the executable name:

   ```python
   FD_NAME = "fd.exe" if os.name == "nt" else "fd"
   ```

   - `os.name == "nt"` — Windows; otherwise use `fd` (Linux/macOS).

3. Locate the executable inside the package:

   ```python
   FD_PATH = files("git_repos").joinpath("bin", FD_NAME)
   ```

   - `files("git_repos")` — accesses the files of the `git_repos` package using Python's import system. It does **not** search the entire disk.
   - `files()` returns a `Traversable` object, which supports operations similar to `Path`. With a normal installed directory, it is usually a `Path`.
   - `joinpath("bin", FD_NAME)` — selects the executable inside the package's `bin/` directory.
   - `FD_PATH` is set once when `repos.py` is imported, not on every call to `scan_fd()`.

4. Use `FD_PATH` in `scan_fd()`:

   ```python
   command = [str(FD_PATH), "-H", "-I", "-g", ".git", str(search_dir)]
   ```

   - `str(FD_PATH)` — provides the executable path as a string for `subprocess.run()`.
   - This works for the file-based installations used in this exercise (`pip install -e .` and `pipx`).

**Note:** A `Traversable` is not always a filesystem path (for example, when importing from a ZIP archive). Such cases require `importlib.resources.as_file()`; they are not used in this exercise.

---

# 5. Wheel and platform tags

A wheel (`.whl`) is a **ZIP archive** containing the package files. Its filename also identifies compatible systems.

Example:

```text
git_repos-0.1.0-py3-none-any.whl
```

- `py3` — Python 3.
- `none` — no Python extension-module ABI requirement.
- `any` — any operating system.

`any` is incorrect when the wheel contains `fd` compiled for one system.


## Platform tags

Choose the **platform tag from the `fd` archive you placed in `bin/`**:

| Bundled `fd` archive | Wheel platform tag |
|---|---|
| `x86_64-pc-windows-msvc.zip` | `win_amd64` |
| `x86_64-unknown-linux-musl.tar.gz` | `linux_x86_64` |
| `x86_64-apple-darwin.tar.gz` | `macosx_11_0_x86_64` — example only; use this tag only if `fd` supports macOS 11 and later |

Platform tags are defined in the [Python Packaging specification](https://packaging.python.org/en/latest/specifications/platform-compatibility-tags/). Use the values in the table for the selected `fd` archives; the tag must match the bundled executable.


## Example: Windows x86-64

1. Copy the Windows `fd.exe` into `src/git_repos/bin/`.
2. Build the wheel as described in the main exercise.
3. Replace the `any` tag with `win_amd64`:

   ```bash
   python -m wheel tags --platform-tag=win_amd64 --remove dist/FILE.whl
   ```

   - `FILE.whl` — wheel created by the build command.
   - `--platform-tag` — replace the wheel's platform label.
   - `--remove` — remove the original, untagged wheel after creating the new one.


>Notes:
>- The command changes the filename and wheel metadata.
>- It does not change the executable or verify compatibility.
>- The macOS tag also states a minimum macOS version, which must be supported by the chosen executable.

A wheel can be inspected without installing it. Python includes the [`zipfile`](https://docs.python.org/3/library/zipfile.html) module:

```bash
python -m zipfile -l dist/FILE.whl
```

- `-l` — list archive contents without extracting them.
- Check for the copied executable and `licenses/LICENSE_fd`.

Documentation: [Wheel tags](https://wheel.readthedocs.io/en/stable/reference/wheel_tags.html), [Wheel format](https://packaging.python.org/en/latest/specifications/binary-distribution-format/).
