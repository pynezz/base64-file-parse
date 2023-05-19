#! /usr/bin/python3

import sys
import base64
import binascii

#### Reads a file from stdin and parses it as if it were base64.
def main():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        base64_bytes = []
        
        # Just read every line, and whatever is base64, decode it
        for l in lines:
            try:
                base64string = l.strip().split(' ')
                for s in base64string:
                    base64_bytes.append(s.encode("ascii"))
            except:
                print(f'Error reading {l}')
                continue
        try:
            base64_string_bytes = b''.join(base64_bytes)
            print(f'Bytes: {base64_string_bytes}')
            decoded_bytes = base64.b64decode(base64_string_bytes)
            print(f'\nDecoded bytes: {decoded_bytes}')
            decoded = decoded_bytes.decode("ascii")
            
            # Pipe with grep to find specific strings
            print(f'\nDecoded: {decoded}')
        except binascii.Error as e:
            print(f'Error decoding base64: {e}')
            return
          
main()
