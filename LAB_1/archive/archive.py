import zipfile
import os


def create_archive(
        archive_name: str,
        password: str,
        files_to_archive: list
) -> bool:
    for f in files_to_archive:
        if not os.path.isfile(f):
            return False

    with zipfile.ZipFile(archive_name, 'w') as zipf:
        for file in files_to_archive:
            if os.path.isfile(file):
                zipf.write(file)

        zipf.setpassword(password.encode('utf-8'))
    return True


def extract_archive(archive_name: str, password: str) -> bool:
    if not os.path.isfile(archive_name):
        return False

    with zipfile.ZipFile(archive_name, 'r') as zipf:
        zipf.setpassword(password.encode('utf-8'))
        zipf.extract()

    return True
