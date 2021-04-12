import pathlib
import sys


images = []
videos = []
music = []
docs = []
archives = []


def sort_files():
    if len(sys.argv) < 2:
        user_input = ""
    else:
        user_input = sys.argv[1]


path = pathlib.Path(user_input)

if path.exists():
    if path.is_dir():
        for files in Path(path).glob("*.png", "*.svg", "*.jpg", "*.jpeg"):
            images.append(files)
            for files in Path(path).glob("*.avi", "*.mp4", "*.mov", "*.mkv"):
                videos.append(files)
            for files in Path(path).glob("*.doc", "*.txt", "*.pdf", "*.docx"):
                docs.append(files)
            for files in Path(path).glob("*.mp3", "*.ogg", "*.wav", "*.arm"):
                music.append(files)
            for files in Path(path).glob("*.zip", "*.gz", "*.tar"):
                archives.append(files)
        else:
            print(f"{path} is not dir")

if __name__ == '__main__':
    print(sort_files())
