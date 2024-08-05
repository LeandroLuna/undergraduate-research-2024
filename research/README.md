# Fracture Vision Research

This repository contains the code for the research project "Fracture Vision" developed for undergraduate research at the FIAP. The project aims to develop a computer vision system capable of detecting and segmenting fractures in X-ray images of human bones.

## Model

The pretreined model used in this project (for both tasks) is the [YOLOv8](https://yolov8.com), from "You Only Look Once" (YOLO) family, which is a state-of-the-art computer vision model developed by Ultralytics. 

Training was accelerated using an AWS ml.g4dn.2xlarge instance to expedite the process.

## Dataset 

The dataset used in this project is the "FracAtlas" dataset, which contains 4.083 (1.538 being hands) X-ray images of human bones with fractures. The dataset is divided into 2 classes: `fracture` and `no fracture`. The dataset is available at the following link: [FracAtlas](https://figshare.com/articles/dataset/The_dataset/22363012?file=43283628). 

Paper: [FracAtlas: A Dataset for Fracture Classification, Localization and Segmentation of Musculoskeletal Radiographs](https://www.nature.com/articles/s41597-023-02432-4)

## Technologies

- Python 3: A high-level programming language used for general-purpose programming and scientific computing.
- Pandas: A data manipulation and analysis library for Python, providing data structures and operations for numerical tables and time series.
- Ultralytics: Provides state-of-the-art computer vision models, including YOLO, for object detection and segmentation tasks.
- Scikit-learn: A machine learning library for Python that supports various supervised and unsupervised learning algorithms.
- Venv: A tool for creating isolated Python environments, helping manage dependencies for different projects.
- Jupyter Notebook: An open-source web application that allows you to create and share documents containing live code, equations, visualizations, and narrative text.

## Installation

Create and activate the virtual environment:

```bash
python -m venv venv
source . venv/bin/activate.fish  # On Windows use: venv\Scripts\activate or Linux: source venv/bin/activate
```

## Setup (additional)

Commands that could be useful to setup the environment: 

- sudo apt-get install nvidia-utils-515

- sudo apt-get install -y libgl1-mesa-dev

# - nano "/Users/leandroluna/Library/Application Support/Ultralytics/settings.yaml" # (deixar "dataset", removendo o "s")

- sudo apt-get install unzip

- unzip file.zip

- ipython kernel install --user --name=venv

- pip install -r requirements.txt
