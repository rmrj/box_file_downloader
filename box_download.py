from boxsdk import JWTAuth, Client
from concurrent.futures import ThreadPoolExecutor

# add the folder id from box url
FOLDER_ID = ''
# add the shared link of the folder
SHARED_LINK_URL = ''  
# Initializing JWT Auth using config.json
auth = JWTAuth.from_settings_file('CONFIG.JSON_FILE_PATH')
client = Client(auth)


def list_files_using_shared_link(shared_link_url):
    # Fetch the shared item using the shared link
    shared_item = client.get_shared_item(shared_link_url)
    items = shared_item.get_items()
    return items


def download_file(file):
    content = file.content()
    print(content)
    with open(file.name, 'wb') as file_obj:
        file_obj.write(content)
    print(f"Downloaded {file.name}")



def main():
    files = list_files_using_shared_link(SHARED_LINK_URL)
    with ThreadPoolExecutor() as executor:
        for file in files:
            if file.type == 'file' and any(file.name.startswith(f"Application_{i}") for i in range(10, 100)):
                executor.submit(download_file, file)

    print("Download completed!")


if __name__ == "__main__":
    main()
