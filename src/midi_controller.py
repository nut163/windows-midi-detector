```python
import mido
from mido import MidiFile

class MidiController:
    def __init__(self):
        self.midi_info = {
            'keys': [],
            'knobs': [],
            'velocity': []
        }

    def detect_midi(self):
        for msg in MidiFile('midi_file.mid'):
            if msg.type == 'note_on':
                self.midi_info['keys'].append(msg.note)
                self.midi_info['velocity'].append(msg.velocity)
            elif msg.type == 'control_change':
                self.midi_info['knobs'].append(msg.control)

    def get_midi_info(self):
        return self.midi_info

    def send_midi_event(self, midi_event):
        self.detect_midi()
        midi_event(self.get_midi_info())
```