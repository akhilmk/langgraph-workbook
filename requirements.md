# lang-graph: Project Requirements & Setup Guide

## Table of Contents

- [Prerequisites](#prerequisites)
- [Fresh Checkout — Environment Setup](#fresh-checkout--environment-setup)
- [Jupyter Notebook Support](#jupyter-notebook-support)
- [uv Command Reference](#uv-command-reference)
- [Project Files](#project-files)

---

## Prerequisites

Before getting started, ensure the following tools are installed on your system.

### Python

- **Version**: Python 3.11 or higher
- **Check**: `python --version`
- **Install**: [python.org](https://www.python.org/downloads/) or via your system package manager

### uv (Python Package Manager)

`uv` is a fast, modern Python package and project manager (replaces pip + virtualenv).

- **Version**: 0.11.0 or higher
- **Check**: `uv --version`

#### Install uv

```bash
# Linux / macOS (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Reload shell after install
source ~/.bashrc   # or ~/.zshrc
```

---

## Fresh Checkout — Environment Setup

Follow these steps after cloning the repository for the first time.

### Step 1: Clone the Repository

```bash
git clone https://github.com/akhilmk/lang-graph.git
cd lang-graph
```

### Step 2: Create Virtual Environment

```bash
uv venv
```

This creates a `.venv/` directory in the project root.

### Step 3: Activate the Virtual Environment

```bash
# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
uv sync
```

This reads `pyproject.toml` and installs all pinned dependencies from `uv.lock`.

### Step 5: Run the Project

```bash
uv run main.py
```

---

## Jupyter Notebook Support (VS Code)

This project uses **VS Code** to run Jupyter notebooks — no separate JupyterLab or browser UI needed.
VS Code provides the best notebook experience with full IntelliSense, debugging, and Git integration built in.

### Step 1: Install the dev dependency

Only `ipykernel` is required — it connects your project's virtual environment to VS Code as a kernel:

```bash
uv sync --group dev
```

> `ipykernel` is already listed under `[dependency-groups] dev` in `pyproject.toml`.

### Step 2: Install VS Code Extensions

Install these two extensions in VS Code:

| Extension | ID | Purpose |
|---|---|---|
| **Jupyter** | `ms-toolsai.jupyter` | Run `.ipynb` notebooks |
| **Python** | `ms-python.python` | Python language support |

Quick install via terminal:
```bash
code --install-extension ms-toolsai.jupyter
code --install-extension ms-python.python
```

### Step 3: Select the Project Kernel in VS Code

1. Open any `.ipynb` file in VS Code
2. Click **"Select Kernel"** (top right of the notebook)
3. Choose **"Python Environments"** → select `.venv` (the project's virtual environment)

VS Code auto-detects the `.venv` created by `uv venv` — no manual kernel registration needed.

### Step 4: Create a Notebook

```bash
# Create a new notebook file
touch notebooks/explore.ipynb
```

Then open it in VS Code and start coding!


---

## uv Command Reference

| Command | Description |
|---|---|
| `uv init` | Initialize a new project (creates `pyproject.toml`) |
| `uv venv` | Create a virtual environment in `.venv/` |
| `uv sync` | Install all dependencies from `uv.lock` (like `npm install`) |
| `uv add <package>` | Add a dependency and update `pyproject.toml` + `uv.lock` |
| `uv add --dev <package>` | Add a development-only dependency |
| `uv remove <package>` | Remove a dependency |
| `uv run <script>` | Run a script inside the project environment |
| `uv lock` | Regenerate `uv.lock` from `pyproject.toml` |
| `uv pip compile pyproject.toml -o requirements.txt` | Export to `requirements.txt` (for CI/CD compatibility) |
| `uv self update` | Update uv itself to the latest version |

---

## Project Files

| File | Purpose |
|---|---|
| `pyproject.toml` | Project metadata and dependency definitions |
| `uv.lock` | Locked, pinned dependency versions (commit this file) |
| `.venv/` | Local virtual environment (do NOT commit) |

> **Note**: Add `.venv/` to your `.gitignore` — do not commit the virtual environment directory.
