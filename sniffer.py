import pyshark

def analyze_packets(interface='eth0'):
    print(f"Starting packet capture on interface: {interface}")
    try:
        capture = pyshark.LiveCapture(interface=interface)
        for packet in capture.sniff_continuously(packet_count=10):
            print(f"Packet captured: {packet}")
            if hasattr(packet, 'ip'):
                print(f"Source IP: {packet.ip.src}")
                print(f"Destination IP: {packet.ip.dst}")
                print(f"Protocol: {packet.highest_layer}")
            print("-" * 50)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_packets(interface='eth0')  # Replace 'eth0' with your network interface

