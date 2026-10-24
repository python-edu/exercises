# Exercise: Build an Installable Raster Tools Package

**Independent exercise — preparation for the next Python class**

**Package or script?**
- A script is executed to perform a task.
- A package provides reusable code that other programs can import.
- `raster_tools` will be a collection of helper functions for raster data.
- Import its functions into Python scripts or notebooks; do not run it as a standalone script.

**Goal**
- Create a Python project with the `src` layout.
- Build an installable package named `raster_tools`.
- Add two simple function placeholders.
- Install the package in editable mode and test it in IPython.
- Do not implement raster processing yet.

---

# 1. Create the project

1. Open a terminal.
2. Check the project generator installed in the previous class:

   ```bash
   projgen --help
   ```

3. Use `projgen` to create a project with:
   - Project name: `raster_tools`
   - Package name: `raster_tools`
   - Layout: `src`
4. Enter the project directory:

   ```bash
   cd raster_tools
   ```

5. Check the generated structure. It should include:

   ```text
   raster_tools/
   ├── pyproject.toml
   ├── env/
   └── src/
       └── raster_tools/
           └── __init__.py
   ```

---

# 2. Create the module

1. Create and open the module:

   ```bash
   micro src/raster_tools/raster_tools.py
   ```

2. Define two functions:
   - `raster_show()` — prints `My name is raster_show`.
   - `raster_hist()` — prints `My name is raster_hist`.
3. Use `def` and `print()` only.
   - No raster operations.
   - No parameters yet.

---

# 3. Check `pyproject.toml`

1. Open `pyproject.toml`:

   ```bash
   micro pyproject.toml
   ```

2. Check:
   - Package/project name: `raster_tools`.
   - The package uses the `src` layout.
   - The build-system settings are present.
3. Remove the CLI entry point if the generator created one:

   ```toml
   [project.scripts]
   raster_tools = "raster_tools.cli:main"
   ```

   - Remove these lines (or the whole `[project.scripts]` section if it contains only this entry).
   - This package provides importable functions, not a terminal command.

---

# 4. Prepare the virtual environment

1. Use the `env/` environment already created by `projgen`.
2. Activate it:
   - **Linux / macOS:**

     ```bash
     source env/bin/activate
     ```

   - **Windows (PowerShell):**

     ```powershell
     env\Scripts\Activate.ps1
     ```

3. Install the libraries:

   ```bash
   python -m pip install ipykernel numpy matplotlib
   ```

   - `ipykernel` installs `IPython` automatically as a dependency.

---

# 5. Install the package

1. From the project directory, install the local package in editable mode:

   ```bash
   python -m pip install -e .
   ```

2. Check the installation:

   ```bash
   python -m pip show raster_tools
   ```

   - Editable installation: changes to your `.py` file can be used without reinstalling the package (restart IPython or reload the module after changes).

See [pip: Local project installs](https://pip.pypa.io/en/stable/topics/local-project-installs/).

---

# 6. Test in IPython

1. Start IPython in the activated environment:

   ```bash
   ipython
   ```

2. Import and call both functions:

   ```python
   from raster_tools import raster_tools as rt

   rt.raster_show()
   rt.raster_hist()
   ```

3. Expected output:

   ```text
   My name is raster_show
   My name is raster_hist
   ```

4. Exit IPython:

   ```python
   exit
   ```

---

# 7. Final check

- [ ] Project generated with `projgen` and `src` layout.
- [ ] `src/raster_tools/raster_tools.py` contains two function placeholders.
- [ ] Generated `__init__.py` remains empty.
- [ ] No CLI entry point in `pyproject.toml`.
- [ ] Existing `env/` has `ipykernel`, `numpy`, and `matplotlib`.
- [ ] `pip install -e .` succeeds.
- [ ] Both functions work after import in IPython.

**Next class:** implement raster visualization and histograms using NumPy and Matplotlib.
