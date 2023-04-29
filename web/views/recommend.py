import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from django.shortcuts import render


def index(request):
    # Load data
    ratings_df = pd.read_csv('ratings.csv')
    products_df = pd.read_csv('product.csv')

    # Data cleaning and preprocessing
    ratings_df.drop_duplicates(inplace=True)
    products_df.drop_duplicates(inplace=True)
    ratings_pivot = ratings_df.pivot_table(index='user_id', columns='product_id', values='rating')
    ratings_pivot.fillna(0, inplace=True)

    # Train collaborative filtering algorithm
    cosine_sim = cosine_similarity(ratings_pivot.T)

    # Function to generate recommendations
    def get_recommendations(product_name):
        product_id = products_df[products_df['product_name'] == product_name]['product_id'].values[0]
        sim_scores = list(enumerate(cosine_sim[product_id]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        product_indices = [i[0] for i in sim_scores]
        recommendations = products_df.iloc[product_indices]['product_name'].values.tolist()
        return recommendations

    # Render HTML file with recommendations
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        recommendations = get_recommendations(product_name)
        return render(request, 'web/recommend.html',
                      {'product_name': product_name, 'recommendations': recommendations})
    else:
        return render(request, 'web/index.html')
