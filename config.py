from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "data" / "ids_model.pkl"
TRAIN_DATA_PATH = BASE_DIR / "data" / "KDDTrain+.txt"

SELECTED_FEATURES = [
    "duration",
    "src_bytes",
    "dst_bytes",
    "count",
    "srv_count",
    "diff_srv_rate",
    "same_srv_rate",
    "diff_srv_rate"
]
