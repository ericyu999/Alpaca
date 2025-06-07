#!/bin/bash

# Simple script to run Alpaca for development testing
echo "🦙 Starting Alpaca..."

# Make sure we're in the right directory
cd "$(dirname "$0")"

# Check if the GResource file exists, compile if needed
if [ ! -f "src/alpaca.gresource" ]; then
    echo "📦 Compiling UI resources..."
    cd src
    glib-compile-resources --target=alpaca.gresource --sourcedir=. alpaca.gresource.xml
    cd ..
fi

# Run Alpaca
echo "🚀 Launching Alpaca..."
ALPACA_NO_DBUS=1 python3 -m src.main 6.1.7 