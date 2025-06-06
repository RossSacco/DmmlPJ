from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

class DiabetesFeatureEngineer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        

        
        sedentary_cols = [col for col in ['EXERANY2', '_PACAT1'] if col in X.columns]
        risky_cols = [col for col in ['SMOKE100', 'ALCDAY5'] if col in X.columns]       
            # Calcolo del NutritionScore basato su consumo ponderato di frutta e verdura
        nutri_cols = ['FRUIT1', 'FVBEANS', 'FVGREEN', 'FVORANG', 'VEGETAB1']
        weights = {'FRUIT1': 1, 'FVBEANS': 1.2, 'FVGREEN': 1.5, 'FVORANG': 0.5, 'VEGETAB1': 1.5}

        available_nutri = [col for col in nutri_cols if col in X.columns]
        if all(col in X.columns for col in weights.keys()):
            X['NutritionScore'] = sum(X[col] * weights[col] for col in available_nutri)

        if all(col in X.columns for col in ['EXERANY2', '_PACAT1']):
            X['Sedentary'] = (1 - X['EXERANY2']) + (X['_PACAT1'] == 4).astype(int)
        """
            EXERANY2	_PACAT1	Sedentary
                    1 (sì)	2	0
                    0 (no)	2	1
                    0 (no)	4	2
                    1 (sì)	4	1   
        """

        if 'SMOKE100' in X.columns and 'ALCDAY5' in X.columns:
            X['RiskyBehavior'] = X['SMOKE100'] + (X['ALCDAY5'] >= 3).astype(int)


        if all(col in X.columns for col in ['PERSDOC2', 'MEDCOST']):
            X['LowAccess'] = (1 - X['PERSDOC2']) + X['MEDCOST']


        if '_AGE_G' in X.columns:
            X['AGE_GROUP'] = pd.cut(X['_AGE_G'], bins=[0, 2, 4, 6], labels=['Young', 'Middle', 'Older'])

        
        X.drop(columns=['_AGE_G', 'FRUIT1', 'FVBEANS', 'FVGREEN', 'FVORANG', 'VEGETAB1'], inplace=True, errors='ignore')

        return X