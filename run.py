#!/usr/bin/env python3
"""
Alternative startup script for the Flask portfolio application.
Use this file instead of app.py if you prefer a dedicated run script.
"""

from app import app
import os

if __name__ == '__main__':
    # Configuration for different environments
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_ENV', 'production') == 'development'
    
    print(f"🚀 Starting Portfolio application...")
    print(f"📡 Running on: http://localhost:{port}")
    print(f"🔧 Debug mode: {'ON' if debug else 'OFF'}")
    print(f"🌟 Environment: {os.environ.get('FLASK_ENV', 'production')}")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    ) 