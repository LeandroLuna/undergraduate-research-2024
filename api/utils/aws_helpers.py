import psycopg2
import boto3
from botocore.exceptions import NoCredentialsError
from utils.constants import AWS_RDS_ENDPOINT, AWS_RDS_DATABASE, AWS_RDS_USER, AWS_RDS_PASSWORD, AWS_S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from models.prediction import PredictionResult

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

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

def insert_prediction(id, detect, segment, img_url):
    connection = None
    
    try:
        connection = psycopg2.connect(
            host=AWS_RDS_ENDPOINT,
            database=AWS_RDS_DATABASE,
            user=AWS_RDS_USER,
            password=AWS_RDS_PASSWORD
        )
        cursor = connection.cursor()

        insert_prediction_query = """ 
            INSERT INTO predictions (id, detect, segment, img_url) 
            VALUES (%s, %s, %s, %s)
        """
        
        cursor.execute(insert_prediction_query, (id, detect, segment, img_url))
        connection.commit()
        
        count = cursor.rowcount
        print(count, "Record inserted successfully into predictions table")
        
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into predictions table", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()

def insert_prediction_data(model, id, fractured, img_file_path, img_labels_file_path, object_data):
    connection = None
    
    try:
        connection = psycopg2.connect(
            host=AWS_RDS_ENDPOINT,
            database=AWS_RDS_DATABASE,
            user=AWS_RDS_USER,
            password=AWS_RDS_PASSWORD
        )
        cursor = connection.cursor()

        if model == 'segment':
            insert_query = """ 
                INSERT INTO segment (fractured, img_file_path, img_labels_file_path, object, prediction_id) 
                VALUES (%s, %s, %s, %s, %s)
            """
        elif model == 'detect':
            insert_query = """ 
                INSERT INTO detect (fractured, img_file_path, img_labels_file_path, object, prediction_id) 
                VALUES (%s, %s, %s, %s, %s)
            """
        
        record_to_insert = (fractured, img_file_path, img_labels_file_path, object_data, id)
        cursor.execute(insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into", model, "table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into", model, "table", error)

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

        select_query = """
            SELECT 
                p.id, 
                p.detect, 
                p.segment, 
                p.img_url,
                s.id AS segment_id, 
                s.fractured AS segment_fractured,
                s.img_file_path AS segment_img_file_path, 
                s.img_labels_file_path AS segment_img_labels_file_path, 
                s.object AS segment_object,
                d.id AS detect_id, 
                d.fractured AS detect_fractured, 
                d.img_file_path AS detect_img_file_path,
                d.img_labels_file_path AS detect_img_labels_file_path, 
                d.object AS detect_object 
            FROM 
                predictions p
            LEFT JOIN 
                segment s ON p.id = s.prediction_id
            LEFT JOIN 
                detect d ON p.id = d.prediction_id
            ORDER BY p.id
            LIMIT %s OFFSET %s
        """
        cursor.execute(select_query, (limit, offset))
        predictions = cursor.fetchall()

        return predictions, total_records

    except (Exception, psycopg2.Error) as error:
        print("Failed to get predictions from predictions table", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

def get_total_predictions():
    connection = None

    try:
        connection = psycopg2.connect(
            host=AWS_RDS_ENDPOINT,
            database=AWS_RDS_DATABASE,
            user=AWS_RDS_USER,
            password=AWS_RDS_PASSWORD
        )
        cursor = connection.cursor()

        count_query = """
            SELECT COUNT(*)
            FROM predictions p
            LEFT JOIN segment s ON p.id = s.prediction_id
            LEFT JOIN detect d ON p.id = d.prediction_id
        """
        cursor.execute(count_query)
        total_records = cursor.fetchone()[0]

        return total_records

    except (Exception, psycopg2.Error) as error:
        print("Failed to get total predictions count", error)
        return 0

    finally:
        if connection:
            cursor.close()
            connection.close()
            
def get_prediction_by_id(prediction_id, model=None):
    connection = None
    
    try:
        connection = psycopg2.connect(
            host=AWS_RDS_ENDPOINT,
            database=AWS_RDS_DATABASE,
            user=AWS_RDS_USER,
            password=AWS_RDS_PASSWORD
        )
        cursor = connection.cursor()

        if model == 'segment':
            select_by_id_query = """
                SELECT 
                    p.id, 
                    p.detect, 
                    p.segment, 
                    p.img_url, 
                    s.fractured, 
                    s.img_file_path, 
                    s.img_labels_file_path, 
                    s.object 
                FROM 
                    predictions p
                LEFT JOIN 
                    segment s ON p.id = s.prediction_id
                WHERE 
                    p.id = %s
            """
        elif model == 'detect':
            select_by_id_query = """
                SELECT 
                    p.id, 
                    p.detect, 
                    p.segment, 
                    p.img_url, 
                    d.fractured, 
                    d.img_file_path, 
                    d.img_labels_file_path, 
                    d.object 
                FROM 
                    predictions p
                LEFT JOIN 
                    detect d ON p.id = d.prediction_id
                WHERE 
                    p.id = %s
            """
        else:
            select_by_id_query = """
                SELECT 
                    p.id, 
                    p.detect, 
                    p.segment, 
                    p.img_url, 
                    s.id AS segment_id, 
                    s.fractured AS segment_fractured,
                    s.img_file_path AS segment_img_file_path, 
                    s.img_labels_file_path AS segment_img_labels_file_path, 
                    s.object AS segment_object, 
                    d.id AS detect_id,
                    d.fractured AS detect_fractured, 
                    d.img_file_path AS detect_img_file_path,
                    d.img_labels_file_path AS detect_img_labels_file_path, 
                    d.object AS detect_object 
                FROM 
                    predictions p
                LEFT JOIN 
                    segment s ON p.id = s.prediction_id
                LEFT JOIN 
                    detect d ON p.id = d.prediction_id
                WHERE
                    p.id = %s
            """
            
        cursor.execute(select_by_id_query, (prediction_id,))
        prediction = cursor.fetchone()

        return prediction

    except (Exception, psycopg2.Error) as error:
        print("Failed to get prediction from predictions table", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            
def update_prediction(id, model):
    connection = None
    
    try:
        connection = psycopg2.connect(
            host=AWS_RDS_ENDPOINT,
            database=AWS_RDS_DATABASE,
            user=AWS_RDS_USER,
            password=AWS_RDS_PASSWORD
        )
        cursor = connection.cursor()

        if model == 'segment':
            update_query = """
                UPDATE predictions 
                SET segment = TRUE 
                WHERE id = %s
            """
        elif model == 'detect':
            update_query = """
                UPDATE predictions 
                SET detect = TRUE 
                WHERE id = %s
            """
        
        cursor.execute(update_query, (id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Record updated successfully in predictions table")
        
    except (Exception, psycopg2.Error) as error:
        print("Failed to update record in predictions table", error)
        
    finally:
        if connection:
            cursor.close()
            connection.close()