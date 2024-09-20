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

## Create loops for each feature, to generate 100k rows of randomized data relevant to that feature.

diet_type_dict = {'vegan', 'paleo', 'carnivore', 'atkins', 'raw food', 'pescatarian', 'gluten free', 'ketogenic', 'mediterranean', 'vegetarian', 'weight watchers', 'low carb'}

#Export to Excel