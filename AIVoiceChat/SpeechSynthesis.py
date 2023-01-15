from gtts import gTTS

language = 'ja'

# 音声合成で生成した音声データをoutput_pathにmp3形式で保存(wavは非対応？)
def speech_synthesis(text, output_path):
    tts = gTTS(text, lang=language)
    tts.save(output_path)
