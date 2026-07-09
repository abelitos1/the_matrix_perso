import sys
import os


def print_inside_construct() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print("")
    print("Current Python:" + sys.executable)
    print("Virtual Environment:" + os.path.basename(sys.prefix))
    print("Environment Path:" + sys.prefix)
    print("")
    print("SUCCESS: You're in an isolated environement!")
    print("Safe to install package without affecting the global system.")
    print("")
    version = f"python{sys.version_info.major}.{sys.version_info.minor}"
    site_packages = os.path.join(sys.prefix, "lib", version, "site-packages")
    print("Package installation path:" + site_packages)


def print_outside_matrix() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print("")
    print("Current Python:" + sys.executable)
    print("Virtual Environment: None detected")
    print("")
    print("WARNING: Your're in the global environement!")
    print("The machine can see everything you install.")
    print("")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print("")
    print("Then run this program again.")


def is_in_env() -> None:
    if sys.prefix == sys.base_prefix:
        print_outside_matrix()
    else:
        print_inside_construct()


if __name__ == "__main__":
    is_in_env()
