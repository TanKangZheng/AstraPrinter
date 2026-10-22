# AstraPrinter

An Echoes of Astra proxy preparer for services like MakePlayingCards.

## Description

This project aims to be a one-click preperator for converting an Echoes of Astra deck into MakePlayingCards-project ready images, removing the need to manually prepare each individual card.

## Getting Started

### Dependencies

These dependencies are only required if you are building the project yourself! The standalone executable has been done so that you don't need any other dependencies, installs, or setup.

* Python 3.11.4
    * Run `pip install -r requirements.txt` in the project folder

### Installing

* **Self-Building the Project**
    * Compiled and Tested on Python 3.11.4
    * External Package requirements are listed in [requirements.txt](requirements.txt)
    * Pull the repo, and simply run the main.py file
* **Standalone Executable (exe)**
    * Download the AstraPrinter zip file from Downloads
    * Extract the folder, and run AstraPrinter.exe
    * The exe is not malware, I swear.

## Usage

* **Left Column | Input and Functions**
    * Input Text Field
        * *The large input text field is where you will paste your decklist exports*
        * *Currently, this project supports [Astraplay](https://app.echoesofastra.com/deck-builder) and [Astrabook](https://astrabook.net/) deck exports*
    * Load Images
        * *This button will attempt to fetch all cards you've added*
        * *Once loaded, the preview images will show on the right column*
    * Download Images
        * *This button will begin downloading card images for all cards added*
        * *Once downloaded, it will apply all features that have been enabled to the images*
        * *Once complete, it will open the file location of the images*
    * Optional Enhancement Features
        * ***Foil:*** *When printing using MakePlayingCard's foil finish, the images tend to be a bit washed. Enabling this feature will boost the saturation and vibrancy of the card.*
        * ***Upscale:*** *Enabling this option will upscale the card images by 2x. Not mandatory since it is almost un-noticeable when printed.*

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the [LICENSE.MD](LICENSE.MD) file for details.

## Acknowledgments
Huge thanks to the Echoes of Astra team for providing an open source API to access card information and images.
**Echoes of Astra**
* [Echoes of Astra Website](https://echoesofastra.com/)
* [Echoes of Astra Discord](https://discord.gg/Qfknb8HW94)

The slugify function used to ensure that filenames are safe and legal (for your computer to use as a filepath) was taken from another online repo as it was the first thing to pop up.

**Django**
* [Django/django/utils/text.py](https://github.com/django/django/blob/main/django/utils/text.py)
