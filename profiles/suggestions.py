from .models import FavoritesProducts, Cluster
from accounts.models import User
from products.models import Product
from django.contrib.auth import get_user_model
from sklearn.cluster import KMeans
from scipy.sparse import dok_matrix, csr_matrix
import numpy as np

def update_clusters():
    #num_favorites = FavoritesProducts.objects.count()
    #update_step = ((num_favorites/100)+1) * 5
    #if num_favorites % update_step == 0: # using some magic numbers here, sorry...
        # Create a sparse matrix from user favorites
        # all_user_names = map(lambda x: x.email, User.objects.only("email"))
    
    all_user = User.objects.all()        
    all_product_ids = set(map(lambda x: x.product.id, FavoritesProducts.objects.only("product")))
    num_users = len(all_user)
    ratings_m = dok_matrix((num_users, max(all_product_ids)+1), dtype=np.float32)
    for i in range(num_users): # each user corresponds to a row, in the order of all_user_names
        user_favorites = FavoritesProducts.objects.filter(user=all_user[i])
        for user_favorite in user_favorites:
            #As long as a user favourites a product, we take it that the rating is 5/5
            ratings_m[i,user_favorite.product.id] = 5

    # Perform kmeans clustering
    k = int(num_users / 10) + 2
    kmeans = KMeans(n_clusters=k)
    clustering = kmeans.fit(ratings_m.tocsr())
    
    # Update clusters
    Cluster.objects.all().delete()
    new_clusters = {i: Cluster(name=i) for i in range(k)}
    for cluster in new_clusters.values(): # clusters need to be saved before refering to users
        cluster.save()
    for i,cluster_label in enumerate(clustering.labels_):
        new_clusters[cluster_label].users.add(all_user[i])