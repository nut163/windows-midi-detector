```python
import mido

class MidiParser:
    def __init__(self):
        self.midi_info = {
            'keys': [],
            'knobs': [],
            'velocity': []
        }

    def parse_midi(self, midi_event):
        msg = mido.parse(midi_event)
        if msg.type == 'note_on':
            self.midi_info['keys'].append(msg.note)
            self.midi_info['velocity'].append(msg.velocity)
        elif msg.type == 'control_change':
            self.midi_info['knobs'].append(msg.control)

        return self.midi_info
```