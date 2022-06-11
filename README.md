# SB_Zad1
Symulator Biznesu Zadanie 1

Program bierze pliki mp3 z folderu MP3_Files i je zamienia na .wav, które zapisuje następnie w WAV_files.
Następnie z pomocą bibliotek SpeechRecognition bierze pliki .wav i tworzy tekst z nich, który zostaje następnie zapisany w Transcription_Files.
Na koniec czyta pliki tekstowe i tworzy listę wszystkich słow w nich zawarte i porównuje, które się pojawiają w obydwóch plikach i wyświetla je.

Z racji tego że .google_recognize ma problemy z odczytywaniem dużych plików musiałem podzielić plik 8772767ver2.mp3 na 2 części za pomocą ffmpeg.

Python 3.9.0
SpeechRecognition
PyDub
ffmpeg (używany poza programem) 
