#!/usr/bin/env python3

import sys
import os

# Add src to path
sys.path.insert(0, 'src')

# Run as a module
if __name__ == '__main__':
    os.environ['ALPACA_NO_DBUS'] = '1'  # Flag to disable D-Bus
    
    # Import and run the main function
    from main import main
    exit_code = main('6.1.7')
    print(f"Alpaca exited with code: {exit_code}") 