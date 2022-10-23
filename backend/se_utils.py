import boto3
from boto3.s3.transfer import TransferConfig

class S3Utils:
    def init(self):
        self.client = boto3.client('s3')
        self.resource = boto3.resource('s3')


    def upload_to_aws(self,local_file, bucket, s3_file):
        config = TransferConfig(multipart_threshold=1024*20, max_concurrency=10,
                                multipart_chunksize=1024*5, use_threads=True)

        try:
            self.client.upload_file(local_file, bucket, s3_file, Config=config)
            print("Upload Successful")
            return True
        except Exception as e:
            print(e)
            return False

    def get_s3_file(self,bucket, prefix):
        lista_name_file=[]
        result = self.client.list_objects(Bucket=bucket, Prefix=prefix, Delimiter='/')
        for filename in result['Contents']:
            file = filename['Key'].split('/')[-1]
            lista_name_file.append(file)
            self.resource.Bucket(bucket).download_file(filename['Key'], '/tmp/'+file)

        return lista_name_file
    
    def delete_file(self, bucket, prefix):
        result = self.client.list_objects(Bucket=bucket, Prefix=prefix)
        for file in result.get('Contents', []):
            self.resource.Object(bucket, file['Key']).delete()