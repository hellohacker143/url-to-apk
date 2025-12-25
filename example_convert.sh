#!/bin/bash

# URL to APK Converter - Example Quick Start Script
# This script demonstrates how to convert a website URL to an Android APK

echo "================================"
echo "URL to APK Converter"
echo "================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed. Please install Python 3.7 or later."
    exit 1
fi

echo "[+] Python 3 found: $(python3 --version)"
echo ""

# Example 1: Convert btechfaqa.com
echo "[*] Example 1: Converting btechfaqa.com"
echo "[*] Command: python3 url_to_apk_converter.py https://btechfaqa.com 'BTech FAQA' com.btechfaqa"
echo ""
python3 url_to_apk_converter.py "https://btechfaqa.com" "BTech FAQA" "com.btechfaqa" -v "1.0.0"

if [ $? -eq 0 ]; then
    echo ""
    echo "[+] Successfully generated APK files for BTech FAQA!"
    echo "[+] Check the 'output_apk/' directory for the generated files."
    echo ""
    echo "Next steps:"
    echo "1. Copy the generated files to your Android Studio project"
    echo "2. Build the project using Gradle"
    echo "3. Generate a signed APK"
    echo "4. Install on your Android device"
else
    echo ""
    echo "[ERROR] Failed to generate APK files. Check the error messages above."
    exit 1
fi

echo ""
echo "================================"
echo "[+] Conversion Complete!"
echo "================================"
