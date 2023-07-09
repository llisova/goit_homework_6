from pathlib import Path
import shutil
import sys
import sort1 as parser
from normalize import normalize


def handle_images(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_documents(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_audio(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_video(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)  # робимо папку для архіва
    folder_for_file = target_folder / \
        normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(filename, folder_for_file)

    except shutil.ReadError:
        print('It is not archive')
        folder_for_file.rmdir()

    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Can't delete folder: {folder}")


def main(folder: Path):
    parser.scan(folder)
    for file in parser.images:
        handle_images(file, folder / 'images')
    for file in parser.documents:
        handle_documents(file, folder / 'documents')
    for file in parser.audio:
        handle_audio(file, folder / 'audio')
    for file in parser.video:
        handle_video(file, folder / 'video')
    for file in parser.other:
        handle_other(file, folder / 'other')
    for file in parser.archives:
        handle_archive(file, folder / 'archive')
    for folder in parser.folders[::-1]:
        handle_folder(folder)


if __name__ == "__main__":
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Start in folder: {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())
