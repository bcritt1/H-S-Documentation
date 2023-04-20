import argparse
import torch
import torchaudio
import librosa
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

def resample_audio(file):
    # Load the audio file and resample to 16000 Hz
    waveform, sample_rate = librosa.load(file, sr=16000, mono=True)
    waveform = torch.from_numpy(waveform)

    return waveform, sample_rate

def transcribe(file):
    # Load the pre-trained wav2vec2 model and processor
    model = Wav2Vec2ForCTC.from_pretrained('facebook/wav2vec2-base-960h')
    processor = Wav2Vec2Processor.from_pretrained('facebook/wav2vec2-base-960h')

    # Resample the audio file to 16000 Hz
    waveform, sample_rate = resample_audio(file)

    # Perform the wav2vec2 transcription
    input_values = processor(waveform, sampling_rate=sample_rate, return_tensors='pt').input_values
    with torch.no_grad():
        logits = model(input_values).logits
        transcription = processor.decode(torch.argmax(logits, dim=-1)[0])

    # Print the transcription. Outputs are routed through the .out files defined in the sbatch script
    print(transcription)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, required=True,
                        help='Path to the audio file')
    args = parser.parse_args()

    transcribe(args.file)
