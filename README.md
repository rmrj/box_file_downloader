# Box File Downloader User Guide
Table of Contents
1. Introduction
2. Prerequisites
3. Permissions & Access Control
4. Setting Up and Configuration
5. How to Use
6. Functions Overview
7. Useful Box SDK Documentation Links
8. Complete script
9. Conclusion
1. Introduction
The script allows you to list and download files from a shared Box folder, specifically files that start with the prefix "Application_" followed by numbers in the range 10 to 99. 

Note: You can replace your condition for downloading specific files here. I have used the above example for downloading specifically files that start with the prefix "Application_" followed by numbers in the range 10 to 99.

2. Prerequisites
Python 3.x

Box Python SDK. Installation via pip:



pip install boxsdk
3. Permissions & Access Control
Box App Permissions:

Read and write all files and folders: This permission allows your application to read and write content in Box. It's necessary to download files and list folder contents.

Manage shared links: This allows the application to use shared links to access content.

Ensure that the above permissions are granted in the Box Developer Console for your application.

Shared Link Permissions:

Access Level: The shared link should be set to "People with the link" if it's meant to be accessed without specific Box account restrictions. If the link is restricted to specific users or groups, ensure the script or service account running the script is among them.

Allow Download: This permission should be enabled on the shared link to allow downloading of files. 

4. Setting Up and Configuration
Box Developer Account: Ensure you have a Box Developer Account and have created a Box Application for JWT (JSON Web Tokens) authentication.

Configuration File: Obtain the config.json file for your Box Application, which contains necessary details for authentication.

Script Configuration: Update the following placeholders in the script:

FOLDER_ID: Add the folder ID which can be extracted from the Box URL.

SHARED_LINK_URL: Add the shared link URL of the folder.

CONFIG.JSON_FILE_PATH: Replace with the path to your config.json file.

5. How to Use
Ensure all configurations and permissions are in place.

Execute the script:



python your_script_name.py
The script will list and download the matching files to the directory from which the script is run. Upon completion, you'll see the message "Download completed!".

6. Functions Overview
list_files_using_shared_link(shared_link_url): Lists the items present in the shared Box folder.

download_file(file): Downloads a file from Box to the local directory where the script resides.

main(): The main function which orchestrates the process of listing and downloading files based on the criteria.

7. Useful Box SDK Documentation Links
Box Python SDK Github Repository: GitHub - box/box-python-sdk: Box SDK for Python 

Box API Documentation: Guides - Box Developer Documentation 

JWT Authentication: JWT Auth - Box Developer Documentation 

8. Complete script can be found in box_download.py

9. Conclusion
The Box File Downloader offers a streamlined way for engineers to access specific files shared via Box programmatically. For further enhancements or advanced features, refer to the official Box API documentation. Always prioritize security by ensuring the safe storage of your config.json file and never exposing sensitive authentication details.

Note: Always ensure the safe storage of your config.json file and never expose sensitive authentication details.
