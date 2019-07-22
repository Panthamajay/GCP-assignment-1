from google.cloud import storage

#Creating a bucket
bucket_name = 'ques4-buck'
storage_client = storage.Client()
bucket = storage_client.create_bucket(bucket_name)
print('Bucket {} created'.format(bucket.name))


#uploading in the bucket
bucket = storage_client.get_bucket(bucket_name)
destination_blob_name = 'first1.txt'
source_file_name = 'Desktop/first.txt'
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(source_file_name)
print('File {} uploaded to {}.'.format(source_file_name,destination_blob_name))


#downloading from tbe bucket
source_blob_name = 'second.txt'
destination_file_name = 'Desktop/second.txt'
blob = bucket.blob(source_blob_name)
blob.download_to_filename(destination_file_name)
print('Blob {} downloaded to {}.'.format(source_blob_name, destination_file_name))

#Deleting a blob
blob_name = 'pic.doc'
blob = bucket.blob(blob_name)
blob.delete()
print('Blob {} deleted.'.format(blob_name))


