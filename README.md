# Raw Manga Translator

## Inspiration
One early Wednesday morning, I woke up excitedly to read a new chapter on One Piece. However, there was no translated text yet. With anger, frustration, bargaining, depression, and acceptance, we decided to start this project to prevent this from happening again.

## How I built it
- Python 3
- Microsoft's Cognitive Services (for extracting text)
- Google Translate API (for translating text)

## How to use the application
### Prerequistites
- Install [Python 3+](https://www.python.org/downloads/)
- Get an API key for [Microsoft's Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/)
- Get an API key for [Google Translate API](https://cloud.google.com/translate/docs/)

### Steps
1. Clone the repository.
2. Open the command line and navigate to the repository.
3. Type `pip install -r requirements.txt` and enter.
4. Open `config.ini` in a code editor and put your API keys for both APIs.
5. Run the application using `python main.py --url IMAGE_URL`.

## Future Work
- Replace the text inside the image with translated text
- Improve the translations