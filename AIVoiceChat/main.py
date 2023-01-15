import SoundRecAndPlay as sound
import ConvertVoiceToText
import GenerateText
import SpeechSynthesis

# 録音時間を指定
record_time = 5
# 録音データのパスを指定
input_path = ".\wav\input.wav"
# 音声合成で生成する音声データのパスを指定
output_path = ".\wav\output.mp3"

# 録音データのパスと録音時間を指定して録音
sound.recsound(input_path, record_time)
# input_pathに保存された録音データをConvertVoiceToTextでテキストに変換
input_text = ConvertVoiceToText.convert_voice_to_text(input_path)
print(input_text)
# input_textをGenerateTextに投げて生成された文章を受け取る
result_text = GenerateText.generate_text(input_text)
print(result_text)
# result_textをSpeechSynthesisで音声合成し、生成した音声データをoutput_pathにmp3形式で保存
SpeechSynthesis.speech_synthesis(result_text, output_path)
# output_pathに保存した音声データをwav形式に変換したうえで再生
sound.playsound(output_path)
