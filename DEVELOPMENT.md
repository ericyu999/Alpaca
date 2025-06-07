# Alpaca Development Setup Guide

This guide covers setting up the Alpaca AI chat client for development and testing on Linux systems.

## Prerequisites

### System Dependencies
Install required packages:
```bash
sudo dnf install meson ninja-build gcc gcc-c++ gtk4-devel libadwaita-devel python3-gobject-devel gettext appstream glib2-devel vte291-devel libicu-devel python3-pip python3-devel
```

### Python Dependencies
Install required Python packages:
```bash
pip3 install --user requests pillow matplotlib odfpy markitdown openai pydantic instructor anthropic google-generativeai groq together mistralai
```

## Setup Process

### 1. Compile UI Resources
```bash
cd src
glib-compile-resources --target=alpaca.gresource --sourcedir=. alpaca.gresource.xml
cd ..
```

### 2. Install GSettings Schema
```bash
sudo cp data/com.jeffser.Alpaca.gschema.xml /usr/share/glib-2.0/schemas/
sudo glib-compile-schemas /usr/share/glib-2.0/schemas/
```

### 3. Running the Application
Use the helper script:
```bash
./run_alpaca.sh
```

Or run directly:
```bash
ALPACA_NO_DBUS=1 python3 -m src.main 6.1.7
```

## Known Issues and Fixes

### Anthropic API Authentication Fix

**Issue**: Previously, Anthropic API integration was failing with "Invalid bearer token" errors because the OpenAI library was sending `Authorization: Bearer` headers instead of the required `x-api-key` header.

**Fix Applied**: Modified the `Anthropic` class in `src/widgets/instance_manager.py` to override the `get_local_models()` method to use the correct Anthropic authentication headers:

- Uses `x-api-key` header for authentication
- Includes required `anthropic-version: 2023-06-01` header
- Properly handles Anthropic's models API response format

**Related GitHub Issue**: [#727](https://github.com/Jeffser/Alpaca/issues/727) - "Invalid bearer token" when using Anthropic API

### Translation Function Error Fix

**Issue**: Runtime NameError when trying to send messages: `NameError: name '_' is not defined` in multiple widget files.

**Fix Applied**: Added proper gettext setup to widget files that were missing translation functions:

- **`src/widgets/blocks/text.py`**: Added missing imports (`os`, `gettext`) and translation setup
- **`src/widgets/message.py`**: Added gettext import and proper translation function configuration
- Ensured consistency with other modules' translation setup across the codebase

This fix resolves errors when creating Message widgets, interacting with the chat interface, and using various UI components that depend on translated text.

### Environment Variables
- `ALPACA_NO_DBUS=1`: Disables D-Bus service registration which can cause startup failures in development environments

## Project Structure

The application is a GTK4/Libadwaita desktop client that supports multiple AI providers:
- Local models via Ollama
- OpenAI ChatGPT
- Google Gemini  
- Anthropic Claude
- And many other cloud providers

## Development Status

The application successfully launches and is functional. Recent fixes have addressed:
- Translation system setup across multiple Python modules
- Resource loading and compilation
- Anthropic API authentication
- D-Bus optional configuration
- Module imports and structure

The main functionality is working with proper AI provider integration. 