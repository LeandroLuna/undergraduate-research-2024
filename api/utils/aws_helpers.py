import psycopg2
import boto3
from botocore.exceptions import NoCredentialsError
from utils.constants import AWS_RDS_ENDPOINT, AWS_RDS_DATABASE, AWS_RDS_USER, AWS_RDS_PASSWORD, AWS_S3_BUCKET_NAME

s3_client = boto3.client('s3')

def upload_file_to_s3(file_path, subdirectory, bucket_name=AWS_S3_BUCKET_NAME):
    try:
        s3_key = f"{subdirectory}/{file_path.name}"
        s3_client.upload_file(str(file_path), bucket_name, s3_key)
        return f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"
    except FileNotFoundError:
        print("The file was not found")
        return None
    except NoCredentialsError:
        print("Credentials not available")
        return None
    finally:
        file_path.unlink()

def insert_prediction_data(id, fractured, img_file_path, img_labels_file_path, object_data):
    connection = None
    
    try:
        connection = psycopg2.connect(
            host=AWS_RDS_ENDPOINT,
            database=AWS_RDS_DATABASE,
            user=AWS_RDS_USER,
            password=AWS_RDS_PASSWORD
        )
        cursor = connection.cursor()

        postgres_insert_query = """ 
        INSERT INTO predictions (id, fractured, img_file_path, img_labels_file_path, object) 
        VALUES (%s, %s, %s, %s, %s)
        """
        
        record_to_insert = (id, fractured, img_file_path, img_labels_file_path, object_data)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into predictions table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into predictions table", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

def get_all_predictions(limit: int = 10, offset: int = 0):
    connection = None
    try:
        connection = psycopg2.connect(
            host=AWS_RDS_ENDPOINT,
            database=AWS_RDS_DATABASE,
            user=AWS_RDS_USER,
            password=AWS_RDS_PASSWORD
        )
        cursor = connection.cursor()

        select_query = "SELECT * FROM predictions ORDER BY id LIMIT %s OFFSET %s"
        cursor.execute(select_query, (limit, offset))
        predictions = cursor.fetchall()

        return predictions

    except (Exception, psycopg2.Error) as error:
        print("Failed to get predictions from predictions table", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            
def get_prediction_by_id(prediction_id):
    connection = None
    
    try:
        connection = psycopg2.connect(
            host=AWS_RDS_ENDPOINT,
            database=AWS_RDS_DATABASE,
            user=AWS_RDS_USER,
            password=AWS_RDS_PASSWORD
        )
        cursor = connection.cursor()

        select_by_id_query = "select * from predictions where id = %s"
        cursor.execute(select_by_id_query, (prediction_id,))
        prediction = cursor.fetchone()

        return prediction

    except (Exception, psycopg2.Error) as error:
        print("Failed to get prediction from predictions table", error)

    finally:
        if connection:
            cursor.close()
            connection.close()