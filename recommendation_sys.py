import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
import numpy as np


neurosky_dataset = pd.read_csv('neurosky-dataset.csv')

# Define aggregation functions
agg_funcs = {
    'Delta': ['mean'],
    'Theta': ['mean'],
    'Alpha1': ['mean'],
    'Alpha2': ['mean'],
    'Beta1': ['mean'],
    'Beta2': ['mean'],
    'Gamma1': ['mean'],
    'Gamma2': ['mean'],
    'Attention': ['mean'],
    'Meditation': ['mean'],
    'Mental Effort': ['mean'],
    'Task Familiarity': ['mean'],
    'Blink Strength': ['mean']
}


aggregated_df = neurosky_dataset.groupby('movie_id').agg(agg_funcs).reset_index()


# Step 1: Load and merge the datasets
movie_dataset = pd.read_csv('movie_dataset.csv')

merged_dataset = pd.merge(movie_dataset, aggregated_df, on='movie_id')

# Step 3: Perform high-level feature extraction (TF-IDF)


# Specify the columns for different types of features
text_columns = ['overview']
categorical_columns = ['genre', 'title','popularity','release_date']
numerical_columns = [('Delta', 'mean'), ('Theta', 'mean'), ('Alpha1', 'mean'), ('Alpha2', 'mean'),
                     ('Beta1', 'mean'), ('Beta2', 'mean'), ('Gamma1', 'mean'), ('Gamma2', 'mean'),
                     ('Attention', 'mean'), ('Meditation', 'mean'), ('Mental Effort', 'mean'),
                     ('Task Familiarity', 'mean'), ('Blink Strength', 'mean')]

# numerical_features = merged_dataset[numerical_columns].values
numerical_features = (numerical_features - numerical_features.mean()) / numerical_features.std()  # Normalize


# Perform TF-IDF feature extraction on text columns
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrices = {}
for column in text_columns:
    tfidf_matrix = tfidf_vectorizer.fit_transform(merged_dataset[column])
    tfidf_matrices[column] = tfidf_matrix.toarray()


# Continue with your model training, evaluation, and recommendation code



# Preprocess numerical columns (e.g., normalization)

# numerical_features = merged_dataset[numerical_columns].values
numerical_features = (numerical_features - numerical_features.mean()) / numerical_features.std()  # Normalize

# Preprocess categorical columns (e.g., one-hot encoding)
categorical_features = pd.get_dummies(merged_dataset[categorical_columns])

# Combine all feature matrices
X = np.concatenate([tfidf_matrices[column] for column in text_columns], axis=1)
X = np.concatenate([X, numerical_features, categorical_features], axis=1)

# Target variable
y = merged_dataset['popularity']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   



# Step 5: Train the recommendation models
models = {
    'KNN': KNeighborsRegressor(),
    'Random Forest': RandomForestRegressor(),
    'Gradient Boosting': GradientBoostingRegressor(),
    'SVM': SVR(),
    'Neural Network': MLPRegressor()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    
    
    
# Step 6: Evaluate the models and select the best-performing one (using R-squared as an example)
model_scores = {name: model.score(X_test, y_test) for name, model in models.items()}
best_model = max(model_scores, key=model_scores.get)

print("Model R-squared Scores:")
print(model_scores)
print(f"Best-performing model: {best_model}")    