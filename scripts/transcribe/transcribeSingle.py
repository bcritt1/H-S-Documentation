import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import pandas as pd

#load pre-trained model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

#load any audio file of your choice
speech, rate = librosa.load("/Users/bcritt/Documents/StanfordProjects/Corpora/audio/recording1.wav",sr=16000)

input_values = tokenizer(speech, return_tensors = 'pt').input_values

#Store logits (non-normalized predictions)
logits = model(input_values).logits

#Store predicted id's
predicted_ids = torch.argmax(logits, dim =-1)

#decode the audio to generate text
transcriptions = tokenizer.decode(predicted_ids[0])
df = pd.DataFrame([transcriptions])
df.to_csv("/Users/bcritt/Documents/StanfordProjects/Corpora/audio/transcribe.csv")
