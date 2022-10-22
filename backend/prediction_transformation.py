

def model_answer_to_front(predict_dict: dict, predicts,index: int)-> str: 
    print('Modificando las etiquetas del modelo por colores')
    prediction = predicts[index].output
    print(prediction)
    if prediction == []:
        prediction_result = 'rgba(0,0,0,0)'
        return prediction_result
    prediction.sort() 
    key_value = ','.join(prediction)
    prediction_result = predict_dict[key_value]
    return prediction_result 