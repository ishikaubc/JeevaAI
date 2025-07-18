import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class DonorAvailabilityPredictor:
    def __init__(self, csv_path = "data/donors.csv"):
        self.df = pd.read_csv(csv_path)
        self.x = pd.get_dummies(self.df[['region', 'days_since_last', 'willing']], drop_first=True)
        self.y = self.df['availability']
        self.x_columns = self.x.columns  

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            self.x, self.y, test_size=0.2, random_state=42
        )
        self.model = LogisticRegression()
        self.model.fit(self.x_train, self.y_train)

    def predict_availability(self, region: str, days_since_last: int, willing: int) -> str:
        input_dict = {
            "region": [region],
            "days_since_last": [days_since_last],
            "willing": [willing]
        }

        input_df = pd.DataFrame(input_dict)
        input_encoded = pd.get_dummies(input_df, drop_first=True)

        for col in self.x_columns:
            if col not in input_encoded.columns:
                input_encoded[col] = 0


        input_encoded = input_encoded[self.x_columns]
        prediction = self.model.predict(input_encoded)[0]

        return "Available" if prediction == 1 else "Unavailable"

if __name__ == "__main__":
    predictor = DonorAvailabilityPredictor()
    print(predictor.predict_availability("Mumbai", 80, 1))