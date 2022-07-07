import json, requests, os, shutil
from zipfile import ZipFile

owner = "nihui"
repo = "waifu2x-ncnn-vulkan"
path = "C:\Path\waifu2x-ncnn-vulkan"


r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/releases/latest', headers={'Accept': 'application/vnd.github.v3+json'})
if r.status_code == 200:
    r = json.loads(r.text)
    rr = r['assets'][-1]
    rrr = rr['browser_download_url']
    name = rr['name'].replace('.zip', '')
    print(rrr)

response = requests.get(rrr)
open('waifu2x-ncnn-vulkan-windows.zip', 'wb').write(response.content)

with ZipFile('waifu2x-ncnn-vulkan-windows.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()

# 폴더 이름 변경
os.rename(f'{name}', 'waifu2x-ncnn-vulkan')
# 이전 Path 파일 삭제
if (os.path.isdir(path)) == True:
    shutil.rmtree('C:\Path\waifu2x-ncnn-vulkan')
elif (os.path.isdir(path)) == False:
    pass
else:
    print("ERROR!")
    exit()
##
source_dir = ".\waifu2x-ncnn-vulkan"
destination_dir = path
shutil.copytree(source_dir, destination_dir)
os.remove('.\waifu2x-ncnn-vulkan-windows.zip')
shutil.rmtree('.\waifu2x-ncnn-vulkan')
# 환경변수 설정
print("Adding environment variables is manual :>")
print("pass enter key to continue")
