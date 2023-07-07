```python
import logging

class MidiLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        logging.basicConfig(filename=self.log_file, level=logging.INFO)

    def log_midi(self, midi_info):
        logging.info(f"MIDI Event: {midi_info}")

if __name__ == "__main__":
    logger = MidiLogger("logs/midi_logs.txt")
    midi_info = {"keys": "C4", "knobs": "Knob1", "velocity": 127}
    logger.log_midi(midi_info)
```