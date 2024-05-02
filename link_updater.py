import requests
from bs4 import BeautifulSoup

def fetch_vlc_download_link():
    # Fetch the VLC download page
    vlc_download_page = requests.get("https://www.videolan.org/vlc/download-windows.html")

    if vlc_download_page.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(vlc_download_page.content, 'html.parser')
        # Find the link element for the download
        download_link = soup.find("a", id="downloadButton2")
        if download_link:
            return download_link["href"]
        else:
            print("Download link not found on the page.")
            return None
    else:
        print("Failed to fetch VLC download page.")
        return None

def update_links_file(link, filename="links.txt"):
    try:
        with open(filename, "a+") as file:
            file.write(link + "\n")
        print("Download link appended to links.txt")
    except IOError:
        print("Error: Unable to write to file.")

if __name__ == "__main__":
    vlc_download_link = fetch_vlc_download_link()
    if vlc_download_link:
        print("Latest VLC Download Link:", vlc_download_link)
        update_links_file(vlc_download_link)
    else:
        print("Failed to fetch VLC download link.")
