import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import pandas as pd
import numpy as np
import os
import sys

#load pre-trained model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

pathAudio = "/home/users/bcritt/audio/"
files = librosa.util.find_files(pathAudio, ext=['wav'])
files = np.asarray(files)
info=[]
for y in files:
	data = librosa.load(y, sr=16000)
	data = data[0]
	input_values = tokenizer(data, return_tensors = 'pt').input_values
	logits = model(input_values).logits
	predicted_ids = torch.argmax(logits, dim =-1)
	transcriptions = tokenizer.decode(predicted_ids[0])
	info.append(transcriptions)

df = pd.DataFrame(info)
df.to_csv("/scratch/users/bcritt/outputs/transcribe.csv")
