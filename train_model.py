import pandas as pd
from model_utils import train_model
from config import SELECTED_FEATURES
from config import TRAIN_DATA_PATH, MODEL_PATH

columns = [
    "duration","protocol_type","service","flag",
    "src_bytes","dst_bytes","land","wrong_fragment",
    "urgent","hot","num_failed_logins","logged_in",
    "count","srv_count","serror_rate","srv_serror_rate",
    "rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count",
    "dst_host_srv_count","dst_host_same_srv_rate",
    "dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate",
    "dst_host_srv_serror_rate","dst_host_rerror_rate",
    "dst_host_srv_rerror_rate","label"
]

print("Loading dataset...")
df = pd.read_csv(TRAIN_DATA_PATH, names=columns)

label = df["label"]

def map_attack(label):
    if label == "normal":
        return "normal"
    elif label in ["neptune", "smurf", "teardrop"]:
        return "DoS"
    elif label in ["satan", "ipsweep", "nmap"]:
        return "PortScan"
    elif label in ["guess_passwd", "ftp_write"]:
        return "BruteForce"
    else:
        return "Other"

df["label"] = df["label"].apply(map_attack)
# binary label
#df["label"] = df["label"].apply(lambda x: 0 if x == "normal" else 1)

# select only usable features
df = df[SELECTED_FEATURES + ["label"]]

X = df.drop("label", axis=1)
y = df["label"]

print("Training model...")
train_model(X, y)

print("Model trained and saved!")
