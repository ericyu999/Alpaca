#!/usr/bin/env python3
"""
Development launcher for Alpaca that handles relative imports and resource paths properly.
"""

import sys
import os
import subprocess

def main():
    # Get the current directory (project root)
    project_root = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(project_root, 'src')
    
    if not os.path.exists(src_dir):
        print(f"Error: Source directory not found at {src_dir}")
        sys.exit(1)
    
    # Set up environment variables
    env = os.environ.copy()
    
    # Add src to Python path
    if 'PYTHONPATH' in env:
        env['PYTHONPATH'] = f"{src_dir}:{env['PYTHONPATH']}"
    else:
        env['PYTHONPATH'] = src_dir
    
    # Set development mode
    env['ALPACA_DEV_MODE'] = '1'
    
    # Set resource path to our build directory
    resource_path = os.path.join(project_root, 'builddir', 'src', 'alpaca.gresource')
    if os.path.exists(resource_path):
        env['ALPACA_RESOURCE_PATH'] = resource_path
    
    # Set up XDG data dirs for our local install
    local_share = os.path.join(project_root, 'install', 'usr', 'local', 'share')
    if os.path.exists(local_share):
        if 'XDG_DATA_DIRS' in env:
            env['XDG_DATA_DIRS'] = f"{local_share}:{env['XDG_DATA_DIRS']}"
        else:
            env['XDG_DATA_DIRS'] = f"{local_share}:/usr/local/share:/usr/share"
    
    # Create a temporary launcher script that avoids relative import issues
    launcher_script = f"""
import sys
import os

# Ensure we can import from src directory
src_dir = "{src_dir}"
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

# Import main without relative imports
import main

if __name__ == '__main__':
    main.main('6.1.7')
"""
    
    # Write the launcher script to a temporary file
    temp_launcher = os.path.join(project_root, 'temp_launcher.py')
    with open(temp_launcher, 'w') as f:
        f.write(launcher_script)
    
    try:
        # Run the application
        print("Starting Alpaca...")
        print("Note: If this is your first run, you may need to set up AI providers in preferences.")
        result = subprocess.run([sys.executable, temp_launcher], env=env)
        return result.returncode
    finally:
        # Clean up temporary file
        if os.path.exists(temp_launcher):
            os.remove(temp_launcher)

if __name__ == '__main__':
    sys.exit(main()) 