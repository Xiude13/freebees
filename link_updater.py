import requests
from bs4 import BeautifulSoup

def update_download_link():
    download_page = requests.get("https://www.videolan.org/vlc/download-windows.html")
    download_page = requests.get("https://inkscape.org/")

    if download_page.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(download_page.content, 'html.parser')
        # Find the link element for the download
        download_link = soup.find("a", id="downloadButton2")
        if download_link:
            return download_link["href"]
        else:
            print("Download link not found on the page.")
            return None
    else:
        print("Failed to fetch download page.")
        return None

def update_links_file(link, filename="links.txt"):
    try:
        # Read the current contents of the file
        with open(filename, "r") as file:
            lines = file.readlines()

        # Remove any previous version of the link
        lines = [line for line in lines if "videolan" not in line]

        # Append the updated link if it's not already present
        if link.strip() not in lines:
            lines.append(link + "\n")

            # Write the updated contents back to the file
            with open(filename, "w") as file:
                file.writelines(lines)

            print("Download link updated in links.txt")
        else:
            print("Link already exists in links.txt")
    except IOError:
        print("Error: Unable to write to file.")

if __name__ == "__main__":
    update_download_link = update_download_link()
    if update_download_link:
        print("Latest Download Link:", update_download_link)
        update_links_file(update_download_link)
    else:
        print("Failed to fetch download link.")
