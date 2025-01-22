# 320 Finder

A simple and user-friendly tool to scan your music folder for high-quality MP3 tracks and create a Rekordbox-compatible `.m3u` playlist.

## Features
- **High-Quality Filtering**: Automatically selects tracks with a bitrate of at least 256 kbps, a sample rate of at least 44.1 kHz, and a duration longer than 30 seconds.
- **Intuitive Interface**: Easy-to-use graphical interface with a progress indicator.
- **Non-Destructive**: Your files remain untouched and unaltered.

## How to Use the Executable

1. **Download the Latest Release**
   - Go to the [Releases](https://github.com/samuel-clement/rekordbox_320kbps_finder/releases) page of this repository.
   - Download the `320finder.exe` file.

2. **Run the Application**
   - Double-click the downloaded `320finder.exe` file to launch the application.

3. **Select Your Music Folder**
   - Use the "Browse" button to choose the folder containing your MP3 files.

4. **Generate the Playlist**
   - Click the "Generate Playlist" button.
   - The application will scan your folder and create a `.m3u` playlist containing high-quality tracks.
   - A success message will display the location of the created playlist.

## FAQ
### Where is the playlist saved?
The `.m3u` playlist will be saved in the same folder you selected for scanning.

### What if no high-quality tracks are found?
The application will notify you if no tracks meeting the quality criteria are found.

### Can I use this app without Python installed?
Yes! The provided `.exe` file allows you to use the app without installing Python or any dependencies.

## Contributing
We welcome contributions! If you'd like to improve this project, feel free to fork the repository and submit a pull request.

## Developer Details

### Code Overview
This application is written in Python and uses the following libraries:
- `mutagen`: For extracting MP3 metadata like bitrate, sample rate, and duration.
- `tkinter`: For building a user-friendly graphical interface.

### How It Works
1. The user selects a folder containing MP3 files using the GUI.
2. The application scans the folder (and subfolders) for high-quality MP3 files.
3. High-quality tracks are identified based on bitrate, sample rate, and duration thresholds.
4. A Rekordbox-compatible `.m3u` playlist is generated in the same folder.

### File Structure
```
320finder/
├── 320finder.py                # Main Python script
├── README.md                   # Documentation
├── LICENSE                     # License file
```

### Running the Code
To run the code locally, ensure you have Python installed and install dependencies:
```bash
pip install mutagen
```
Then execute the script:
```bash
python 320finder.py
```

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

