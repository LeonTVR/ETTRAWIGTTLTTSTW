﻿import moviepy.editor as mp
import ffmpeg
import os
import torch
import matplotlib.pyplot as plt

def isNumber(string):
    try:
        float(string)

        return True
    except ValueError:
        return False

def matrixMultiplyChunk(collumn, row, kernelSize, matrixInput, matrixMultiplier):
    chunk = matrixInput[row-1:row-1+kernelSize+1]

    return torch.matmul(chunk, matrixMultiplier)

def runKernel(kernel, matrixInput, step, kernelSize):
    matrix = matrixInput

    convoluting = True

    row = 0
    collumn = 0

    while convoluting:
        # Sees if the kernel is at the end of its row. Then checks if it's at the end of its collumn, if it's both, then it stops convoluting since it's done.

        if collumn > matrix.shape[1]-(kernelSize-1):
            if row > matrix.shape[0]-(kernelSize-1):
                convoluting = False
            else:
                collumn = 0

                row += 1

        matrixMultiplyChunk(collumn, row, kernelSize, matrix, kernel)

    return matrix

def getPhoneme(path):
    # This turns the audio slice that it gets from the video and turns it into a spectrogram for the CNN.

    out, _ = ffmpeg.input("slice.wav").output("pipe:1", format="wav", ac=1, ar="32000").run(capture_stdout=True, quiet=True)

    audioData = torch.frombuffer(out, dtype=torch.int16)

    plt.figure(figsize=(0.5, 1))
    plt.specgram(audioData.detach().cpu().numpy(), Fs=32000, NFFT=1024, noverlap=512, cmap="gray")

    plt.axis("off")

    plt.savefig("spectrogram.png", bbox_inches="tight", pad_inches=0, dpi=300)

    plt.close()

    spectrogram = plt.imread("spectrogram.png")

    collumn = 1
    row = 1

    step = 1

    kernelSize = 2

def main():
    wordList = []

    running = True

    percentage = 0

    weights = torch.tensor([[]])

    biases = torch.tensor([[]])

    connections = []

    print("Type path to video:")

    path = input()

    video = mp.VideoFileClip(path)

    duration = video.duration

    audioTime = 0

    audio = video.audio

    audio.write_audiofile("tempUncompressed.mp3")

    probeBitrate = ffmpeg.probe("tempUncompressed.mp3", v='error', select_streams='a', show_entries='stream=bit_rate')
    probeSampleRate = ffmpeg.probe("tempUncompressed.mp3", v='error', select_streams='a', show_entries='stream=sample_rate')

    bitrate = probeBitrate["streams"][0]['bit_rate']

    sampleRate = probeSampleRate["streams"][0]["sample_rate"]

    bitrate = int(bitrate)

    sampleRate = int(sampleRate)

    bitrate /= 1000

    if bitrate < 100:
        print("The video's audio bitrate is too low! Aborted.")

        running = False

    if sampleRate < 32000:
        print("The video's audio sample rate is too low! Aborted.")

        running = False

    ffmpeg.input("tempUncompressed.mp3").output("temp.mp3", audio_bitrate="100k", ar=32000, y=None).run(quiet=True)

    os.remove("tempUncompressed.mp3")

    # Opens the file that stores the whole model.

    model = open("model.txt", "r")

    modelString = model.read()

    currentNumber = ""

    currentStringToBeWrittenTo = 0

    for char in modelString:
        if char == "B":
            currentStringToBeWrittenTo = 1

        if currentStringToBeWrittenTo == 0:
            if isNumber(char):
                currentNumber += char
            else:
                if isNumber(currentNumber):
                    connections.append(float(currentNumber))

                currentNumber = ""

    while running:
        ffmpeg.input("temp.mp3", ss=audioTime, t=0.1).output("slice.wav", acodec="copy").run(quiet=True, overwrite_output=True)

        audioTime += 0.1

        percentage = audioTime/duration*100

        print(f"\rCreating video... {percentage:.2f}%   ", end="", flush=True)

        if audioTime >= duration:
            print("\nDone!")

            running = False

        getPhoneme("slice.wav")

main()
