# Flow Log Parser

## Description

The python code parses flow log from a file and then it maps every row with a tag which is based on a lookup table then it generates an output file with the counts of matches for every tag and every port and protocol combination.

## Files

- `flow_parser.py`: This is the main file which includes the code to parse and process the flow logs.
- `lookup.csv`: This file is the lookup table for mapping ports and protocols to the tags.
- `flow_logs.txt`: This file has some sample flow log data.
- `README.md`: Documentation and instruction on how to run the program.

## Assumptions

- The lookup file and flow logs are plain text files.
- The lookup file can have to 10000 mappings and flow file can have size up to 10 mb.
- The tags are case insensitive.

## Instructions on how to run

1. Make sure you have python installed.
2. There are already `lookup.csv` and `flow_logs.txt` files for testing so make sure they are on the same directory as `flow_parser.py`(the main parser file).
3. Navigate to the directory and run the script using Python:
   python flow_parser.py

4. The script will generate a file named Output in the same directory where it will have tag counts(counts of each tag) and port/protocol counts (counts of each port/protocol combination).


## Thank You!
