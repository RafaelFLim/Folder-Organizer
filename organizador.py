import os

from tkinter.filedialog import askdirectory

path = askdirectory(title="Selecione uma pasta")

list_files = os.listdir(path)

locations = {
    "images": [".png", ".jpg", '.jpeg', '.gif', '.svg', '.bmp', '.ico', '.ico', '.tif', '.tiff', '.raw', '.cr2', '.net' '.heic', '.webp' ],
    " 3D images":[".obj", ".stl", ".fbx", ".blend"],
    'videos': [".mp4", '.mov', '.avi', '.wmv', '.mkv', '.flv', '.webm', '.mpeg', '.mpg'],
    'audios':['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma'],
    'WordDocuments': ['.docx'],
    'PowerPoint':['.pptx', '.odp'],
    'OthersDocumentos':['.OSDT', '.ODS', '.ODP', '.txt', '.rtf', '.log'],
    "pdfs": [".pdf"],
    "spreadsheets":['.xlsx', '.csv',],
    "compressed": ['.zip', '.rar', '.7z'],
    "executable": ['.exe'],
    'iso':['.iso'],
    'apk':['.apk'],
    'DMG':['.dmg'],
    'EPUB':['.epub'],
    'FB2':['.fb2'],
    'Packages MSI':['.msi'],
    'Data':['.xml', '.tsv'],
    'DLL':['.dll'],
    'Sources':['.ttf', '.otf', '.woff', '.woff2'],
    'ipynb':['.ipynb'],
    'python':['.py'],
    'JAVA':['.jar', ],
    'JavaScript':['.js', '.jsx', '.json'],
    'C++':['.cpp', '.h'],
    'C#':['.cs'],
    'PHP':['.php'],
    'TypeScript':['.ts'],
    'Go':['.go'],
    'Swift':['.swift'],
    'Kotlin':['.kt'],
    'Ruby':['.rb'],
    'Rust':['.rs'],
    'SQL':['.sql'],
    'R':['.R'],
    'MATLAB':['.m'],
    'Assembly':['.asm'],
    'Objective':['.m', '.h'],
    'Groovy':['.groovy'],
    'HTML, CSS, JAVASCRIPT': ['.html', '.css', ',js'],
}



for archive in list_files:
    name, extension = os.path.splitext(f'{path}/{archive}')
    moved = False
    for folder in locations:
        if extension in locations[folder]:
            if not os.path.exists(f'{path}/{folder}'):
                os.mkdir(f"{path}/{folder}")
            os.rename(f'{path}/{archive}', f'{path}/{folder}/{archive}')
            moved = True
            break
    if not moved:
        folder = extension[1:]
        if not os.path.exists(f'{path}/{folder}'):
            os.mkdir(f"{path}/{folder}")
        os.rename(f'{path}/{archive}', f'{path}/{folder}/{archive}')
