# Hack_This_Fall_Project
Hack_This_Fall Hackathon was Oraganized from 3rd Feb to 5th Feb, So worked on Local_Zomato_Idea.

#### **Local Zomato targets Local stalls on streets who sells delicious food. Usually People have to stand in queue due to the high demand of dishes available at that stall/dhabas; What if they can just order it, the way people orders on Zomato/Swiggy?**
#### **So, The idea is to Create a Platform for those users and Sellers where they will be able to order it and have to takeaway which eliminates the issue of standing in a queue (of a user) and it benefits the stall seller as well by focusing on the incoming new customers.**

#### **The files uploaded by me are of Recommendation System, that suggests food to the user based on search and ratings by other users.**

#### **Have used Collaborative Based Filtering Recommendation System**

# Datasets: (I have Used Book Dataset and then Modified it to get the Users and Ratings Straight-away)
* At Kaggle -> Data: https://www.kaggle.com/code/jaiminmukeshjariwala/recommendation-system/edit

![image](https://user-images.githubusercontent.com/70468773/217220414-90cb524d-8f39-45d8-9e73-35bf8ee011f1.png)
![image](https://user-images.githubusercontent.com/70468773/217220514-04b42948-5df8-4194-b4b2-e5c6e0bc93be.png)

### **Testing API using Postman**
![image](https://user-images.githubusercontent.com/70468773/217221032-880c7e33-f04e-44da-89af-02f9942de2f7.png)


### **Dependencies Required to be installed...**
* pip instal fastapi uvicorn <br>
* pip install numpy <br>
* pip install pandas <br>
* pip install pickle <br>
* pip install scikit-learn <br>
* pip install joblib <br>

### **Imports that are required...**
* import pandas as pd <br>
* import numpy as np <br>
* from sklearn.metrics.pairwise import cosine_similarity
* import uvicorn
* import pickle
* from fastapi import FastAPI
