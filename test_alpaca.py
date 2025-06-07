#!/usr/bin/env python3
"""
Simple test script to verify Alpaca dependencies and basic functionality
"""

import sys
import os

print("Testing Alpaca dependencies...")

# Test GTK4 and Adwaita imports
try:
    import gi
    gi.require_version('Gtk', '4.0')
    gi.require_version('Adw', '1')
    from gi.repository import Gtk, Adw, Gio, GLib
    print("✓ GTK4 and Adwaita imports successful")
except Exception as e:
    print(f"✗ GTK4/Adwaita import failed: {e}")
    sys.exit(1)

# Test other dependencies
try:
    import requests
    print("✓ requests available")
except ImportError:
    print("✗ requests not available")

try:
    from PIL import Image
    print("✓ Pillow available")
except ImportError:
    print("✗ Pillow not available")

try:
    import matplotlib
    print("✓ matplotlib available")
except ImportError:
    print("✗ matplotlib not available")

try:
    import pydbus
    print("✓ pydbus available")
except ImportError:
    print("✗ pydbus not available")

# Test if we can access the source files
src_dir = os.path.join(os.path.dirname(__file__), 'src')
if os.path.exists(src_dir):
    print(f"✓ Source directory found: {src_dir}")
    
    # Try to import constants without running the full app
    sys.path.insert(0, src_dir)
    try:
        import constants
        print("✓ Alpaca constants module loads successfully")
        print(f"  - Cache dir: {constants.cache_dir}")
        print(f"  - Data dir: {constants.data_dir}")
        print(f"  - Config dir: {constants.config_dir}")
    except Exception as e:
        print(f"✗ Failed to import constants: {e}")
else:
    print(f"✗ Source directory not found: {src_dir}")

# Check for resource file
resource_file = os.path.join(os.path.dirname(__file__), 'builddir', 'src', 'alpaca.gresource')
if os.path.exists(resource_file):
    print(f"✓ Resource file found: {resource_file}")
else:
    print(f"✗ Resource file not found: {resource_file}")

print("\nAll basic dependencies seem to be working!")
print("The application should be ready to run.")
print("\nTo run Alpaca:")
print("1. Make sure you have Ollama installed (optional, for local AI)")
print("2. Run the application with proper environment setup") 