import os
import pandas as pd
from sklearn.model_selection import train_test_split  # If needed for your features

# Download raw dataset if not exists (uses Kaggle API - install via pip install kaggle first)
if not os.path.exists('data/raw/creditcard.csv'):
    os.makedirs('data/raw', exist_ok=True)
    os.system('kaggle datasets download -d mlg-ulb/creditcardfraud -p data/raw --unzip')

# Optional: Re-create processed features here if someone wants to run from scratch
# df = pd.read_csv('data/raw/creditcard.csv')
# ... your feature engineering code ...
# df.to_parquet('data/processed/creditcard_features.parquet')
print("Raw data ready in data/raw/. Run your notebooks/scripts to generate processed features.")