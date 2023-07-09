import sys
from pathlib import Path

images = []
documents = []
audio = []
video = []
archives = []
other = []
extensions = set()
unknown_ext = []
folders = []

file_list = {
    'images': images,
    'documents': documents,
    'audio': audio,
    'video': video,
    'archives': archives,
    'other': other
}


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                folders.append(item)
                scan(item)
            continue
        else:

            scan_file(item)


def scan_file(file: Path):
    ext = file.suffix[1:].upper()
    if ext in ['JPEG', 'PNG', 'JPG', 'SVG']:
        images.append(file)
        extensions.add(ext)
    elif ext in ['AVI', 'MP4', 'MOV', 'MKV']:
        video.append(file)
        extensions.add(ext)
    elif ext in ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']:
        documents.append(file)
        extensions.add(ext)
    elif ext in ['MP3', 'OGG', 'WAV', 'AMR']:
        audio.append(file)
        extensions.add(ext)
    elif ext in ['ZIP', 'RAR']:
        archives.append(file)
        extensions.add(ext)

    else:
        unknown_ext.append(ext)
        other.append(file)


if __name__ == "__main__":
    folder_to_scan = sys.argv[1]
    print(f'Start in folder {folder_to_scan}')
    scan(Path(folder_to_scan))
    print(f"Список файлів в категоріях {file_list}")
    print(f"Перелік відомих скрипту розширень {extensions}")
    print(f"Перелік невідомих скрипту розширень {unknown_ext}")
    print(f"Інші{other}")
    print(f'Folders{folders}')
