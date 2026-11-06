import os
import pandas as pd

def register_and_validate(file_path):
    expected_cols = [
        'CustomerID', 'ProdTaken', 'Age', 'TypeofContact', 'CityTier', 
        'Occupation', 'Gender', 'NumberOfPersonVisiting', 'PreferredPropertyStar', 
        'MaritalStatus', 'NumberOfTrips', 'Passport', 'OwnCar', 
        'NumberOfChildrenVisiting', 'Designation', 'MonthlyIncome',
        'PitchSatisfactionScore', 'ProductPitched', 'NumberOfFollowups', 'DurationOfPitch'
    ]
    if not os.path.exists(file_path):
        print(f"CRITICAL ERROR: Dataset file not found at '{file_path}'.")
        return False
    df = pd.read_csv(file_path)
    print("Dataset Shape Verified:", df.shape)
    return True

if __name__ == "__main__":
    register_and_validate('tourism_project/data/tourism.csv')
