#!/usr/bin/python3
"""
Test script to check module-level documentation.
"""

import sys
print(f"Python Version: {sys.version}")

import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

if __name__ == "__main__":
    module_name = "0-read_file"
    command = f'python3 -m {module_name}'

    print(f"Running command: {command}")

    return_code, output, error_output = run_command(command)

    print(f"Return Code: {return_code}")
    print(f"Output: {output}")
    print(f"Error Output: {error_output}")

    if "Module-level documentation" in output:
        print("Test passed: Module-level documentation present.")
    else:
        print(f"Test failed: Module-level documentation not found or invalid.")
