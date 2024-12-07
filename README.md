# QR_Mover

File Sharing Flask Application Documentation
Overview
This Flask-based application allows users to upload files, generate a QR code for downloading those files, and retrieve the files by scanning the QR code. Once a file is successfully downloaded, it is automatically deleted from the server to optimize storage and maintain security.

Features
File Upload: Drag-and-drop or browse to upload files.
QR Code Generation: Generates a QR code for downloading the uploaded files.
File Retrieval: Users can download files by scanning the QR code.
File Auto-Deletion: Files are automatically deleted from the server after being successfully downloaded.
Setup Instructions
1. Prerequisites
Python 3.9 or higher
Pip (Python package manager)

2. Installation
Clone the repository:

Create and activate a virtual environment:
bash
Copy code
python -m venv venv
source venv/bin/activate # On Windows, use: venv\Scripts\activate
Install dependencies:
bash
Copy code
pip install -r requirements.txt
3. Running the Application
Run the Flask development server:

python app.py
Access the application in your browser at:
http://127.0.0.1:5000

Usage
1. Uploading Files
Drag and drop a file into the upload area or use the file browser.
Once uploaded, a QR code is generated.
2. Downloading Files
Scan the QR code to open the download link on any device.
Click the "Download" button to retrieve the file.
3. Auto-Deletion of Files
After a file is successfully downloaded:

The server automatically deletes the file from the storage directory.
This ensures no residual files are left behind, maintaining optimal storage usage.
