# YOLOv7 Training Script for Sentiment Analysis Dataset

import torch
import os

# Training configuration
config = {
    'weights': 'yolov7.pt',  # Pre-trained weights
    'cfg': 'cfg/training/yolov7.yaml',
    'data': 'dataset.yaml',  # Our dataset config
    'epochs': 100,
    'batch_size': 16,
    'img_size': [640, 640],
    'device': '0',  # GPU device
    'workers': 8,
    'project': 'runs/train',
    'name': 'sentiment_detection'
}

# Command to run training
training_command = f"""
python train.py \
    --weights {config['weights']} \
    --cfg {config['cfg']} \
    --data {config['data']} \
    --epochs {config['epochs']} \
    --batch-size {config['batch_size']} \
    --img-size {config['img_size'][0]} {config['img_size'][1]} \
    --device {config['device']} \
    --workers {config['workers']} \
    --project {config['project']} \
    --name {config['name']}
"""

print("YOLOv7 Training Command:")
print(training_command)
