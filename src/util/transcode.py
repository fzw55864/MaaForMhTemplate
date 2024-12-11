import sys

class Transcode():
    def transcode(self, text) -> str:
        return bytes(text, 'utf-8').decode('unicode-escape')
        

