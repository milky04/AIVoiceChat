import pyaudio
import wave

from pydub import AudioSegment
from pydub.playback import play
import pydub
import re
import os

# wav形式で録音
def recsound(input_path, record_time):
    CHUNK = 2**10
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    print("Recording ...")
    frames = []
    for i in range(0, int(RATE / CHUNK * record_time)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Done.")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(input_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# pyaudio+waveで音声の再生を行う場合はこちら(waveではmp3が再生できないため一旦コメントアウト)
# def play(output_path):
#     CHUNK_SIZE = 2**10
 
#     wf = wave.open(output_path, 'rb')
#     p = pyaudio.PyAudio()
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                     channels=wf.getnchannels(),
#                     rate=wf.getframerate(),
#                     output=True)
    
#     data = wf.readframes(CHUNK_SIZE)
#     while len(data) > 0:
#         stream.write(data)
#         data = wf.readframes(CHUNK_SIZE)
    
#     stream.stop_stream()
#     stream.close()
#     p.terminate()

# pydubでもしmp3形式だった場合wav形式に変換したうえで再生
def playsound(output_path):
    pattern = r".*(mp3)"
    if re.search(pattern, output_path):
        # 元のmp3ファイル名をoutput_path_mp3に保持
        output_path_mp3 = output_path
        # output_pathのファイル名の拡張子をmp3からwavに置換
        output_path = output_path.replace("mp3", "wav")
        # mp3ファイルを元にwavファイルを出力
        sound = pydub.AudioSegment.from_mp3(output_path_mp3)
        sound.export(output_path, format="wav")
        # 元のmp3ファイルを削除
        os.remove(output_path_mp3)
        
    sound = AudioSegment.from_file(output_path, format="wav")
    play(sound)
