import requests
import zipfile
import os

def download(url, filename):
    print(f"Downloading {url}...")
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Download complete!")

def unzip(zip_path, extract_to):
    print(f"Extracting {zip_path} to {extract_to}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("Extraction complete!")

def main():
    url = ""
    zip_filename = "assets.zip"
    assets_dir = "assets"
    
    download(url, zip_filename)
    unzip(zip_filename, assets_dir)
    os.remove(zip_filename)

if __name__ == "__main__":
    main()