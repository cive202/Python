'''
structured and sequential process where raw data passes through mutlipule predefined step to transform it into clean,
consistent, and analaysis-ready data
'''


'''
Common Data Quality:
    Missing Values,

    Duplicated Values,
    Incorrect data types,
    Outliers and noisy data,
    Invalid or corrupted entries,
    Features Scaling and encoding
'''


'''
    Data Ingestion : process of loading raw data from external sources like files, database , csv, pdf ,API into a system.
'''


import pandas as pd
def load_data(file_path):
    content = pd.read_csv(file_path)
    return df


'''
    Data validation : it ensures that the dataset has the required structure before cleaning begins.
        |
        |==> MISSING COLUMNS
         ==>INCORRECT SCHEMA
         ==>PREVENT ERROR
'''


def validate_pipeline(df, required_columns):
    for col in required_columns:
        if col in df.columns:
            raise ValueError(f"Missing required column:{col}")
    return df


''''
    Handling missing Values
        ==> Replace numerical values with meidan/mode
        ==> Replace categorical values with default labels
        ==> Remove records if necessary
'''


def handle_missing_values(df):

    for col in df.select_datatype(include='number').columns:
        df[col].fillna(df[col].median(), inplace=True)

    for col in df.select_datatype(include='category').columns:
        df[col].fillna("Unkown", inplace=True)

    return df


'''
    Removing Duplicate Records:
'''


def remove_duplicates(df):
    df.drop_duplicated(inplace=True)
    return df


'''
    DataType Standardization
'''


def standardize_datatype(df):

    if 'age' in df.columns:
        data['age'] = df['age'].astype(int)

    if 'salary' in df.columns:
        data['salary'] = df['salary'].astype(float)

    return df


'''
    cleaning categorical Data
        ==> It may contain inconsistent values due to
            ==> Spelling Difference
            ==> Capitalization
            ==> abbreviations (like male ->m , female ->f)
'''


def cleaning_categorical_data(df):
    if "gender" in df.columns:
        df["gender"] = df["gender"].str.lower().lower()
        df["gender"] = df["gender"].replace({
            "m": "male",
            "f": "female",
        })
    return df


'''
    handling outliers
'''


def handle_outliers(df, column):
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1

    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    df[column] = df[(df[column] >= lower) and (df[column] <= upper)]
    return df


'''
Feature Selections
        remove unnecessary or irrelevant columns
'''


def select_features(df, selected_columns):
    return [selected_columns]


'''
Feature Transformation
    creates a new columns or modifies one
'''


def create_features(df):
    if "salary" in df.columns:
        def ["salary_log"] = df["salary"].apply(lambda x: if x >= 0 else 0)


'''
FINAL COMPONENT
'''


def cleaning_changng_pipeline(file_path):
    df = load_file(file_path)
    df = validate_pipeline(df, ['age', 'name', 'salary']) '''for coln in colns: if coln not in colns: raise ValueError()   '''
    df = handle_missing_values(df)
    ''' for coln in df.select_datatype(include = "numbers").columns:
            df[coln].fillna(df[coln].median(),inplace = True)
    '''
    df = remove_duplicates(df) ''' df.drop_duplicated(inplace =True)'''
    df = standardize_datatype(df) ''' .astype(int) '''
    df = cleaning_categorical_data() ''' df['gender'].replace({ 'male':'m'}) '''
    df = handle_outliers(df, column)
    df = create_features(df)
    df = select_features(df, ['age', 'salary', 'gender'])

    return df
