import boto3
import pandas as pd 
from s3_utils import S3Utils

s3 = S3Utils() 


def building_dataframe(response: dict)->pd.DataFrame:
    print('Recogiendo los datos y enviandolos a s3')
    df = pd.DataFrame(data=response)
    df.to_csv('resultados.csv',sep=',',index=None) 
    s3.upload_to_aws(local_file='resultados.csv',bucket='stage',s3_file='stage_files/stage_resultados.csv')