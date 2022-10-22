import re 

words_to_delete = ['Δdocument','getElementById', 'ak_js_2',\
'setAttribute', 'value','new', 'Date', 'getTime']

def cleaning_tildes(sentence: str)->str: 
    """
    Definition: replace the tildes found in the sentence
    """
    sentence = sentence.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u') 

    return sentence 


def cleaning_html_words(sentence:str)-> str:
    """
    Definition: Delete any html/js/css tag found at the moment of scrapping the data. 
                Also deletes not alphanumeric chars found in the sentence
    input: the sentence we are trying to clean 
    output: the sentence cleaned
    """
     
    words_to_delete = ['Tus respuestas ayudan a mejorar la experiencia de la Búsqueda de Google.',\
    'Nota: Tus comentarios no influirán de forma directa en la clasificación de ninguna página.Más información',\
    '\xa0','Δdocument','getelementbyid', 'ak_js_2',\
    'setattribute', 'value','new', 'Date', 'getTime','ak_js_3','Debe responder al hcaptcha',\
    'Guarda mi nombre correo electrónico y web en este navegador para la próxima vez que comente',\
    ] 
    sentence = re.sub(r'\W+', ' ', sentence)
    for word in words_to_delete: 
        sentence = sentence.replace(word,'') 
    return sentence 