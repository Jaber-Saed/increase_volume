from pydub import AudioSegment

def increase_volume(input_file: str, output_file: str, db_increase: float):
    """
    Increase the volume of an MP3 file by a specified number of decibels.
    
    Parameters:
    - input_file (str): Path to the input MP3 file.
    - output_file (str): Path to save the output MP3 file.
    - db_increase (float): The amount of decibels to increase the volume.
    """
    # Load the audio file
    audio = AudioSegment.from_mp3(input_file)
    
    # Increase the volume
    louder_audio = audio.apply_gain(db_increase)
    
    # Export the modified audio to a new file
    louder_audio.export(output_file, format="mp3")
    print(f"Volume increased by {db_increase} dB and saved to {output_file}")

# Usage Example
input_file = "input.wav"
output_file = "output_louder.mp3"
db_increase = 10.0  # Increase by 10 dB

increase_volume(input_file, output_file, db_increase)
