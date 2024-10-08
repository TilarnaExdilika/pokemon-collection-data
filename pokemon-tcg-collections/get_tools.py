import os
import requests
from bs4 import BeautifulSoup
import urllib.parse
import concurrent.futures

def get_data_from_website():
    url = 'https://pkmncards.com/sets/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    entry_content = soup.find('div', class_='entry-content')
    
    data = {}
    current_main_folder = None
    
    for element in entry_content.find_all(['h2', 'ul']):
        if element.name == 'h2':
            current_main_folder = element.text.strip()
            data[current_main_folder] = []
        elif element.name == 'ul' and current_main_folder:
            for li in element.find_all('li'):
                set_name = li.text.strip()
                set_url = li.find('a')['href'] if li.find('a') else None
                data[current_main_folder].append((set_name, set_url))
    
    return data

def create_folders(base_dir, data):
    print("Starting folder creation...")
    for main_folder, subfolders in data.items():
        main_folder_path = os.path.join(base_dir, main_folder)
        os.makedirs(main_folder_path, exist_ok=True)
        print(f"Created main folder: {main_folder_path}")
        
        for subfolder, set_url in subfolders:
            subfolder_path = os.path.join(main_folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)
            print(f"Created subfolder: {subfolder_path}")
    print("Folder creation completed.")

def download_image(args):
    img_url, img_path = args
    if not os.path.exists(img_path):
        img_data = requests.get(img_url).content
        with open(img_path, 'wb') as handler:
            handler.write(img_data)
        print(f"Downloaded image: {img_path}")
    else:
        print(f"Image already exists, skipping: {img_path}")

def download_images(base_dir, data):
    print("Starting image download...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for main_folder, subfolders in data.items():
            for subfolder, set_url in subfolders:
                folder_path = os.path.join(base_dir, main_folder, subfolder)
                print(f"Downloading images for set: {subfolder}")
                
                response = requests.get(set_url)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                img_tags = soup.find_all('img', class_='card-image')
                
                download_args = [
                    (img['src'], os.path.join(folder_path, f"{i:03d}.jpg"))
                    for i, img in enumerate(img_tags, start=1)
                ]
                
                list(executor.map(download_image, download_args))
                
                print(f"Completed downloading images for set: {subfolder}")
    print("All image downloads completed.")

if __name__ == "__main__":
    base_dir = ""
    data = get_data_from_website()
    create_folders(base_dir, data)
    download_images(base_dir, data)

print("Folder structure and images have been successfully created!")
