import os
import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading

def download_file(url, save_path, progress_bar, progress_label):

    total_size = 0
    try:
        with requests.get(url, stream=True, timeout=30) as r:  # Timeout set to 30 seconds
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            bytes_written = 0
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        bytes_written += len(chunk)
                        f.write(chunk)
                        progress = min(100, int(bytes_written / total_size * 100))
                        progress_bar['value'] = progress
                        progress_label.config(text=f"Downloading... {progress}%")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while downloading:\n{e}")
        return False
    return True

def save_location(url, save_dir, progress_bar, progress_label):

    os.makedirs(save_dir, exist_ok=True)
    file_name = url.split("/")[-1]
    save_path = os.path.join(save_dir, file_name)

    # Check if the file already exists, if so, skip download
    if os.path.exists(save_path):
        messagebox.showinfo("Info", f"Skipping download of {file_name}. File already exists.")
        return True

    success = download_file(url, save_path, progress_bar, progress_label)
    if not success:
        # Delete the incomplete download if download was not successful
        if os.path.exists(save_path):
            os.remove(save_path)
    return success

def download_selected(checkboxes, save_dir, progress_bar, progress_label):

    for var, checkbox in checkboxes:
        if var.get():
            url = checkbox.url
            threading.Thread(target=save_location, args=(url, save_dir, progress_bar, progress_label)).start()

def main():

    software_list = [
        ("https://inkscape.org/gallery/item/44619/inkscape-1.3.2_2023-11-25_091e20e-x64.msi", "Inkscape"),
        ("https://get.videolan.org/vlc/3.0.16/win64/vlc-3.0.16-win64.exe", "VLC"),
        ("https://download.blender.org/release/Blender2.83/blender-2.83.0-windows64.zip", "Blender")
    ]

    save_dir = os.path.abspath(os.path.join(os.getcwd(), "downloads"))

    root = tk.Tk()
    root.title("Freebees")
    root.geometry("400x200")

    progress_label = tk.Label(root, text="Ready to download...")
    progress_label.pack(pady=5)

    progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack(pady=10)

    checkboxes = []
    for url, software_name in software_list:
        var = tk.BooleanVar()
        checkbox = ttk.Checkbutton(root, text=software_name, variable=var)
        checkbox.url = url  # Attach URL to the checkbox
        checkbox.pack(anchor="w")
        checkboxes.append((var, checkbox))

    download_button = ttk.Button(
        root, text="Download Selected", command=lambda: download_selected(checkboxes, save_dir, progress_bar, progress_label)
    )
    download_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
