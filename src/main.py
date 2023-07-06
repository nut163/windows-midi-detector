```python
import midi_controller
import midi_parser
import midi_logger
import gui

log_file = "logs/midi_logs.txt"

def main():
    controller = midi_controller.MidiController()
    parser = midi_parser.MidiParser()
    logger = midi_logger.MidiLogger(log_file)
    gui_instance = gui.GUI()

    while True:
        midi_event = controller.get_midi_event()
        midi_info = parser.parse_midi(midi_event)
        logger.log_midi(midi_info)
        gui_instance.display_midi(midi_info)

if __name__ == "__main__":
    main()
```