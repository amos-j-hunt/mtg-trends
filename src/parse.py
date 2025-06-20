import os
import requests
import json
import pandas as pd

def load_json(path):
    ### Download AllPrintings.json if not already present
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        print('Downloading AllPrintings.json...')
        url = 'https://mtgjson.com/api/v5/AllPrintings.json'
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print('Download complete.')
        else:
            raise Exception(f'Failed to download: {response.status_code}')
    else:
        print('AllPrintings.json already exists.')
    
    ### Load the data into a dictionary
    with open('../data/AllPrintings.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def flatten_cards(data):
    all_cards = []
    allowed_types = ['core','expansion','draft_innovation','masters','commander']
    for set_code, set_data in data['data'].items():
        set_name = set_data['name']
        release_date = set_data['releaseDate']
        if set_data['type'] in allowed_types:  ### Only analyze the allowed set types.
            for card in set_data['cards']:
                if not card.get('isAlternative', False):  ### Avoid most duplicate cards in each set.
                    card_data = {
                        'set_code': set_code,
                        'set_name': set_name,
                        'release_date': release_date,
                        'name': card.get('name'),
                        'colors': card.get('colors', []),
                        'color_identity': card.get('colorIdentity', []),
                        'mana_cost': card.get('manaCost'),
                        'mana_value': card.get('convertedManaCost'),
                        'oracle_text': card.get('text') or card.get('oracleText'),
                        'rulings': card.get('rulings', []),
                        'type_line': card.get('type'),
                        'supertypes': card.get('supertypes', []),
                        'power': card.get('power'),
                        'toughness': card.get('toughness'),
                        'keywords': card.get('keywords', []),
                        'layout': card.get('layout')
                    }
                    all_cards.append(card_data)
    return all_cards

def to_dataframe(records):
    return pd.DataFrame(records)

