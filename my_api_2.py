import uvicorn

import pickle

import numpy as np
import pandas as pd

from fastapi import FastAPI

from flask import jsonify

new_pt = pickle.load(open('new_pt.pkl', 'rb'))
new_similarity_scores = pickle.load(open('new_similarity_scores', 'rb'))
food_dataset = pickle.load(open('food_dataset.pkl', 'rb'))

app = FastAPI()

@app.get('/home/{food_name}')
def recommend(food_name):
# fetching the index of so and so food
    index = np.where(new_pt.index==food_name)[0][0]
    similar_items = sorted(list(enumerate(new_similarity_scores[index])), key = lambda x : x[1], reverse=True)[1:6]
    
    data = []
    for i in similar_items:
        item = []
        # print(food_dataset[food_dataset['food_names'] == new_pt.index[i[0]]].values[0][0])
        temp_df = food_dataset[food_dataset['food_names'] == new_pt.index[i[0]]]
        item.extend(list(temp_df['food_names'].values))
        item.extend(list(temp_df['food_images'].values))
        data.append(item)
    
    return {'recommendation':data}
  
# run api with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1', port = 8000)