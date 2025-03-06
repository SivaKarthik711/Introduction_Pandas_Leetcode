import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # Filter the animals DataFrame where 'weight' is greater than 100
    result = animals[animals['weight'] > 100].sort_values(by = "weight", ascending = False)[['name']] # Ensuring the result is a DataFrame
    return result
