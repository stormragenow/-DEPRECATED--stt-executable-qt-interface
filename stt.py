# -*- coding: utf8 -*-
"""
convert wav/ogg -> text
"""
import json
import os
import subprocess
from datetime import datetime
from sys import platform
from vosk import KaldiRecognizer, Model
import download_lib



class STT:
    """
    Класс для распознования аудио через Vosk и преобразования его в текст.
    Поддерживаются форматы аудио: wav, ogg
    """
    default_init = {
        "model_path": "vosk/",  # путь к папке с файлами STT модели Vosk
        "sample_rate": 48000,
        "ffmpeg_path": "ffmpeg/" # путь к ffmpeg
    }

    def __init__(self,
                 model_path=None,
                 sample_rate=None,
                 ffmpeg_path=None
                 ) -> None:
        """
        Настройка модели Vosk для распознования аудио и
        преобразования его в текст.

        :arg model_path:  str  путь до модели Vosk
        :arg sample_rate: int  частота выборки, обычно 16000
        :arg ffmpeg_path: str  путь к ffmpeg
        """
        self.model_path = model_path if model_path else STT.default_init["model_path"]
        self.sample_rate = sample_rate if sample_rate else STT.default_init["sample_rate"]
        self.ffmpeg_path = ffmpeg_path if ffmpeg_path else STT.default_init["ffmpeg_path"]

        self._check_model()

        model = Model(self.model_path)
        self.recognizer = KaldiRecognizer(model, self.sample_rate)
        self.recognizer.SetWords(True)

    def _check_model(self):
        """
        Проверка наличия модели Vosk на нужном языке в каталоге приложения
        """        
        voskModelCheck=None
        if not os.path.exists(self.model_path):            
            voskModelCheck=False            
            download_lib.download_vosk()
            # если нужна полная версия vosk, download_vosk(True)
        else:
            voskModelCheck = True
            
        #"Vosk: сохраните папку model в папку vosk\n"
        #"Скачайте модель по ссылке https://alphacephei.com/vosk/models"        
        ffmpegCheck=None
        if not os.path.exists(self.ffmpeg_path):
            ffmpegCheck=False
            download_lib.download_ffmpeg()
        else:
            ffmpegCheck=True
                # "Ffmpeg: сохраните ffmpeg.exe в папку ffmpeg\n"
                # "Скачайте ffmpeg.exe по ссылке https://ffmpeg.org/download.html"                           

        
        if platform =='win32':  
            self.ffmpeg_path = self.ffmpeg_path + '/ffmpeg'
        else:
            self.ffmpeg_path = 'ffmpeg'
        


    def audio_to_text(self, audio_file_name=None) -> str:      
        
        if audio_file_name is None:
            return "Укажите путь и имя файла"
        if not os.path.exists(audio_file_name):
            return "Укажите правильный путь и имя файла"

        # Конвертация аудио в wav и результат в process.stdout
        process = subprocess.Popen(
            [self.ffmpeg_path,
             "-loglevel", "quiet",
             "-i", audio_file_name,          # имя входного файла
             "-ar", str(self.sample_rate),   # частота выборки
             "-ac", "1",                     # кол-во каналов
             "-f", "s16le",                  # кодек для перекодирования, у нас wav
             "-"                             # имя выходного файла нет, тк читаем из stdout
             ],
            stdout=subprocess.PIPE
                                   )

        # Чтение данных кусками и распознование через модель
        while True:
            assert process.stdout is not None
            data = process.stdout.read(4000)            
            if len(data) == 0:
                break
            if self.recognizer.AcceptWaveform(data):
                pass

        # Возвращаем распознанный текст в виде str
        result_json = self.recognizer.FinalResult()  # это json в виде str
        result_dict = json.loads(result_json)    # это dict
        return result_dict["text"]               # текст в виде str
