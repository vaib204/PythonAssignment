import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier


def whether():

    border = "-" * 70

    print(border)
    print("Weather Conditions")
    print(border)


    datapath = "MarvellousInfosystems_PlayPredictor (1).csv"

    df = pd.read_csv(datapath)

    print("\nOriginal Columns:")
    print(df.columns.tolist())

    print("\nOriginal Dataset:")
    print(df.head())

    print(border)
    print("Step 2 : Clean, Prepare and Manipulate")
    print(border)

    
    df.columns = df.columns.str.strip()

    
    df["Wether"] = df["Wether"].astype(str).str.strip()
    df["Temperature"] = df["Temperature"].astype(str).str.strip()
    df["Play"] = df["Play"].astype(str).str.strip()

    Weather_encoder = LabelEncoder()
    temperature_encoder = LabelEncoder()
    play_encoder = LabelEncoder()

    # Encode Weather
    df["Wether"] = Weather_encoder.fit_transform(
        df["Wether"]
    )

    # Encode Temperature
    df["Temperature"] = temperature_encoder.fit_transform(
        df["Temperature"]
    )

    # Encode Play
    df["Play"] = play_encoder.fit_transform(
        df["Play"]
    )

    print("\nEncoded Dataset:")
    print(df)

  
    print(border)
    print("Label Encoding")
    print(border)

    print("\nWeather Mapping:")

    for i, value in enumerate(Weather_encoder.classes_):
        print(value, "->", i)

    print("\nTemperature Mapping:")

    for i, value in enumerate(temperature_encoder.classes_):
        print(value, "->", i)

    print("\nPlay Mapping:")

    for i, value in enumerate(play_encoder.classes_):
        print(value, "->", i)

    # ---------------------------------------------------------
    # Step 3 : Independent and Dependent Variables
    # ---------------------------------------------------------

    print(border)
    print("Step 3 : Decide Independent and Dependent Variables")
    print(border)

    
    X = df[["Wether", "Temperature"]]

    # Target
    Y = df["Play"]

    print("\nX:")
    print(X)

    print("\nY:")
    print(Y)

    print("\nShape of X:", X.shape)
    print("Shape of Y:", Y.shape)

    
    print("Number of training features:", X.shape[1])

    # ---------------------------------------------------------
    # Step 4 : Train Model
    # ---------------------------------------------------------

    print(border)
    print("Step 4 : Train the Model")
    print(border)

    model = KNeighborsClassifier(n_neighbors=5)

    print("Model created successfully")

    model.fit(X, Y)

    print("Model trained successfully")

    print("Model expects:",
          model.n_features_in_,
          "features")

    # ---------------------------------------------------------
    # Step 5 : Test Model
    # ---------------------------------------------------------

    print(border)
    print("Step 5 : Test the Model")
    print(border)

    temp_input = input(
        "Enter Temperature (Hot/Mild/Cool): "
    ).strip()

    weather_input = input(
        "Enter Weather (Sunny/Overcast/Rainy): "
    ).strip()

    # ---------------------------------------------------------
    # Encode User Input
    # ---------------------------------------------------------

    weather_encod = Weather_encoder.transform(
        [weather_input]
    )

    temp_encod = temperature_encoder.transform(
        [temp_input]
    )

    print("\nEncoded Weather:", weather_encod[0])
    print("Encoded Temperature:", temp_encod[0])

    # ---------------------------------------------------------
    # Create New Point
    # ---------------------------------------------------------

    new_point = np.array([
        [
            weather_encod[0],
            temp_encod[0]
        ]
    ])

    print("\nNew Point:")
    print(new_point)

    print("New Point Shape:", new_point.shape)

    # Both must be 2
    print("Training Features:", X.shape[1])
    print("Testing Features:", new_point.shape[1])

    # ---------------------------------------------------------
    # Prediction
    # ---------------------------------------------------------

    prediction = model.predict(new_point)

    
    result = play_encoder.inverse_transform(prediction)

    print(border)
    print("Prediction:", result[0])
    print(border)


def main():
    whether()


if __name__ == "__main__":
    main()
