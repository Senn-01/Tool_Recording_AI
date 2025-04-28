import os
import click
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from dotenv import load_dotenv
from openai import OpenAI
import time

# Initialize rich console for beautiful terminal UI
console = Console()

def setup_environment():
    """Load environment variables and initialize OpenAI client"""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        console.print("[red]Error: OPENAI_API_KEY not found in environment variables[/red]")
        raise ValueError("OPENAI_API_KEY is required")
    return OpenAI(api_key=api_key)

def record_audio():
    """Record audio from microphone"""
    # TODO: Implement audio recording
    console.print("[yellow]Audio recording functionality coming soon...[/yellow]")

def transcribe_audio(client, audio_file):
    """Transcribe audio file using Whisper API"""
    try:
        if not os.path.exists(audio_file):
            console.print(f"[red]Error: Audio file '{audio_file}' not found[/red]")
            return

        with Progress() as progress:
            task = progress.add_task("[cyan]Transcribing audio...", total=100)
            
            # Open and send the audio file for transcription
            with open(audio_file, "rb") as audio:
                # Create transcription using whisper-1 model
                response = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio,
                    response_format="text"
                )
                progress.update(task, advance=100)

            # Save transcription to a file
            output_file = f"{os.path.splitext(audio_file)[0]}_transcription.txt"
            with open(output_file, "w") as f:
                f.write(response)

            console.print(f"[green]✓ Transcription completed and saved to: {output_file}[/green]")
            return output_file

    except Exception as e:
        console.print(f"[red]Error during transcription: {str(e)}[/red]")
        return None

def process_transcription(client, transcription):
    """Process transcription with GPT-4"""
    # TODO: Implement post-processing
    console.print("[yellow]Post-processing functionality coming soon...[/yellow]")

@click.group()
def cli():
    """Whisper Transcription Tool - A comprehensive audio recording and transcription tool"""
    pass

@cli.command()
def record():
    """Record audio from microphone"""
    console.print(Panel.fit("🎤 Starting Audio Recording", style="bold blue"))
    record_audio()

@cli.command()
@click.argument('audio_file')
def transcribe(audio_file):
    """Transcribe an audio file"""
    console.print(Panel.fit("📝 Starting Transcription", style="bold blue"))
    client = setup_environment()
    transcribe_audio(client, audio_file)

@cli.command()
@click.argument('transcription_file')
def process(transcription_file):
    """Process a transcription file"""
    console.print(Panel.fit("🤖 Starting Post-Processing", style="bold blue"))
    client = setup_environment()
    with open(transcription_file, 'r') as f:
        transcription = f.read()
    process_transcription(client, transcription)

if __name__ == "__main__":
    cli()
