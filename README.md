# Sentiment Analysis Dataset for YOLOv7

Generated on: 2025-05-29 19:23:00

## Dataset Overview
- **Source**: Amazon Automotive Reviews
- **Total Samples**: 9,206
- **Classes**: 3 (positive, neutral, negative)
- **Image Size**: 640x640

## Sentiment Distribution
- Positive: 6,223 samples
- Negative: 1,579 samples
- Neutral: 1,404 samples

## Files Structure
```
yolo_sentiment_output/
├── images/                     # Synthetic images
├── labels/                     # YOLOv7 format labels
├── annotations/               # JSON annotations
├── dataset.yaml              # YOLOv7 dataset config
├── classes.names             # Class names
├── processed_reviews.csv     # Processed review data
├── summary_stats.json        # Summary statistics
└── sentiment_analysis_report.png
```

## Usage with YOLOv7
1. Update the `path` in `dataset.yaml` to your local directory
2. Use this dataset for training: `python train.py --data dataset.yaml`

## Performance Metrics
- Average Confidence: 0.806
- Model Used: cardiffnlp/twitter-roberta-base-sentiment-latest
- Processing Device: cpu
