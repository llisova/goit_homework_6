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


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                scan(folder)
        else:
            scan_file(item)


def scan_file(file: Path):
    for item in file.name:

        if item.suffix[1:] == 'JPEG' or 'PNG' or 'JPG' or 'SVG':
            images.append(item)
            extensions.append(item.suffix[1:])
        elif item.suffix[1:] == 'AVI' or 'MP4' or 'MOV' or 'MKV':
            video.append(item)
            extensions.append(item.suffix[1:])
        elif item.suffix[1:] == 'DOC' or 'DOCX' or 'TXT' or 'PDF' or 'XLSX' or 'PPTX':
            documents.append(item)
            extensions.append(item.suffix[1:])
        elif item.suffix[1:] == 'MP3' or 'OGG' or 'WAV' or 'AMR':
            audio.append(item)
            extensions.append(item.suffix[1:])

        else:
            unknown_ext.append(item.suffix[1:])

            other.append(item)


if __name__ == "__main__":
    folder = sys.argv[1]
    print(f'Start in folder {folder}')
    scan(Path(folder))
    print(f"Список файлів в категоріях {file_list}")
    print(f"Перелік відомих скрипту розширень {extensions}")
    print(f"Перелік невідомих скрипту розширень {unknown_ext}")
