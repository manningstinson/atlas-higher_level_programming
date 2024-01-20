#!/usr/bin/python3
"""
Test script to check module-level documentation.
"""

import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout.strip()

# ... (previous code)

if __name__ == "__main__":
    module_name = "0-read_file"
    command = f'timeout 30 bash -c "python3 -c \\"d = __import__(\\\'{module_name}\\\').__doc__ ; r = \\\'OK\\\\n\\\' if d is not None and len(d.strip()) > 0 else \\\'\\\' ; print(r, end=\\\'\\\'\\" | wc -l"'
    
    print(f"Running command: {command}")

    return_code, output = run_command(command)

    print(f"Return Code: {return_code}")
    print(f"Output: {output}")

    if return_code == 0 and output == "1":
        print("Test passed: Module-level documentation present.")
    else:
        print("Test failed: Module-level documentation not found or invalid.")
