import numpy as np

def create_features(df, window_size=20):

    heights = df["height"].values

    X = []

    for i in range(len(heights) - window_size):

        window = heights[i:i+window_size]

        features = [
            np.mean(window),
            np.std(window),
            np.max(window),
            np.min(window),
            np.gradient(window).mean()
        ]

        X.append(features)

    return np.array(X)