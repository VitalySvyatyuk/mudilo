import re

from .plate_regex import regex, word_map


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


def map_words(plate):
    # change all cyrillic to latin
    for cyrillic, latin in word_map.items():
        plate = plate.replace(cyrillic, latin)
    return plate


def pre_return(plate, country):
    if country == 'Ru':
        # remove the last tail 'rus,ru...'
        last = re.split('[0-9]{2,3}', plate)[-1]
        if last:
            plate = rreplace(plate, last, '', 1)
    return plate, country


def validate_plate(plate):
    for country, masks in regex.items():
        for mask in masks:
            if re.match(mask, plate):
                return pre_return(plate, country)
    return None, None
