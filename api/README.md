# Fracture Vision API

This is the API for the Fracture Vision project. It is a RESTful API that allows users to interact with the Fracture Vision database, which includes functionalities for object detection, segmentation, and managing prediction data.

## Technologies

- **psycopg2**: Python library for interacting with PostgreSQL databases, allowing efficient query execution and connection management.

- **boto3**: AWS SDK for Python, used to interact with Amazon Web Services, such as S3 for file storage.

- **PIL (Pillow)**: Python Imaging Library for opening, manipulating, and saving images in various formats.

- **numpy**: Library for numerical computing in Python, providing support for arrays and advanced mathematical functions, used for image data processing.

- **fastapi**: Modern framework for building web APIs in Python, known for its high performance and ease of use, used to create the project's API.

- **pydantic**: Library for data validation and settings management in Python, used to define and validate data models in the API.

- **ultralytics**: Machine learning library that includes implementations for object detection and segmentation models, such as YOLO, used for image processing and analysis.

- **s3**: AWS cloud storage service, used for storing and managing files like images and model results.

- **rds**: AWS relational database service, used for reliable and scalable database management and storage.

- **venv**: Tool for creating virtual environments in Python, isolating project-specific dependencies and packages to avoid conflicts between different projects.

---

## Installation

To set up the Fracture Vision API, follow these steps:

### Prerequisites

- Python 3 or later
- RDS database using PostgreSQL engine
- AWS account for S3

### Clone the repository

```bash
git clone https://github.com/LeandroLuna/undergraduate-research-2024
cd undergraduate-research-2024/api
```

### Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the root of the project and add the following environment variables:

```env
AWS_RDS_USER=your_db_user
AWS_RDS_PASSWORD=your_db_password
```

And change the following variables in the `utils/constants.py` file:

```python
AWS_S3_BUCKET_NAME = 'your_bucket_name'
AWS_RDS_ENDPOINT = 'your_db_endpoint'
AWS_RDS_DATABASE = 'your_db_name'
```

### Set up the database

Run the necessary SQL commands to set up your database. Use the following SQL commands to create the tables:

```sql
-- Create predictions table
CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    detect BOOLEAN DEFAULT FALSE,
    segment BOOLEAN DEFAULT FALSE,
    img_url TEXT
);

-- Create segment table
CREATE TABLE segment (
    id SERIAL PRIMARY KEY,
    prediction_id INTEGER REFERENCES predictions(id),
    fractured BOOLEAN,
    img_file_path TEXT,
    img_labels_file_path TEXT,
    object JSONB
);

-- Create detect table
CREATE TABLE detect (
    id SERIAL PRIMARY KEY,
    prediction_id INTEGER REFERENCES predictions(id),
    fractured BOOLEAN,
    img_file_path TEXT,
    img_labels_file_path TEXT,
    object JSONB
);
```

### Start the API Server

```bash
uvicorn main:app --reload
```

Navigate to `http://localhost:8000` in your browser.

## Endpoints

To view the available endpoints, navigate to `http://localhost:8000/docs` in your browser.