"""Abhishek Tiwari"""

import csv
from collections import defaultdict

def load_lookup_table(filepath):
    lookup_dict = {}
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dstport = int(row['dstport'])
            protocol = row['protocol'].lower()
            tag = row['tag']
            lookup_dict[(dstport, protocol)] = tag
    return lookup_dict

def process_flow_logs(flow_logs_file, lookup_dict):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    with open(flow_logs_file, 'r') as file:
        for line in file:
            fields = line.split()
            if len(fields) >= 7:
                dstport = int(fields[5])  # Destination port
                protocol_num = int(fields[6])  # Protocol number

                # Map protocol number to string
                protocol = 'tcp' if protocol_num == 6 else 'udp' if protocol_num == 17 else 'unknown'
                
                key = (dstport, protocol)
                
                # Count port/protocol combinations
                port_protocol_counts[key] += 1
                
                # Determineing the tag
                tag = lookup_dict.get(key, 'Untagged')
                tag_counts[tag] += 1
    
    return tag_counts, port_protocol_counts

def write_combined_output(tag_counts, port_protocol_counts, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write tag countss
        writer.writerow(['Tag Counts'])
        writer.writerow(['Tag', 'Count'])
        for tag, count in sorted(tag_counts.items()):
            writer.writerow([tag, count])
        
        writer.writerow([])  # Separate sections
        
        # Write port/protocol combination counts
        writer.writerow(['Port/Protocol Combination Counts'])
        writer.writerow(['Port', 'Protocol', 'Count'])
        for (port, protocol), count in sorted(port_protocol_counts.items()):
            writer.writerow([port, protocol, count])

def main():
    lookup_file = 'lookup.csv'
    flow_logs_file = 'flow_logs.txt'
    output_file = 'output.csv'
    
    lookup_dict = load_lookup_table(lookup_file)
    tag_counts, port_protocol_counts = process_flow_logs(flow_logs_file, lookup_dict)
    write_combined_output(tag_counts, port_protocol_counts, output_file)

if __name__ == '__main__':
    main()
