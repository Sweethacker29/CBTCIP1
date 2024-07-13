import sounddevice as sd
import wavio

def record_audio(duration, filename, sample_rate=44100):
    print("Recording...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording finished.")

    # Save the recording to a WAV file
    wavio.write(filename, recording, sample_rate, sampwidth=2)
    print(f"Audio saved as {filename}")

if __name__ == "__main__":
    duration = int(input("Enter the duration of the recording in seconds: "))
    filename = input("Enter the filename to save the recording (e.g., output.wav): ")
    
    record_audio(duration, filename)
