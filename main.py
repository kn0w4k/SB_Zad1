import speech_recognition as sr
from pydub import AudioSegment

# python 3.8+
# pip install SpeechRecognition
# pip install pydub

recognizer = sr.Recognizer()

# nazwy folderów
transcript_f = 'Transcription_Files'
mp3_f = 'MP3_Files'
wav_f = 'WAV_Files'

# lokalizacje MP3 plików
mp3_Key = fr'{mp3_f}/8772767ver2_00.mp3'  # key
mp3_Key1 = fr'{mp3_f}/8772767ver2_01.mp3'  # key
mp3_Rec = fr'{mp3_f}/8813861.mp3'  # recorded


# konwersja plików do .wav formatu inaczej speech_recognise nie działa
def ConvertMP3ToWAV(input_file):
    output_file = input_file.replace(f"{mp3_f}", f"{wav_f}")
    output_file = output_file.replace("mp3", "wav")
    sound = AudioSegment.from_mp3(input_file)
    sound.export(output_file, format='wav')


# analiza plików .wav i zapisywanie ich do plików tekstowych
def Transcription(filename):
    filename = filename.replace(".mp3", ".wav")
    filename = filename.replace(f"{mp3_f}", f"{wav_f}")
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
        recognizer.adjust_for_ambient_noise(source)

        txt_filename = filename.replace(".wav", "")
        txt_filename = txt_filename.replace(f"{wav_f}/", "")

        try:
            text = recognizer.recognize_google(audio_data, language='pl-PL')
            SaveTranscription(txt_filename, text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand source: " + filename)
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")


# funkcja zapisywania do pliku tekstowego
def SaveTranscription(filename, results):
    with open(f"{transcript_f}/Transcription_" + filename + ".txt", "a", encoding="UTF-8") as txt:
        txt.write(results)


# łączenie 2 oddzielnych plików tekstowych podzielonego mp3 w jeden
def JoinTranscription():
    text_ver00 = open(f"{transcript_f}/Transcription_8772767ver2_00.txt", mode="a+")
    text_ver01 = open(f"{transcript_f}/Transcription_8772767ver2_01.txt", mode="r")
    text_ver00.write(" " + text_ver01.read())
    text_ver01.close()
    text_ver00.close()
    with open(f"{transcript_f}/Transcription_KeyRecording_FinalVersion.txt", 'a') as txt:
        final_text = open(f"{transcript_f}/Transcription_8772767ver2_00.txt", mode="r")
        txt.write(final_text.read())
        txt.close()
        final_text.close()


# sprawdzenie które słowa z nagrań były w obydwóch plikach i ich wyświetlenie
def ComparingTranscriptions():
    key_txt = f'{transcript_f}/Transcription_Keys.txt'
    rec_txt = f'{transcript_f}/Transcription_8813861.txt'
    keys_dict = []
    recs_dict = []
    with open(key_txt, mode='r', encoding='utf-8') as key_txt, open(rec_txt, mode='r', encoding='utf-8') as rec_txt:
        for line in key_txt:
            k = line.split(" ")
            keys_dict = keys_dict + k
        for line in rec_txt:
            k = line.split(" ")
            recs_dict = recs_dict + k
        results = list(set(keys_dict).intersection(recs_dict))
        print(results)


if __name__ == '__main__':
    ConvertMP3ToWAV(mp3_Rec)
    ConvertMP3ToWAV(mp3_Key)
    ConvertMP3ToWAV(mp3_Key1)

    Transcription(mp3_Rec)
    Transcription(mp3_Key)
    Transcription(mp3_Key1)

    JoinTranscription()
    ComparingTranscriptions()
