# tts-executable-qt-interface

## Это инструмент для преобразования аудио и видео в текст, на базе [Vosk](https://alphacephei.com/vosk/)

### Версия Python === 3.10.8

#### По умолчания скачивается упрощенная версия Vosk модели, что бы качалась полная вам нужно изменить в файлe ``download_lib.py`` 30ю строчку на: ``def download_vosk(large=True):``

также вы можете сами [скачать](https://alphacephei.com/vosk/models) нужную вам модель и закинуть в папку Vosk рядом с main.py

1.~~Для запуска необходимо скачать [Vosk model](https://alphacephei.com/vosk/models)~~
2.~~Скачать [ffmpeg](https://ffmpeg.org/download.html) (либо установить его в систему если вы иcпользуте не windows)~~
3.~~Закидываем ffmpeg и Vosk в папку в папку с кодом или указываем свои пути в классе STT.~~

Интерфейс программы:
![image](https://user-images.githubusercontent.com/48676453/209669424-3a970586-cb86-4129-a9a1-0b1f17ee7f64.png)
