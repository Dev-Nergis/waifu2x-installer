import requests
import json
import os
import shutil
from zipfile import ZipFile

owner = "nihui"
repo = "waifu2x-ncnn-vulkan"



r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/releases/latest', headers={'Accept': 'application/vnd.github.v3+json'})
if r.status_code == 200:
    print(r.text)
    r = json.loads(r.text)
    rr = r['assets'][-1]
    rrr = rr['browser_download_url']
    name = rr['name'].replace('.zip', '')
    print(rrr)

response = requests.get(rrr)
open("waifu2x-ncnn-vulkan-windows.zip", "wb").write(response.content)

with ZipFile('waifu2x-ncnn-vulkan-windows.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()

# os.chdir(name)
os.rename(f'{name}', 'waifu2x-ncnn-vulkan')
source_dir = r".\waifu2x-ncnn-vulkan"
destination_dir = r"C:\Path\waifu2x-ncnn-vulkan"
shutil.copytree(source_dir, destination_dir)
os.remove('.\waifu2x-ncnn-vulkan-windows.zip')
shutil.rmtree('.\waifu2x-ncnn-vulkan')
