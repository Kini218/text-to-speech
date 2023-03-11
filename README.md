# PDF to MP3 Converter

This Python script converts PDF and TXT files into MP3 audio files using Google Text-to-Speech (gTTS). The script checks if the specified file exists, ensures that the file extension is either a PDF or TXT file, and checks if the specified language is supported by gTTS. 

The script uses pdfplumber to extract text from PDF files and replaces any issues with the Russian letter 'к'. Once the text is extracted, gTTS is used to generate an MP3 file from the text in the specified language. The script is designed to be easy to use, with a simple command-line interface that prompts the user for the file path and language input.

## Requirements

- Python 3.x
- pdfplumber
- gtts

## Usage

To use the script, simply run it in the terminal and provide the file path and language input when prompted:

```python
python text_to_speech.py
```


The script will generate an MP3 file with the same name as the input file in the same directory. If there are any issues during the conversion process, the script will display an error message and exit. 

## Supported Languages

Google Text-to-Speech supports a wide variety of languages, which can be specified using the language code. Here is a table of some of the supported languages and their language codes:

| Language | Language Code |
| --- | --- |
| English | en |
| French | fr |
| German | de |
| Italian | it |
| Spanish | es |
| Russian | ru |
| Japanese | ja |
| Korean | ko |

For a full list of supported languages and their codes, you can refer to the [gTTS documentation](https://gtts.readthedocs.io/en/latest/module.html). 
