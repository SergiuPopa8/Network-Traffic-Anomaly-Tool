import time
from collections import defaultdict

connection_tracker = defaultdict(list)

WINDOW_SIZE = 10  # seconds

def extract_features(packet):
    if not packet.haslayer("IP"):
        return None

    src = packet["IP"].src
    dst = packet["IP"].dst
    size = len(packet)
    now = time.time()
    flags = None
    if packet.haslayer("TCP"):
        port = packet["TCP"].dport
    elif packet.haslayer("UDP"):
        port = packet["UDP"].dport
    else:
        port = 0


    key = src

    connection_tracker[key].append({
    "time": now,
    "size": size,
    "dst_port": port,
    "flags": flags
})


    # keep only recent packets
    connection_tracker[key] = [
        conn for conn in connection_tracker[key]
        if now - conn["time"] < WINDOW_SIZE
    ]

    packets = connection_tracker[key]

    print("PORTS:", [conn["dst_port"] for conn in packets])
    duration = packets[-1]["time"] - packets[0]["time"] if len(packets) > 1 else 0
    src_bytes = sum(conn["size"] for conn in packets)
    dst_bytes = 0  # simplificat
    count = len(packets)
    ports = [conn["dst_port"] for conn in packets]

    unique_ports = len(set(ports))
    most_common_port = max(set(ports), key=ports.count)
    srv_count = ports.count(most_common_port)  
    same_srv_rate = srv_count / count if count > 0 else 0
    diff_srv_rate = unique_ports / count if count > 0 else 0

    rate = count / duration if duration > 0 else 0
    unique_ports_rate = unique_ports / duration if duration > 0 else 0

    syn_count = 0
    rst_count = 0

    for conn in packets:
        flags = conn.get("flags", None)

        if flags is not None:
            flags_str = str(flags)

            if "S" in flags_str:
                syn_count += 1

            if "R" in flags_str:
                rst_count += 1


    syn_rate = syn_count / count if count > 0 else 0
    rst_rate = rst_count / count if count > 0 else 0
 

    def calculate_diff_srv_rate(window):
        if len(window) == 0:
            return 0

        ports = []

        for conn in window:
            ports.append(conn["dst_port"])

        unique_ports = len(set(ports))
        total_connections = len(ports)

        diff_srv_rate = unique_ports / total_connections

        return diff_srv_rate


    return {
        "duration": duration,
        "src_bytes": src_bytes,
        "dst_bytes": dst_bytes,
        "count": count,
        "srv_count": srv_count,
        "diff_srv_rate": calculate_diff_srv_rate(packets),
        "same_srv_rate": same_srv_rate,
        "diff_srv_rate": diff_srv_rate,
        "rate": rate,
        "unique_ports": unique_ports,
        "unique_ports_rate": unique_ports_rate,
        "syn_rate": syn_rate,
        "rst_rate": rst_rate
    }
