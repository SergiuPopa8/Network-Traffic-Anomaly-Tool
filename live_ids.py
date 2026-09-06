from scapy.all import sniff
import pandas as pd
from model_utils import load_model
from feature_extractor import extract_features
from config import SELECTED_FEATURES

print("Loading model...")
model = load_model()

def process_packet(packet):
    features = extract_features(packet)

    if features:
        print("FEATURES:", features)


        if not packet.haslayer("IP"):
            return

        src_ip = packet["IP"].src

        if (
            features["unique_ports"] >= 5 and
            features["diff_srv_rate"] > 0.5
        ):
            print(f"PORTSCAN DETECTED from {src_ip}")
            return

        if features["same_srv_rate"] > 0.9 and features["count"] > 30:
            print(f"BRUTEFORCE DETECTED from {src_ip}")
            return

        if features["syn_rate"] > 0.7 and features["count"] > 20:
            print(f"SYN Scan DETECTED from {src_ip}")
            return

        df = pd.DataFrame([features])
        df = df[SELECTED_FEATURES]

        try:
             
            prediction = model.predict(df)[0]

            if prediction == "DoS":
                print(f"Dos Detected from {packet['IP'].src}")
            elif prediction == "PortScan":
                print(f"PortScan Detected from {packet['IP'].src}")
            elif prediction == "BruteForce":
                print(f"BruteForce Detected from {packet['IP'].src}")
            else:
                print("Normal traffic")
        except Exception as e:
            print("Prediction error:", e)
    print(packet.summary())

print("Starting Tool...")
sniff(prn=process_packet, store=0)



