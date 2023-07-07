# MIDI Controller Information Detector

This application runs on Windows and detects MIDI information from external MIDI controllers. It provides a visual readout of what keys, knobs, etc are being pressed and at what velocity. The application also creates log files that log all of the information so it can be parsed later.

## Installation

1. Clone the GitHub repository to your local machine.
```
git clone <repo_url>
```
2. Navigate to the project directory.
```
cd <project_directory>
```
3. Install the required Python packages.
```
pip install -r requirements.txt
```
4. Run the setup file.
```
python setup.py install
```
For more detailed installation steps, please refer to the `src/installation_guide.txt`.

## Usage

To start the application, run the `src/main.py` script.
```
python src/main.py
```
The application will start detecting MIDI events from your external MIDI controller and display them on the GUI. All MIDI events will also be logged in the `logs/midi_logs.txt`.

## Contributing

Please read through our contributing guidelines. Included are directions for opening issues, coding standards, and notes on development.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.