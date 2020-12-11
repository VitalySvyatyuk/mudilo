W = '[A-Za-zА-Яа-я]'

word_map = {  # cyrillic to latin map
    'а': 'a', 'в': 'b', 'е': 'e', 'к': 'k', 'м': 'm', 'н': 'h',
    'о': 'o', 'р': 'p', 'с': 'c', 'т': 't', 'у': 'y', 'х': 'x'
}

regex = {
    'ru': [
        '^[a-z]{1}[0-9]{3}[a-z]{2}[0-9]{2,3}[a-z]*'
    ],
    'am': [
        '^[0-9]{2,3}[a-z]{2}[0-9]{3}',
        '^[0-9]{3}[a-z]{2}[0-9]{2}'
    ],
    'by': [
        '^[0-9]{4}[a-z]{2}[0-9]{1}'
    ],
    'ua': [
        '^[a-z]{2}[0-9]{4}[a-z]{2}'
    ]
}
