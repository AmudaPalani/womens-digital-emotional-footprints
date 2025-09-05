# Women's Mental Health Analysis

A Python-based sentiment analysis project that analyzes social media posts related to women's mental health.

## Features
- Sentiment analysis of tweets related to women's mental health
- Categorization into five universal emotions (Joy, Sadness, Fear, Anger, and Disgust)
- Visual representation of emotion distribution using pie charts
- Sample dataset included

## Setup
1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - Windows: `.\.venv\Scripts\Activate.ps1`
   - Linux/Mac: `source .venv/bin/activate`
4. Install dependencies: `pip install pandas textblob matplotlib`

## Usage
Run the analysis:
```bash
python simple_sentiment_analysis.py
```

This will analyze the sample tweets and generate:
- Detailed emotion analysis for each tweet
- Distribution statistics
- A pie chart visualization (saved as 'emotion_distribution.png')

## Sample Output
The analysis categorizes tweets into emotions and provides:
- Sentiment scores
- Emotion categories
- Distribution statistics
- Visual representation

## Technologies Used
- Python
- pandas
- TextBlob
- matplotlib
