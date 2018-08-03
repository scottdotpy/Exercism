# hello_world_extended
# Scott @ scottdotpy
# 30 July 2018

# This script will fail the hello_world test on all passes

# Imports ------------------------------------------------------------------ #

import random

# Dictionaries ------------------------------------------------------------- #

languages = {'Afrikaans': 'Hello Wêreld!', 'Albanian': 'Përshendetje Botë!',
             'Amharic': 'ሰላም ልዑል!', 'Arabic': ' مرحبا بالعالم!',
             'Armenian': 'Բարեւ աշխարհ!', 'Basque': 'Kaixo Mundua!',
             'Belarussian': 'Прывітанне Сусвет!', 'Bengali': 'ওহে বিশ্ব!',
             'Bulgarian': 'Здравей свят!', 'Catalan': 'Hola món!',
             'Chichewa': 'Moni Dziko Lapansi!', 'Chinese': '你好世界！',
             'Croatian': 'Pozdrav svijete!', 'Czech': 'Ahoj světe!',
             'Danish': 'Hej Verden!', 'Dutch': 'Hallo Wereld!',
             'English': 'Hello World!', 'Estonian': 'Tere maailm!',
             'Finnish': 'Hei maailma!', 'French': 'Bonjour monde!',
             'Frisian': 'Hallo wrâld!', 'Georgian': 'გამარჯობა მსოფლიო!',
             'German': 'Hallo Welt!', 'Greek': 'Γειά σου Κόσμε!',
             'Hausa': 'Sannu Duniya!', 'Hebrew': 'שלום עולם!',
             'Hindi': 'नमस्ते दुनिया!', 'Hungarian': 'Helló Világ!',
             'Icelandic': 'Halló heimur!', 'Igbo': 'Ndewo Ụwa!',
             'Indonesian': 'Halo Dunia!', 'Italian': 'Ciao mondo!',
             'Japanese': 'こんにちは世界！', 'Kazakh': 'Сәлем Әлем!',
             'Khmer': 'សួស្តី​ពិភពលោក!', 'Kyrgyz': 'Салам дүйнө!',
             'Lao': 'ສະ​ບາຍ​ດີ​ຊາວ​ໂລກ!', 'Latvian': 'Sveika pasaule!',
             'Lithuanian': 'Labas pasauli!', 'Luxemburgish': 'Moien Welt!',
             'Macedonian': 'Здраво свету!', 'Malay': 'Hai dunia!',
             'Malayalam': 'ഹലോ വേൾഡ്!', 'Mongolian': 'Сайн уу дэлхий!',
             'Myanmar': 'မင်္ဂလာပါကမ္ဘာလောက!', 'Nepali': 'नमस्कार संसार!',
             'Norwegian': 'Hei Verden!', 'Pashto': 'سلام نړی!',
             'Persian': 'سلام دنیا!', 'Polish': 'Witaj świecie!',
             'Portuguese': 'Olá Mundo!', 'Punjabi': 'ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਦੁਨਿਆ!',
             'Romanian': 'Salut Lume!', 'Russian': 'Привет мир!',
             'Scots Gaelic': 'Hàlo a Shaoghail!', 'Serbian': 'Здраво Свете!',
             'Sesotho': 'Lefatše Lumela!', 'Sinhala': 'හෙලෝ වර්ල්ඩ්!',
             'Slovenian': 'Pozdravljen svet!', 'Spanish': '¡Hola Mundo!',
             'Sundanese': 'Halo Dunya!', 'Swahili': 'Salamu Dunia!',
             'Swedish': 'Hej världen!', 'Tajik': 'Салом Ҷаҳон!',
             'Thai': 'สวัสดีชาวโลก!', 'Turkish': 'Selam Dünya!',
             'Ukrainian': 'Привіт Світ!', 'Uzbek': 'Salom Dunyo!',
             'Vietnamese': 'Chào thế giới!', 'Welsh': 'Helo Byd!',
             'Xhosa': 'Molo Lizwe!', 'Yiddish': 'העלא וועלט!',
             'Yoruba': 'Mo ki O Ile Aiye!', 'Zulu': 'Sawubona Mhlaba!'
             }

# Functions ---------------------------------------------------------------- #


def hello():
    # Converts values form languages dict to list then chooses one at random
    return random.choice(list(languages.values()))


# Script ------------------------------------------------------------------- #

print(hello())
