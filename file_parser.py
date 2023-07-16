import sys
from pathlib import Path

JPEG_IMAGES = []
PNG_IMAGES = []
JPG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS= []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_MUSIC = []
OGG_MUSIC = []
WAV_MUSIC = []
AMR_MUSIC = []
ZIP_ARCHIVE = []
GZ_ARCHIVE = []
TAR_ARCHIVE = []
MY_OTHERS = []

REGISTERED_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'MP3': MP3_MUSIC,
    'OGG': OGG_MUSIC,
    'WAV': WAV_MUSIC,
    'AMR': AMR_MUSIC,
    'ZIP': ZIP_ARCHIVE,
    'GZ': GZ_ARCHIVE,
    'TAR': TAR_ARCHIVE,
}

FOLDERS = []
EXTENSIONS = set() # only unique
UNDEFINED = set() # only unique

def define_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper() # without fullstop and in capital letters
   
def scanning(folder: Path) -> None:
    for el in folder.iterdir():
        if el.is_dir():
            if el.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other files'):
                FOLDERS.append(el)
                scanning(el)
            continue
        
        ext = define_extension(el.name)
        fullname = folder / el.name

        if not ext:
            MY_OTHERS.append(fullname)
            
        else: 
            try:
                container = REGISTERED_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNDEFINED.add(ext)
                MY_OTHERS.append(fullname)

if __name__ == '__main__':
    folder_to_scan = sys.argv[1]

    print(f'Start scanning folder {folder_to_scan}')
    scanning(Path(folder_to_scan))

    print(f'Images in JPEG format: {JPEG_IMAGES}')
    print(f'Images in PNG format: {PNG_IMAGES}')
    print(f'Images in JPG format: {JPG_IMAGES}')
    print(f'Images in SVG format: {SVG_IMAGES}')
    print(f'Video in AVI format: {AVI_VIDEO}')
    print(f'Video in MP4 format: {MP4_VIDEO}')
    print(f'Video in MOV format: {MOV_VIDEO}')
    print(f'Video in MKV format: {MKV_VIDEO}')
    print(f'Documents in DOC format: {DOC_DOCUMENTS}')
    print(f'Documents in DOCX format: {DOCX_DOCUMENTS}')
    print(f'Documents in TXT format: {TXT_DOCUMENTS}')
    print(f'Documents in PDF format: {PDF_DOCUMENTS}')
    print(f'Documents in XLSX format: {XLSX_DOCUMENTS}')
    print(f'Documents in PPTX format: {PPTX_DOCUMENTS}')
    print(f'Music in MP3 format: {MP3_MUSIC}')
    print(f'Music in OGG format: {OGG_MUSIC}')
    print(f'Music in WAV format: {WAV_MUSIC}')
    print(f'Music in AMR format: {AMR_MUSIC}')
    print(f'Archive in ZIP format: {ZIP_ARCHIVE}')
    print(f'Archive in GZ format: {GZ_ARCHIVE}')
    print(f'Archive in TAR format: {TAR_ARCHIVE}')
   
    print(f'Types of files in folder: {EXTENSIONS}')
    print(f'Files with undefined formats: {UNDEFINED}')
    print(f'Other files: {MY_OTHERS}')

    print(f'List of folders: {FOLDERS}')