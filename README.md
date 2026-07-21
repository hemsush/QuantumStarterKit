# QuantumComputingExperiments

This repository contains quantum computing experiments built with Qiskit.

# Notes

https://hemsush.github.io/QuantumStarterKit/


## Windows setup (Qiskit 2.x)

These instructions are for Windows PowerShell and install the versions requested:

- qiskit >= 2.0
- qiskit-aer >= 0.16
- matplotlib >= 3.7
- pylatexenc >= 2.10
- scipy >= 1.11
- sympy >= 1.12

### 1. Install Python

Download and install 3.11 and above from https://www.python.org/downloads/windows/.

During installation, make sure to check:
- Add Python to PATH
- Install pip

### 2. Create and activate a virtual environment

Open PowerShell in the repository folder and run:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 3. Upgrade packaging tools

```powershell
python -m pip install --upgrade pip setuptools wheel
```

### 4. Install dependencies

```powershell
python -m pip install "qiskit>=2.0" "qiskit-aer>=0.16" "matplotlib>=3.7" "pylatexenc>=2.10" "scipy>=1.11" "sympy>=1.12" jupyter ipykernel
```

### 5. Optional: register the environment in Jupyter

```powershell
python -m ipykernel install --user --name qiskit-env --display-name "Python (Qiskit)"
```

### 6. Verify the installation

```powershell
python -c "import qiskit, qiskit_aer, matplotlib, scipy, sympy; print('Qiskit version:', qiskit.__version__)"
```

If the command runs without errors, the environment is ready.

## Running the notebooks

You can open the notebooks in VS Code or Jupyter Notebook after activating the environment:

```powershell
jupyter notebook
```

## Google Colab setup

If you are using Google Colab, run the following cell at the start of your notebook:

```python
!pip install --upgrade pip
!pip install "qiskit>=2.0" "qiskit-aer>=0.16" "matplotlib>=3.7" "pylatexenc>=2.10" "scipy>=1.11" "sympy>=1.12"
```

Then verify the installation with:

```python
import qiskit
import qiskit_aer
import matplotlib
import scipy
import sympy

print("Qiskit version:", qiskit.__version__)
```

## Notes

- If you see installation issues on Windows, update Visual C++ Build Tools or try installing from the latest Python version supported by your system.
- For notebook usage, it is recommended to use VS Code with the Python extension.
