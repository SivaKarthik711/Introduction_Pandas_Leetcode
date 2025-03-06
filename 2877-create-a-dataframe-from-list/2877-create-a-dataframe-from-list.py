import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    data = {'student_id': [row[0] for row in student_data],
    'age': [row[1] for row in student_data]}
    df = pd.DataFrame(data)
    return df