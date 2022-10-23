import boto3
import pandas as pd 


 


def building_dataframe(response: dict, s3)->pd.DataFrame:
    print('Recogiendo los datos y enviandolos a s3')
    df = pd.DataFrame(data=response)
    df.to_csv('resultados.csv',sep=',',index=None) 
    s3.upload_file(local_file='resultados.csv',bucket='stage-buck',s3_file='stage_files/stage_resultados.csv')