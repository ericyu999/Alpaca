#!/usr/bin/env python3

import sys
import os

# Add src to path
sys.path.insert(0, 'src')

# Set up environment
from constants import cache_dir, data_dir, config_dir, source_dir

for directory in (cache_dir, data_dir, config_dir, source_dir):
    if not os.path.isdir(directory):
        os.mkdir(directory)

# Load resources
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Gio, Adw

# Load GResource file
resource_path = os.path.join(source_dir, 'alpaca.gresource')
if os.path.exists(resource_path):
    print(f"Loading resource from: {resource_path}")
    resource = Gio.Resource.load(resource_path)
    resource._register()
    print("Resource loaded successfully")
else:
    print(f"Resource file not found at: {resource_path}")

# Import the window
try:
    import window
    AlpacaWindow = window.AlpacaWindow
    print("Window imported successfully")
except Exception as e:
    print(f"Error importing window: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Create a simple application without D-Bus
class DebugApplication(Adw.Application):
    def __init__(self):
        super().__init__(application_id='com.jeffser.Alpaca.Debug')
        print("Application created")
    
    def do_activate(self):
        print("Application activating...")
        win = self.props.active_window
        if not win:
            print("Creating new window...")
            win = AlpacaWindow(application=self)
        print("Presenting window...")
        win.present()
        print("Window should be visible now")

if __name__ == '__main__':
    print("Starting debug Alpaca...")
    app = DebugApplication()
    print("Running application...")
    exit_code = app.run([])
    print(f"Application exited with code: {exit_code}") 