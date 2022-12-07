import requests
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog


URL = "https://api.magicthegathering.io/v1/cards"

def main():
    # make a request with the request library
    magicrequest = requests.get(URL )
    card = mtgsk.Card.find(386616)
    cards = Card.all
     
    print(card, cards)
    print(dir(card)) ##Shows all the objects associated with it.
    print(type(card))
    
    # strip off json attachment from our response
    #magicdata = magicrequest.json()

    ## display NASAs NEOW data
    #print(magicdata['cards'])
    #for card in magicdata['cards']:
        #print(f"{card['name']}")
        #print(f"\t{card['setName']} \n")
        





if __name__ == "__main__":
    main()