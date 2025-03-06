import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df = pd.DataFrame(players)
    number_of_rows = len(df)
    number_of_columns = len(df.columns)
    return [number_of_rows, number_of_columns]
    
