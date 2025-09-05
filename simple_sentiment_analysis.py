import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load sample data
df = pd.read_csv('c:/Users/amudhapalani/OneDrive - Microsoft/Security/repos/hackathon_women_mental_health/data/sample_women_mental_health_tweets.csv')

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def get_emotion_category(text, score):
    # Keywords for each emotion
    emotion_keywords = {
        'Joy': ['grateful', 'hopeful', 'celebrating', 'proud', 'peace', 'happy', 'positive', 'hope', 'glad'],
        'Sadness': ['depression', 'isolating', 'struggling', 'overwhelmed', 'sad', 'lonely', 'crushed'],
        'Fear': ['anxiety', 'stress', 'worried', 'panic', 'fear', 'scared', 'nervous'],
        'Anger': ['toxic', 'pressure', 'triggered', 'frustrated', 'angry', 'mad'],
        'Disgust': ['hate', 'sick', 'disgust', 'awful', 'terrible']
    }
    
    text = text.lower()
    emotion_counts = {emotion: 0 for emotion in emotion_keywords}
    
    # Count keyword matches for each emotion
    for emotion, keywords in emotion_keywords.items():
        for keyword in keywords:
            if keyword in text:
                emotion_counts[emotion] += 1
    
    # If we found emotion keywords, use the most frequent one
    max_count = max(emotion_counts.values())
    if max_count > 0:
        # If there's a tie, use sentiment score to break it
        max_emotions = [e for e, c in emotion_counts.items() if c == max_count]
        if len(max_emotions) == 1:
            return max_emotions[0]
        else:
            # Use sentiment score to break ties
            if score > 0.2:
                return 'Joy' if 'Joy' in max_emotions else max_emotions[0]
            elif score < -0.2:
                return next((e for e in max_emotions if e != 'Joy'), max_emotions[0])
    
    # If no keywords found, use sentiment score
    if score > 0.2:
        return 'Joy'
    elif score < -0.2:
        return 'Sadness'
    else:
        return 'Neutral'  # For truly neutral cases

# Apply sentiment analysis
df['sentiment_score'] = df['tweet'].apply(get_sentiment)
df['emotion'] = df.apply(lambda row: get_emotion_category(row['tweet'], row['sentiment_score']), axis=1)

# Print results with emotions
print("\n=== Emotion Analysis Results ===")
print("\nDetailed Analysis:")
print(df[['tweet', 'sentiment_score', 'emotion']])

# Print summary statistics
print("\n=== Summary Statistics ===")
print(f"\nTotal tweets analyzed: {len(df)}")
emotion_counts = df['emotion'].value_counts()
print("\nEmotion Distribution:")
for emotion, count in emotion_counts.items():
    percentage = (count / len(df)) * 100
    print(f"{emotion}: {count} tweets ({percentage:.1f}%)")

# Print most representative tweet for each emotion
print("\n=== Most Representative Tweets by Emotion ===")
for emotion in sorted(df['emotion'].unique()):
    if emotion != 'Neutral':
        emotion_tweets = df[df['emotion'] == emotion]
        if not emotion_tweets.empty:
            # Get the tweet with the highest absolute sentiment score for this emotion
            max_abs_score_idx = emotion_tweets['sentiment_score'].abs().idxmax()
            representative_tweet = df.loc[max_abs_score_idx]
            print(f"\n{emotion}:")
            print(f"Tweet: {representative_tweet['tweet']}")

# Create a pie chart of emotions
plt.figure(figsize=(10, 8))
emotion_counts = df['emotion'].value_counts()
colors = ['#FFD700', '#4169E1', '#DC143C', '#32CD32', '#800080', '#808080']  # Colors for each emotion
plt.pie(emotion_counts.values, labels=emotion_counts.index, autopct='%1.1f%%', 
        colors=colors, startangle=90)
plt.title('Distribution of Emotions in Women\'s Mental Health Tweets', pad=20)

# Add a legend
plt.legend(emotion_counts.index, title="Emotions", 
          loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Ensure the pie chart is circular
plt.axis('equal')

# Save the plot
plt.savefig('emotion_distribution.png', bbox_inches='tight', dpi=300)
plt.close()

print("\nVisualization has been saved as 'emotion_distribution.png'")
