import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from Config import *

def encode_labels(df: pd.DataFrame):
    encoders = []
    y_list = Config.TYPE_COLS
    encoded_y_list = Config.ENCODED_COLS

    for i in range(len(y_list)):
        y = df[y_list[i]]

        # Initialize LabelEncoder
        encoder = LabelEncoder()

        # Fit and transform labels
        df[encoded_y_list[i]] = encoder.fit_transform(y)

        encoders.append(encoder)

    return df, encoders

