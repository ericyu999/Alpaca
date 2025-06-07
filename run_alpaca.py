#!/usr/bin/env python3

import sys
import os
import subprocess

# Add the source directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

# Set up environment for resources
os.environ['ALPACA_DEV'] = '1'

# Import and run the main application
if __name__ == '__main__':
    # Set resource path to our build directory
    build_resource = os.path.join(current_dir, 'builddir', 'src', 'alpaca.gresource')
    if os.path.exists(build_resource):
        os.environ['ALPACA_RESOURCE_PATH'] = build_resource
    
    from main import main
    main('6.1.7') 