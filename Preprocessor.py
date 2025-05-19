from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.preprocessing import OrdinalEncoder


binary_cols = ['HLTHPLN1','MEDCOST','TOLDHI2','CVDINFR4',
               'CVDCRHD4','CVDSTRK3','ASTHMA3','CHCSCNCR','CHCOCNCR',
               'CHCCOPD1','HAVARTH3','ADDEPEV2','CHCKIDNY','VETERAN3',
               'INTERNET','QLACTLM2','USEEQUIP','BLIND','DECIDE',
               'DIFFWALK','DIFFDRES','DIFFALON','SMOKE100','EXERANY2','FLUSHOT6',
               'PNEUVAC3', 'HIVTST6', 'PERSDOC2', 'BPHIGH4'] 
nominal_cols = [
    'MARITAL','EMPLOY1','_RACE', '_BMI5CAT'
]

numeric_cols = [
    'PHYSHLTH','MENTHLTH','CHILDREN','NUMADULT_2',
    'ALCDAY5', 'FRUITJU1','NutritionScore',  'STRENGTH'
]

ordinal = {
    'GENHLTH':       [1,2,3,4,5],       # 1=Excellent … 5=Poor
    'CHECKUP1':      [1,2,3,4,5,6,7,8], # 
    'CHOLCHK':       [1,2,3,4],         
    '_AGE_G':        [1,2,3,4,5,6],     # 1=18–24 … 6=65+
    '_PACAT1':       [1,2,3,4],         # 1=High active … 4=Inactive     
    'EDUCA':         [1,2,3,4,5,6],     # 1=Less than high school … 6=Post-grad
    'INCOME2':       [1,2,3,4,5,6,7,8], # 1=Less than $10K … 8=$75K or more 
    '_SMOKER3':      [1,2,3,4],         # 1=Current every day … 4=Never
}


numerical_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

binary_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent'))
])
nominal_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

ordinal_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OrdinalEncoder(
        categories=[ordinal[col] for col in ordinal],
        handle_unknown='use_encoded_value',
        unknown_value=-1
    ))
])


preprocessor = ColumnTransformer(transformers=[
    ('num', numerical_pipeline, numeric_cols),
    ('bin', binary_pipeline, binary_cols),
    ('nom', nominal_pipeline, nominal_cols),
    ('ord', ordinal_pipeline, list(ordinal.keys())),
])
