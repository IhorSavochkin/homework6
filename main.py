from pathlib import Path 
import shutil
import sys
import file_parser as parser
from normalize import normalize

def handle_media(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_archive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
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
        print(f'Can not delete this folder: {folder}')

def main(folder: Path):
    parser.scanning(folder)

    for file in parser.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    
    for file in parser.AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')
    for file in parser.MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')
    for file in parser.MOV_VIDEO:
        handle_media(file, folder / 'video' / 'MOV')
    for file in parser.MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')

    for file in parser.DOC_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOC')
    for file in parser.DOCX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOCX')
    for file in parser.TXT_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'TXT')
    for file in parser.PDF_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PDF')
    for file in parser.XLSX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'XLSX')
    for file in parser.PPTX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PPTX')
    
    for file in parser.MP3_MUSIC:
        handle_media(file, folder / 'audio' / 'MP3')
    for file in parser.OGG_MUSIC:
        handle_media(file, folder / 'audio' / 'OGG')
    for file in parser.WAV_MUSIC:
        handle_media(file, folder / 'audio' / 'WAV')
    for file in parser.AMR_MUSIC:
        handle_media(file, folder / 'audio' / 'AMR')
    
    for file in parser.MY_OTHERS:
        handle_other(file, folder / 'other files')

    for file in parser.ZIP_ARCHIVE:
        handle_archive(file, folder / 'archives' / 'ZIP')
    for file in parser.GZ_ARCHIVE:
        handle_archive(file, folder / 'archives' / 'GZ')
    for file in parser.TAR_ARCHIVE:
        handle_archive(file, folder / 'archives' / 'TAR')
    
    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)

if __name__ == '__main__' :
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        # print(f'Start in folder: {folder_for_scan.resolve()}')
        # main(folder_for_scan.resolve())
        
        print(f'Start in folder: {folder_for_scan}')
        main(folder_for_scan)
    

    