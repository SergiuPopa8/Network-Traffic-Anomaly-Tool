# Network-Traffic-Anomaly-Tool
This tool captures the LAN trafic between two devices. It detects potential unwanted traffic such as port scanning and brute-force attacks, using Machine Learning. The project uses Scapy for capturing raw TCP packets and Random Forest for the classification model.

# Usage
1. Clone the Repository
```bash
git clone [https://github.com/SergiuPopa8/Network-Traffic-Anomaly-Tool](https://github.com/SergiuPopa8/Network-Traffic-Anomaly-Tool)
cd Network-Traffic-Anomaly-Tool
```
2. Setup a virtual environment

```bash 
python3 -m venv .venv
```

3. Get the dataset

Download the KDDTest+ dataset here: https://www.kaggle.com/datasets/hassan06/nslkdd?select=KDDTest%2B.txt

Download the KDDTrain+ dataset here: https://www.kaggle.com/datasets/hassan06/nslkdd?select=KDDTrain%2B.txt

4. Train the model

```bash
sudo python3 train_model.py
```

5. Run the tool

```bash
sudo python3 live_ids.py
```
