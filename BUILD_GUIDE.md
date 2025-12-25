# URL to APK Converter - Build Guide

## Quick Start

Convert any website URL to a standalone Android APK application.

### Option 1: Using Python Script (Fast)

```bash
python3 url_to_apk_converter.py https://btechfaqa.com "BTech FAQA" com.btechfaqa
```

### What You'll Get:

- Generated Android project files
- MainActivity with WebView
- AndroidManifest.xml
- build.gradle configuration
- Layout files
- String resources

## Requirements

### For Python Script:
- Python 3.7+
- No additional dependencies needed

### For Building APK:
- Android Studio
- Android SDK (minimum API level 21)
- Gradle

## How It Works

1. **URL Validation**: Automatically adds https:// if missing
2. **Project Generation**: Creates all necessary Android files
3. **WebView Integration**: Loads your website in the app
4. **Custom Branding**: Supports app name and package customization

## Supported Features

✅ Custom app names  
✅ Custom package names  
✅ JavaScript enabled  
✅ DOM storage enabled  
✅ Back button navigation  
✅ Loading progress bar  
✅ Any website URL support  
✅ btechfaqa.com optimized  

## Build Steps

1. Run the Python converter script
2. Output files will be in `output_apk/` directory
3. Open in Android Studio
4. Build > Generate Signed Bundle / APK
5. Sign with your keystore
6. Done!

## Example Usage

```bash
# For btechfaqa.com
python3 url_to_apk_converter.py https://btechfaqa.com "BTech FAQA" com.btechfaqa -v 1.0.0

# For custom website
python3 url_to_apk_converter.py https://example.com "My App" com.example.myapp
```

## Generated Files Structure

```
output_apk/
├── AndroidManifest.xml
├── MainActivity.java
├── build.gradle
├── activity_main.xml
└── strings.xml
```

## Features Included

- WebView with JavaScript support
- Progress bar during page load
- Back button navigation
- Network state checking
- Storage permissions
- Internet permissions

## Customization

Edit the generated files to customize:
- App icon
- Splash screen
- Colors and themes
- App permissions
- Target API level

## Troubleshooting

**Issue**: Module not found  
**Solution**: Ensure Python 3.7+ is installed

**Issue**: APK build fails  
**Solution**: Check Android Studio setup and SDK installation

**Issue**: Website not loading  
**Solution**: Ensure URL is accessible and enable JavaScript in WebView settings

## License

MIT License - Feel free to use for personal and commercial projects

## Support

For issues and questions, open a GitHub issue.
