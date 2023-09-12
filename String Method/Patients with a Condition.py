import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    # Set the conditions whereby the conditions has the word DIAB1
    # /b : word boundary anchor
    #  word boundary assertion that ensures 'DIAB1' is a whole word on its own and not part of another word. 
    # This ensures that we only get patients with Type I Diabetes and not other conditions that might contain 'DIAB1' as part of the word.

    # \b anchors ensure that the pattern 'DIAB1' is matched only when it's a complete word on its own.
    # without the \b anchors, it would match all instances of 'DIAB1' regardless of whether it's part of another word or not.
    # eg: it would match DIAB1st (without \b anchor)
    diabetes_patients_df = patients[patients['conditions'].str.contains(r'\bDIAB1')]

    # Select the columns and rows you wish to display 
    result_df = diabetes_patients_df[['patient_id', 'patient_name', 'conditions']]

    return result_df

## diabetes_patients_df = patients[patients['conditions'].str.match(r'DIAB1$')]
## This pattern ensures that the 'conditions' column ends with 'DIAB1', matching only those exact conditions.

## diabetes_patients_df = patients[patients['conditions'].str.contains(r'\bDIAB1')]
## This pattern will match any occurrence of 'DIAB1' regardless of where it appears in the 'conditions' column, as long as it's a complete word.
## It won't require 'DIAB1' to be at the end of the string.
