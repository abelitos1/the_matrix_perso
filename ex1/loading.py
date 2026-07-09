try:
    import numpy as np
    NUMPY_VERSION = numpy.__version__
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    NUMPY_VERSION = None

try:
    import pandas
    PANDAS_VERSION = pandas.__version__
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    PANDAS_VERSION = None

try:
    import matplotlib
    MATPOTLIB_VERSION = matplotlib.__version__
    HAS_MATPOTLIB = True
except ImportError:
    HAS_MATPOTLIB = False
    MATPLOTLIB_VERSION = None

def check_dependencies() -> bool:
    print ("Checking dependencies:")
    deps = [
        ("pandas", HAS_PANDAS, PANDAS_VERSION, "Data manipulation ready"),
        ("numpy", HAS_NUMPY, NUMPY_VERSION, "Numerical computation ready"),
        ("matplotlib", HAS_MATPOTLIB, MATPLOTLIB_VERSION, "Visualization ready"),
    ]
    all_ok = True
    for (name, dispo, vers, desc) in deps:
        if dispo:
            print (f"[OK] {name} ({vers}) - {desc}")
        else:
            print (f"[MISSING] {name} - required for this program")
            all_critical_ok = False

    print("")
    return all_critical_ok

def generate_matrix_data(size: int = 1000) -> np.ndarray:
    data = np.random.normal(loc=50, scale=15, size=size)
    return data


def analyze_data(data: np.ndarray) -> pandas.DataFrame:
    
if __name__ == "__main__":
    check_dependencies()
    data = generate_matrix_data()
    print(type(data), data.shape, data[:5])