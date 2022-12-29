import requests
import json
import zipfile
import os
import shutil


def download_ffmpeg():
    ffmpeg_file_archive_name='ffmpeg.zip'
    repo_releas_json_sting = requests.get("https://api.github.com/repos/GyanD/codexffmpeg/releases?per_page=1")   
    last_releas=json.loads(repo_releas_json_sting.text)[0]
    dict_all_releas=dict(last_releas)
    
    asset=dict(dict_all_releas['assets'][-1])
    download_file=requests.get(str(asset['browser_download_url']),allow_redirects=True)
    os.mkdir('ffmpeg')
    with open(ffmpeg_file_archive_name,"wb") as ffmpegfile:
        ffmpegfile.write(download_file.content)
    
    archive= zipfile.ZipFile(ffmpeg_file_archive_name)
    for file in archive.namelist():
        if file.endswith('.exe'):
             content=archive.open(file).read()
             with open('ffmpeg/'+os.path.basename(file),'wb') as binary_file:
              binary_file.write(content)
    archive.close()
    os.remove(ffmpeg_file_archive_name)              


def download_vosk(large=None):
    if large==None:
        download_file=requests.get("https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip",allow_redirects=True)
        vosk_file_archive_name='vosk-model-small-ru-0.22.zip'
    else:
        download_file=requests.get("https://alphacephei.com/vosk/models/vosk-model-ru-0.22.zip",allow_redirects=True)
        vosk_file_archive_name='vosk-model-ru-0.22.zip'  
    #if os.path.exists(vosk_file_archive_name): os.remove(vosk_file_archive_name)
    if os.path.exists(vosk_file_archive_name)==False:
        with open(vosk_file_archive_name,"wb") as voskfile:
            voskfile.write(download_file.content)
        archive=zipfile.ZipFile(vosk_file_archive_name)
        archive.extractall('temp/')
        archive.close()        
        shutil.move('temp/'+vosk_file_archive_name.replace(".zip","")+"/",'vosk-model/')
        os.rmdir('temp')
        os.remove(vosk_file_archive_name)
    else:       
        archive= zipfile.ZipFile(vosk_file_archive_name)
        archive.extractall()
        archive.close()   
        os.rename(vosk_file_archive_name.replace(".zip",""),"vosk-model")
        os.remove(vosk_file_archive_name)