# Whisper Transcription Tool

A comprehensive Python application for audio recording, transcription, and processing using OpenAI's Whisper API and GPT-4.

## Features

- Audio recording from microphone
- Transcription using OpenAI's Whisper API
- Post-transcription processing with GPT-4
- Rich terminal interface
- File management capabilities

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd whisper-transcription-tool
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

The tool provides three main commands:

1. Record audio:
```bash
python main.py record
```

2. Transcribe an audio file:
```bash
python main.py transcribe path/to/audio_file.wav
```

3. Process a transcription:
```bash
python main.py process path/to/transcription.txt
```

## Development

This project uses:
- Python 3.12+
- OpenAI API
- Rich for terminal UI
- Click for CLI interface

## License

MIT License 