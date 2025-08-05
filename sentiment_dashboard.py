import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings("ignore")

# Load data
df = pd.read_csv("sentimentanalysis.csv")

# Clean column names
df.rename(columns={
    'Graduate Count=IF(C2="Graduate",COUNTIF($C$2:C2,"Graduate"),"")': 'Graduate_Count',
    'Undergraduate Count   ': 'Undergraduate_Count'
}, inplace=True)

# Create status column
df['Status'] = df['Graduate_Count'].apply(lambda x: 'Graduate' if pd.notnull(x) else 'Undergraduate')

# Convert Dates to datetime

df['Dates'] = pd.to_datetime(df['Dates'], errors='coerce')

# Sentiment color palette
sentiment_palette = {
    "Very Positive": "#1f77b4",
    "Positive": "#2ca02c",
    "Neutral": "#ff7f0e",
    "Negative": "#d62728",
    "Very Negative": "#9467bd"
}

#Clean 'Major' values and group infrequent ones as "Other"
df['Major'] = df['Major'].astype(str).str.strip()
major_counts = df['Major'].value_counts()
major_threshold = 5
df['Major_Cleaned'] = df['Major'].apply(lambda x: x if major_counts.get(x, 0) >= major_threshold else 'Other')

# Set up subplots
fig, axs = plt.subplots(3, 2, figsize=(18, 16))
fig.suptitle('📊 Sentiment Analysis Dashboard', fontsize=18, fontweight='bold')

# Plot 1: Overall Sentiment
sns.countplot(data=df, x='Sentiment', palette=sentiment_palette, ax=axs[0, 0])
axs[0, 0].set_title("Overall Sentiment")
axs[0, 0].set_ylabel("Count")
axs[0, 0].set_xlabel("Sentiment")
axs[0, 0].legend_.remove() if axs[0, 0].legend_ else None

# Plot 2: Sentiment by Gender 
gender_data = df.groupby(['Gender', 'Sentiment']).size().unstack().fillna(0)
gender_data.plot(kind='bar', stacked=True, ax=axs[0, 1], width=0.8,
                 color=[sentiment_palette.get(s, "#999999") for s in gender_data.columns],
                 legend=False)
axs[0, 1].set_title("Sentiment by Gender")
axs[0, 1].set_ylabel("Count")
axs[0, 1].set_xlabel("Gender")
axs[0, 1].set_xticklabels(axs[0, 1].get_xticklabels(), rotation=0)  

#  Plot 3: Sentiment by Age 
age_data = df.groupby(['Age', 'Sentiment']).size().unstack().fillna(0)
age_data.plot(kind='bar', stacked=True, ax=axs[1, 0],
              color=[sentiment_palette.get(s, "#999999") for s in age_data.columns],
              legend=False)
axs[1, 0].set_title("Sentiment by Age")
axs[1, 0].set_ylabel("Count")
axs[1, 0].set_xlabel("Age")

# Plot 4: Sentiment by Major
major_data = df.groupby(['Major_Cleaned', 'Sentiment']).size().unstack().fillna(0)
major_data.plot(kind='bar', stacked=True, ax=axs[1, 1], width=0.8,
                color=[sentiment_palette.get(s, "#999999") for s in major_data.columns],
                legend=False)
axs[1, 1].set_title("Sentiment by Major")
axs[1, 1].set_ylabel("Count")
axs[1, 1].set_xlabel("Major") 

# Plot 5: Sentiment by Country 
country_data = df.groupby(['Country', 'Sentiment']).size().unstack().fillna(0)
country_data.plot(kind='bar', stacked=True, ax=axs[2, 0],
                  color=[sentiment_palette.get(s, "#999999") for s in country_data.columns],
                  legend=False)
axs[2, 0].set_title("Sentiment by Country")
axs[2, 0].set_ylabel("Count")
axs[2, 0].set_xlabel("Country")

#  Plot 6: Sentiment Over Time 
time_data = df.groupby([df['Dates'].dt.date, 'Sentiment']).size().unstack().fillna(0)
time_data.plot(ax=axs[2, 1],
               color=[sentiment_palette.get(s, "#999999") for s in time_data.columns],
               legend=False)
axs[2, 1].set_title("Sentiment Over Time")
axs[2, 1].set_ylabel("Count")
axs[2, 1].set_xlabel("Date")

# Unified Legend (top left)
legend_patches = [
    mpatches.Patch(color=color, label=label)
    for label, color in sentiment_palette.items()
]
fig.legend(
    handles=legend_patches,
    loc='upper left',
    bbox_to_anchor=(0.01, 0.98),
    title="Sentiment",
    fontsize=12
)

# Final layout adjustments
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()