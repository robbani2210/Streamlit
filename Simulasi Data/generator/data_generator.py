import pandas as pd
import numpy as np

def generate_data(n_points=1000):
    # Timestamp
    date_rng = pd.date_range(end=pd.Timestamp.today(), periods=n_points, freq="H")

    # Lokasi 1
    arus1 = np.random.normal(loc=10, scale=2, size=n_points)
    volt1 = np.random.normal(loc=220, scale=5, size=n_points)

    # Lokasi 2
    arus2 = np.random.normal(loc=12, scale=2.5, size=n_points)
    volt2 = np.random.normal(loc=225, scale=4, size=n_points)

    df = pd.DataFrame({
        "timestamp": date_rng,
        "arus_lokasi1": arus1,
        "volt_lokasi1": volt1,
        "arus_lokasi2": arus2,
        "volt_lokasi2": volt2,
    })

    return df
