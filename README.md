# Network-Traffic-Anomaly-Tool
This tool captures the LAN trafic between two devices. It detects potential unwanted traffic such as port scanning and brute-force attacks, using Machine Learning. The project uses Scapy for capturing raw TCP packets and Random Forest for the classification model.

# Usage 

Clone the repository, then create a virtual environment. 
Install the required libraries using `pip install -r requirements.txt`
Use `python3 train_model.py` to train the model first. After training the model, use `sudo python3 live_ids.py` to start the program.
