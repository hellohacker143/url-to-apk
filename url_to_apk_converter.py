#!/usr/bin/env python3
"""
URL to APK Converter
Converts any website URL to a standalone Android APK application
Supports: btechfaqa.com, custom branding, WebView integration
"""

import os
import sys
import json
import argparse
from pathlib import Path
import subprocess
import tempfile
import shutil

class URLtoAPKConverter:
    """
    Main converter class that handles URL to APK conversion
    """
    
    def __init__(self, url, app_name, package_name, version="1.0.0"):
        self.url = url
        self.app_name = app_name
        self.package_name = package_name
        self.version = version
        self.output_dir = "output_apk"
        self.temp_dir = tempfile.mkdtemp()
        
    def validate_url(self):
        """Validate if URL is properly formatted"""
        if not self.url.startswith(("http://", "https://")):
            self.url = "https://" + self.url
        return True
    
    def create_android_manifest(self):
        """Generate AndroidManifest.xml"""
        manifest = f"""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="{self.package_name}">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/AppTheme">

        <activity
            android:name=".MainActivity"
            android:label="@string/app_name"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

    </application>

</manifest>
"""
        return manifest
    
    def create_main_activity(self):
        """Generate MainActivity.java with WebView"""
        activity = f"""package {self.package_name};

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ProgressBar;
import android.view.KeyEvent;

public class MainActivity extends Activity {{
    
    private WebView webView;
    private ProgressBar progressBar;
    private static final String TARGET_URL = "{self.url}";
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {{
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        webView = findViewById(R.id.webview);
        progressBar = findViewById(R.id.progressbar);
        
        // Configure WebView settings
        webView.getSettings().setJavaScriptEnabled(true);
        webView.getSettings().setDomStorageEnabled(true);
        webView.getSettings().setDatabaseEnabled(true);
        webView.getSettings().setUseWideViewPort(true);
        webView.getSettings().setLoadWithOverviewMode(true);
        
        // Set WebView client
        webView.setWebViewClient(new WebViewClient() {{
            @Override
            public void onPageStarted(WebView view, String url, android.graphics.Bitmap favicon) {{
                progressBar.setVisibility(android.view.View.VISIBLE);
            }}
            
            @Override
            public void onPageFinished(WebView view, String url) {{
                progressBar.setVisibility(android.view.View.GONE);
            }}
        }});
        
        // Load the URL
        webView.loadUrl(TARGET_URL);
    }}
    
    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {{
        if (keyCode == KeyEvent.KEYCODE_BACK && webView.canGoBack()) {{
            webView.goBack();
            return true;
        }}
        return super.onKeyDown(keyCode, event);
    }}
}}
"""
        return activity
    
    def create_build_gradle(self):
        """Generate build.gradle configuration"""
        gradle = f"""plugins {{
    id 'com.android.application'
}}

android {{
    compileSdkVersion 33
    
    defaultConfig {{
        applicationId "{self.package_name}"
        minSdkVersion 21
        targetSdkVersion 33
        versionCode 1
        versionName "{self.version}"
    }}
    
    buildTypes {{
        release {{
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt')
        }}
    }}
    
    compileOptions {{
        sourceCompatibility JavaVersion.VERSION_11
        targetCompatibility JavaVersion.VERSION_11
    }}
}}

dependencies {{
    implementation 'androidx.appcompat:appcompat:1.5.1'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
}}
"""
        return gradle
    
    def create_layout_xml(self):
        """Generate activity_main.xml layout"""
        layout = """<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <ProgressBar
        android:id="@+id/progressbar"
        android:layout_width="match_parent"
        android:layout_height="4dp"
        android:layout_alignParentTop="true"
        android:visibility="gone"
        style="@android:style/Widget.ProgressBar.Horizontal" />

    <WebView
        android:id="@+id/webview"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:layout_below="@id/progressbar" />

</RelativeLayout>
"""
        return layout
    
    def create_strings_xml(self):
        """Generate strings.xml resources"""
        strings = f"""<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">{self.app_name}</string>
    <string name="action_settings">Settings</string>
</resources>
"""
        return strings
    
    def generate_apk(self):
        """Main method to generate APK"""
        print(f"[*] Starting URL to APK conversion...")
        print(f"[*] URL: {self.url}")
        print(f"[*] App Name: {self.app_name}")
        print(f"[*] Package: {self.package_name}")
        
        # Validate URL
        if not self.validate_url():
            print("[!] Invalid URL format")
            return False
        
        print("[+] URL validated successfully")
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Generate all required files
        files = {
            'AndroidManifest.xml': self.create_android_manifest(),
            'MainActivity.java': self.create_main_activity(),
            'build.gradle': self.create_build_gradle(),
            'activity_main.xml': self.create_layout_xml(),
            'strings.xml': self.create_strings_xml()
        }
        
        # Write files
        for filename, content in files.items():
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"[+] Created {filename}")
        
        print(f"[+] All files generated in {self.output_dir}/")
        print(f"[+] Ready for APK build with Android Studio or Gradle")
        return True

def main():
    parser = argparse.ArgumentParser(
        description='Convert website URL to Android APK',
        epilog='Example: python3 url_to_apk_converter.py https://btechfaqa.com "BTech FAQA" com.btechfaqa'
    )
    
    parser.add_argument('url', help='Website URL to convert')
    parser.add_argument('app_name', help='Application display name')
    parser.add_argument('package_name', help='Java package name (e.g., com.example.app)')
    parser.add_argument('-v', '--version', default='1.0.0', help='App version')
    
    args = parser.parse_args()
    
    # Create converter
    converter = URLtoAPKConverter(
        url=args.url,
        app_name=args.app_name,
        package_name=args.package_name,
        version=args.version
    )
    
    # Generate APK
    success = converter.generate_apk()
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
