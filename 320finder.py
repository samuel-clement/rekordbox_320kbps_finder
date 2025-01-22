import os
import mutagen.mp3
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class RekordboxPlaylistApp:
    def __init__(self, root):
        self.root = root
        self.root.title("320 Finder")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Add title label
        ttk.Label(
            self.root,
            text="320kbps mp3 Playlist Generator",
            font=("Helvetica", 18, "bold"),
            anchor="center",
        ).pack(pady=10)

        # Add directive label
        ttk.Label(
            self.root,
            text="Select a folder to scan for 320kbps tracks and create your playlist.",
            font=("Helvetica", 12),
            anchor="center",
        ).pack(pady=5)

        # Folder path entry
        self.folder_path = tk.StringVar()
        folder_frame = ttk.Frame(self.root)
        folder_frame.pack(pady=10, padx=50, fill=tk.X)
        ttk.Entry(
            folder_frame,
            textvariable=self.folder_path,
            width=40,
            font=("Helvetica", 10),
        ).pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        ttk.Button(folder_frame, text="Browse", command=self.select_folder).pack(side=tk.LEFT)

        # Generate button
        ttk.Button(
            self.root,
            text="Generate Playlist",
            command=self.generate_playlist,
            style="Accent.TButton",
        ).pack(pady=20)

        # Status label
        self.status_label = ttk.Label(self.root, text="", font=("Helvetica", 10))
        self.status_label.pack(pady=10)

    def select_folder(self):
        """Open a folder selection dialog."""
        folder_path = filedialog.askdirectory(title="Select Your Music Folder")
        if folder_path:
            self.folder_path.set(folder_path)

    def check_mp3_quality(self, file_path):
        """Check if an MP3 file meets high-quality criteria."""
        try:
            audio = mutagen.mp3.MP3(file_path)
            bitrate = audio.info.bitrate // 1000  # Convert to kbps
            sample_rate = audio.info.sample_rate
            duration = audio.info.length
            # Define high-quality thresholds
            return bitrate >= 320 and sample_rate >= 44100 and duration > 30
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return False

    def generate_playlist(self):
        """Generate a Rekordbox playlist (M3U) for high-quality MP3s."""
        folder_path = self.folder_path.get()
        if not folder_path:
            messagebox.showwarning("No Folder Selected", "Please select a folder to scan.")
            return

        playlist_path = os.path.join(folder_path, "High_Quality_Playlist.m3u")
        high_quality_files = []

        # Show status message
        self.status_label.config(text="Building playlist, please wait...", foreground="blue")
        self.root.update()

        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(".mp3"):
                    file_path = os.path.join(root, file)
                    if self.check_mp3_quality(file_path):
                        high_quality_files.append(file_path)

        if high_quality_files:
            with open(playlist_path, "w", encoding="utf-8") as playlist:
                for file in high_quality_files:
                    playlist.write(file + "\n")
            self.status_label.config(
                text=f"Playlist created: {playlist_path}", foreground="green"
            )
            messagebox.showinfo(
                "Success", f"Playlist created successfully!\nLocation: {playlist_path}"
            )
        else:
            self.status_label.config(text="No high-quality tracks found.", foreground="red")
            messagebox.showwarning(
                "No High-Quality Tracks", "No high-quality tracks were found in the folder."
            )

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure("Accent.TButton", font=("Helvetica", 12), padding=10)
    app = RekordboxPlaylistApp(root)
    root.mainloop()
