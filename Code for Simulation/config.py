from pathlib import Path

BASE_DIR = Path(__file__).parent

INPUT_FOLDER = BASE_DIR / "Flights"
OUTPUT_FOLDER = BASE_DIR / "Results"

OUTPUT_FOLDER.mkdir(exist_ok=True)