import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    number_of_rows = len(players['player_id'])
    number_of_columns = len(players.keys())
    return [number_of_rows, number_of_columns]
    