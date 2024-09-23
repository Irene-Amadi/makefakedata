##This program is to generate synthetic data to enrich an existing dataset, to be used for the November 2024 Diabetes Hackathon, held by the Data & AI DTE. 
##The original dataset contains 8 featues, and required more features to be added.

# Create featues
columns_headers = [
    'cholesterol_level', 'diabetes_pedigree_function', 'family_diabetes_history', 'diet_type', 
    'star_sign', 'social_media_usage', 'physical_activity_level', 'sleep_duration'
]
# Divide up the features between developers
# dara = 'cholesterol_level, family_diabetes_history, social_media_usage, sleep_duration
# irene = diabetes_pedigree_function, diet_type, physical_activity_level, 

## Create loops for each feature, to: generate 100k rows of randomized data relevant to that feature, with null values randomly distibuted within each feature.

#Diet Type Loop

#import libraries
#import numpy as np
#import pandas as pd
import random as rand
import string 

#create a loop function 
def diet_loop(diet_dict):
    for x in diet_dict:
        print (x)
        break 
#find function to add randomness

#write a dictionary for the     
diet_dict = {'vegan', 'paleo', 'carnivore', 'atkins', 'raw food', 'pescatarian', 'gluten free', 'ketogenic', 'mediterranean', 'vegetarian', 'weight watchers', 'low carb'}

# diet_df =

#Diabetes Pedigree Fucntion loop
# generate 100k randomized dataframe, each value ranging between 
def pedigree_loop(dpf_dict):
    for x in diet_dict:
        print (x)
        break 
pedigree_df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))

#Starsign loop

#Physical activity level loop

#Join dataframes

#Export to Excel - possibly import thhe df, and append in python - or could just export, cut and paste.