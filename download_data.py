__author__ = 'Smadar Gazit'

#download all human proteins from swissprot:https://www.uniprot.org/uniprot/?query=*&fil=organism%3A%22Homo+sapiens+%28Human%29+%5B9606%5D%22+AND+reviewed%3Ayes&desc=no&sort=organism

import os
import pathlib 
import urllib
import urllib.request
import shutil 
import random

def download_data(out_path, url, force=False):
    
    """ downloads the data to the specified out_path """
    
    samples_dir=pathlib.Path(out_path)
    samples_dir.mkdir(exist_ok=True)
    out_filename = str(samples_dir.joinpath("proteins.fasta"))
    
    if os.path.isfile(out_filename) and not force:
        print(f'Proteins file {out_filename} exists, skipping download.')
    else:
        print(f'Downloading {url}...')
        with urllib.request.urlopen(url) as response, open(out_filename, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print(f'Saved to {out_filename}.')

    import zipfile
    with zipfile.ZipFile(out_filename, 'r') as zip_ref:
        zip_ref.extractall(out_path)
    return out_filename