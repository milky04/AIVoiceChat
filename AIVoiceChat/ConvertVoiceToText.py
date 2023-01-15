import whisper

whisper_model = whisper.load_model("small")
language = 'ja'

def convert_voice_to_text(audio):
    result = whisper_model.transcribe(
        audio,
        verbose=True,
        language=language,
        fp16=False
        )
    result_text = result['text']
    return result_text
