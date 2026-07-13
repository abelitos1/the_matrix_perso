import sys


try:
    import numpy as np
    NUMPY_VERSION = np.__version__
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    NUMPY_VERSION = None

try:
    import pandas as ps
    PANDAS_VERSION = ps.__version__
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    PANDAS_VERSION = None

try:
    import matplotlib
    MATPLOTLIB_VERSION = matplotlib.__version__
    HAS_MATPLOTLIB = True
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:
    HAS_MATPLOTLIB = False
    MATPLOTLIB_VERSION = None


def check_dependencies() -> bool:
    print("Checking dependencies:")
    deps = [
        ("pandas", HAS_PANDAS, PANDAS_VERSION, "Data manipulation ready"),
        ("numpy", HAS_NUMPY, NUMPY_VERSION, "Numerical computation ready"),
        ("matplotlib", HAS_MATPLOTLIB, MATPLOTLIB_VERSION,
         "Visualization ready"),
    ]
    all_ok = True
    for (name, dispo, vers, desc) in deps:
        if dispo:
            print(f"[OK] {name} ({vers}) - {desc}")
        else:
            print(f"[MISSING] {name} - required for this program")
            all_ok = False
    print("")
    return all_ok


def generate_matrix_data(size: int = 1000) -> "np.ndarray":
    data = np.random.normal(loc=50, scale=15, size=size)
    return data


def analyze_data(data: "np.ndarray") -> "ps.DataFrame":
    df = ps.DataFrame(data, columns=["value"])
    print("Analyzing Matrix data...")
    print(f"Processing {len(df)} data points...")
    return df


def visualize(df: "ps.DataFrame") -> None:
    print("Generating visualization...")
    plt.figure()
    plt.hist(df["value"], bins=30)
    plt.title("Matrix Data Analysis")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("\nAnalysis complete!")
    print("Result saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    if not check_dependencies():
        print("pip install -r requirements.txt")
        print("poetry install")
        sys.exit(1)
    data = generate_matrix_data()
    df = analyze_data(data)
    visualize(df)
