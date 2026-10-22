# Third-Party Packages
import requests
import astrathon

# Helper Files
import slugify as slg

# Python Package
import os.path
import shutil
import json

USER_AGENT = 'AstraPrinter/0.1 (tankangzheng2000@gmail.com)'
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "image/*;q=0.9,*/*;q=0.8",
}

class CardData:
    name = None
    imgLink = None

    def __init__(self, name:str):
        self.name = name

    def __repr__(self):
        return f"CardData(name='{self.name}', imgLink='{self.imgLink}')"

def parseDecklist(decklist:str, log_func=print):
    parsedList = []

    if "{" in decklist: #JSON type export from astraplayer
        for item in json.loads(decklist):
            parsedList.append(CardData(item["name"]))
    else: #Typical list, AstraBook type export
        cardList = decklist.split("\n")
        for item in cardList:
            # Check if the string contains a number: ensures its a card name and not header (e.g Main Deck)
            if (any(char.isdigit() for char in item)):
                # Truncate number at front by searching for first whitespace in line
                parsedList.append(CardData(item[item.find(" ")+1:]))
                print(parsedList[-1])


    # Generate the list of card image links
    parsedList = generateCardImageLink(parsedList, log_func=log_func)

    return parsedList

def generateCardImageLink(cardList:list[CardData], log_func=print) -> list[CardData]:
    returnList = []
    for cardEntry in cardList:
        try:
            card = astrathon.search(cardEntry.name)
        except:
            log_func(f"Could not find card, skipping {cardEntry.name}...")
            continue
        log_func(f"Found {cardEntry.name}")

        cardEntry.imgLink = card[0].cardImageLargeUrl
        returnList.append(cardEntry)

    return returnList
    
def saveImage(cardData:CardData, savepath, log_func=print):
    image_name = slg.slugify(cardData.name) + ".png"
    path = os.path.join(savepath, image_name)
    log_func(f"Downloading {cardData.imgLink}")
    try:
        with requests.get(
            cardData.imgLink,
            stream=True,
            timeout=15,
            headers=HEADERS
        ) as r:
            if r.status_code != 200:
                log_func(f"Failed ({r.status_code}): {cardData.name}")
                print(r.text)
                return
            with open(path, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

    except requests.RequestException as e:
        log_func(f"Error downloading {cardData.name}: {e}")