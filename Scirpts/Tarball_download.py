
import requests 
import tarfile
import os 
import requests
import tarfile
import os

def download_extract_tarball(url, extract_path='./'):
    """
    Downloads a tarball file from a URL, extracts it, and returns the path to the extracted files.

    Parameters:
    url (str): The URL of the tarball file to be downloaded.
    extract_path (str): The directory where the tarball will be extracted. Defaults to the current directory.

    Returns:
    str: The path to the extracted files.
    """
    # Get the filename from the URL
    filename = url.split('/')[-1]

    # Download the file
    print(f"Downloading {filename}...")
    response = requests.get(url, stream=True)
    
    # Save the downloaded tarball file
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
    print(f"{filename} downloaded successfully.")

    # Extract the tarball file
    if tarfile.is_tarfile(filename):
        print(f"Extracting {filename}...")
        with tarfile.open(filename, 'r:*') as tar:
            tar.extractall(path=extract_path)
        print(f"Extracted to {extract_path}.")
    else:
        print(f"{filename} is not a valid tarball file.")
        return None

    # Remove the tarball file after extraction
    os.remove(filename)
    print(f"{filename} removed after extraction.")

    return extract_path

# Example usage:
# url = 'https://example.com/sample.tar.gz'
# extracted_path = download_extract_tarball(url)
# print(f"Files are extracted to: {extracted_path}")
