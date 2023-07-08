import sys
from pathlib import Path

images = []
documents = []
audio = []
video = []
archives = []
other = []
extensions = []
unknown_ext = []


file_list = {
    'images': images,
    'documents': documents,
    'audio': audio,
    'video': video,
    'archives': archives,
    'other': other
}


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):

                scan(item)
            continue
        else:

            scan_file(item)


def scan_file(file: Path):
    ext = get_extension(file.name)
    if ext == 'JPEG' or 'PNG' or 'JPG' or 'SVG':
        images.append(file)
        extensions.append(ext)
    elif ext == 'AVI' or 'MP4' or 'MOV' or 'MKV':
        video.append(file)
        extensions.append(ext)
    elif ext == 'DOC' or 'DOCX' or 'TXT' or 'PDF' or 'XLSX' or 'PPTX':
        documents.append(file)
        extensions.append(ext)
    elif ext == 'MP3' or 'OGG' or 'WAV' or 'AMR':
        audio.append(file)
        extensions.append(ext)
    elif ext == 'ZIP':
        archives.append(file)
        extensions.append(ext)

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
