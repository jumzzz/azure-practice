import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__



def write_sample_text(file_path):
    with open(file_path, 'w') as f:
        f.write('hello this is content.')


def upload_blob(blob_client, file_path):
    with open(file_path, 'rb') as data:
        blob_client.upload_blob(data)


def list_blobs(container_client):
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print('\t' + blob.name)
        

def main():
    try:
        print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        # Quick start code goes here
        
        print('Connection String = ', connect_str)
        
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_name = str(uuid.uuid4())

        print('Container name = ', container_name)
        # Create container client
        container_client = blob_service_client.create_container(container_name)

        file_path = 'sample_text2.txt'
        write_sample_text(file_path)

        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_path)

        upload_blob(blob_client, file_path)        
        list_blobs(container_client)


    except Exception as ex:
        print('Exception:')
        print(ex)


if __name__ == '__main__':
    main()