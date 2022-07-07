import json, requests, os, shutil
from zipfile import ZipFile

owner = "nihui"
repo = "waifu2x-ncnn-vulkan"
path = "C:\Path\waifu2x-ncnn-vulkan"

####
print(r"""
                            ███     ██████              ████████             
                           ░░░     ███░░███            ███░░░░███            
 █████ ███ █████  ██████   ████   ░███ ░░░  █████ ████░░░    ░███ █████ █████
░░███ ░███░░███  ░░░░░███ ░░███  ███████   ░░███ ░███    ███████ ░░███ ░░███ 
 ░███ ░███ ░███   ███████  ░███ ░░░███░     ░███ ░███   ███░░░░   ░░░█████░  
 ░░███████████   ███░░███  ░███   ░███      ░███ ░███  ███      █  ███░░░███ 
  ░░████░████   ░░████████ █████  █████     ░░████████░██████████ █████ █████
   ░░░░ ░░░░     ░░░░░░░░ ░░░░░  ░░░░░       ░░░░░░░░ ░░░░░░░░░░ ░░░░░ ░░░░░ 
""")
print(r"""
          _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \         
        /::\____\                /::\    \                /::\____\                /::\____\        
       /::::|   |               /::::\    \              /::::|   |               /::::|   |        
      /:::::|   |              /::::::\    \            /:::::|   |              /:::::|   |        
     /::::::|   |             /:::/\:::\    \          /::::::|   |             /::::::|   |        
    /:::/|::|   |            /:::/  \:::\    \        /:::/|::|   |            /:::/|::|   |        
   /:::/ |::|   |           /:::/    \:::\    \      /:::/ |::|   |           /:::/ |::|   |        
  /:::/  |::|   | _____    /:::/    / \:::\    \    /:::/  |::|   | _____    /:::/  |::|   | _____  
 /:::/   |::|   |/\    \  /:::/    /   \:::\    \  /:::/   |::|   |/\    \  /:::/   |::|   |/\    \ 
/:: /    |::|   /::\____\/:::/____/     \:::\____\/:: /    |::|   /::\____\/:: /    |::|   /::\____\
\::/    /|::|  /:::/    /\:::\    \      \::/    /\::/    /|::|  /:::/    /\::/    /|::|  /:::/    /
 \/____/ |::| /:::/    /  \:::\    \      \/____/  \/____/ |::| /:::/    /  \/____/ |::| /:::/    / 
         |::|/:::/    /    \:::\    \                      |::|/:::/    /           |::|/:::/    /  
         |::::::/    /      \:::\    \                     |::::::/    /            |::::::/    /   
         |:::::/    /        \:::\    \                    |:::::/    /             |:::::/    /    
         |::::/    /          \:::\    \                   |::::/    /              |::::/    /     
         /:::/    /            \:::\    \                  /:::/    /               /:::/    /      
        /:::/    /              \:::\____\                /:::/    /               /:::/    /       
        \::/    /                \::/    /                \::/    /                \::/    /        
         \/____/                  \/____/                  \/____/                  \/____/         
""")
print(r"""
                                           lllllll kkkkkkkk                                            
                                           l:::::l k::::::k                                            
                                           l:::::l k::::::k                                            
                                           l:::::l k::::::k                                            
vvvvvvv           vvvvvvvuuuuuu    uuuuuu   l::::l  k:::::k    kkkkkkkaaaaaaaaaaaaa  nnnn  nnnnnnnn    
 v:::::v         v:::::v u::::u    u::::u   l::::l  k:::::k   k:::::k a::::::::::::a n:::nn::::::::nn  
  v:::::v       v:::::v  u::::u    u::::u   l::::l  k:::::k  k:::::k  aaaaaaaaa:::::an::::::::::::::nn 
   v:::::v     v:::::v   u::::u    u::::u   l::::l  k:::::k k:::::k            a::::ann:::::::::::::::n
    v:::::v   v:::::v    u::::u    u::::u   l::::l  k::::::k:::::k      aaaaaaa:::::a  n:::::nnnn:::::n
     v:::::v v:::::v     u::::u    u::::u   l::::l  k:::::::::::k     aa::::::::::::a  n::::n    n::::n
      v:::::v:::::v      u::::u    u::::u   l::::l  k:::::::::::k    a::::aaaa::::::a  n::::n    n::::n
       v:::::::::v       u:::::uuuu:::::u   l::::l  k::::::k:::::k  a::::a    a:::::a  n::::n    n::::n
        v:::::::v        u:::::::::::::::uul::::::lk::::::k k:::::k a::::a    a:::::a  n::::n    n::::n
         v:::::v          u:::::::::::::::ul::::::lk::::::k  k:::::ka:::::aaaa::::::a  n::::n    n::::n
          v:::v            uu::::::::uu:::ul::::::lk::::::k   k:::::ka::::::::::aa:::a n::::n    n::::n
           vvv               uuuuuuuu  uuuullllllllkkkkkkkk    kkkkkkkaaaaaaaaaa  aaaa nnnnnn    nnnnnn
""")
####

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
input("pass enter key to continue")
