import requests
import configparser
import argparse


class RawMangaTranslator:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    def translate(self, image):
        sentences = []
        translated_sentences = []

        # Microsoft API Variables
        headers = {
            "Ocp-Apim-Subscription-Key": self.config["MicrosoftAPI"]["KEY"]}
        payload = {"detectOrientation": "true"}
        data = {"url": image}

        # First, we'll need to extract the words from the image using Microsoft OCR API
        request = requests.post(self.config["MicrosoftAPI"]["URL"],
                                params=payload, headers=headers, json=data)
        result = request.json()

        # Add sentences to the array so we can translate it later
        for s in result["regions"][0]["lines"]:
            sentence = ""

            for word in s["words"]:
                sentence += word["text"]

            sentences.append(sentence)

        print(sentences)

        # Finally, we'll translate the sentences extracted from the image!
        for sentence in sentences:
            data = {"target": "en",
                    "key": self.config["GoogleAPI"]["KEY"],
                    "q": sentence}

            request = requests.get(
                self.config["GoogleAPI"]["URL"], params=data)
            result = request.json()

            translated_sentences.append(
                result["data"]["translations"][0]["translatedText"])

        print(translated_sentences)


# Now, let us start the main show!
if __name__ == "__main__":
    # Set arguments for this program
    parser = argparse.ArgumentParser(description="Translates text in raw manga chapter images.")
    parser.add_argument("--url", help="enter the url of the image you want translated")
    args = parser.parse_args()

    if (args.url):
        translator = RawMangaTranslator()

        translator.translate(args.url)
