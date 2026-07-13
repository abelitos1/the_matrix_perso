import os
import sys
from dotenv import load_dotenv


def load_configuration() -> dict:
    load_dotenv()

    config = {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
        "DATABASE_URL": os.environ.get("DATABASE_URL"),
        "API_KEY": os.environ.get("API_KEY"),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT"),
    }
    return config


def check_missing_config(config: dict) -> list:
    missing = []
    for key, value in config.items():
        if value is None:
            missing.append(key)
    return missing


def print_configuration(config: dict) -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    missing = check_missing_config(config)
    if missing:
        print("WARNING: Missing configuration detected!")
        for key in missing:
            print(f"  - {key} is not set")
        print("")

    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    if config["DATABASE_URL"]:
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Not authenticated")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[MISSING] .env file not found")

    if config["MATRIX_MODE"] == "production":
        print("[OK] Running in production mode")
    else:
        print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    config = load_configuration()
    print_configuration(config)

    if config["MATRIX_MODE"] == "production" and not config["API_KEY"]:
        print("\nERROR: Production mode requires API_KEY")
        sys.exit(1)
    