from cleaning import cleaning_tildes,cleaning_html_words,lower_string
from transformers import TextClassificationPipeline,AutoModelForSequenceClassification,AutoTokenizer
from pysentimiento import create_analyzer
import json 

tokenizer =  AutoTokenizer.from_pretrained("finiteautomata/beto-sentiment-analysis")
model2=AutoModelForSequenceClassification.from_pretrained("bias_model_2",local_files_only=True)
pipe = TextClassificationPipeline(model=model2, tokenizer=tokenizer, return_all_scores=True)

with open('configs/predict_config.json') as json_file:
    predict_dict = json.load(json_file)

hate_speech_analyzer = create_analyzer(task="hate_speech", lang="es")

class Prediction():
    def __init__(self):  
        self.predict_dict = predict_dict
        self.hate_speech_analyzer = pipe

    def infer(self,info):
        response  = {
            "texto":[],
            "main_titles":[],
            "second_titles":[]
        }
        data  = info.dict()
        print('imprimiendo data ')
        for llave,valores in data.items():
            if valores != []:
                valores = list(map(lower_string,valores))
                valores = list(map(cleaning_tildes,valores))
                valores = list(map(cleaning_html_words,valores))
                predicts = self.hate_speech_analyzer(valores) 
                print(valores)
                for index,valor in enumerate(valores):
                    print('imprimiendo la data limpia *********************')
                    predicts = self.hate_speech_analyzer(valor) 
                    response[llave].append(predicts[0][0]["score"])
        return response 

    # def __model_answer_to_front(self,predicts,index: int)-> str: 
    #     print('Modificando las etiquetas del modelo por colores')
    #     prediction = predicts[index].output
    #     print(prediction)
    #     if prediction == []:
    #         prediction_result = 'rgba(0,0,0,0)'
    #         return prediction_result
    #     prediction.sort() 
    #     key_value = ','.join(prediction)
    #     prediction_result = self.predict_dict[key_value]
    #     return prediction_result 