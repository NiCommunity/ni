import numpy as np

def jaccard_sim(ratings: np.array, user_vector: np.array) -> np.array:
    """
    Computes jaccard similarities between user (represented by user_vector) and users in ratings matrix
    
    Args:
        ratings: matrix of ratings of shape (# users we want to find distance to) x n_items
        user_vector: user ratings vector
    Returns:
        jaccard_sim_arr: jaccard distances from this user to others 
            (this vector length should equals ratings.shape[0])
    """
    # your code here:
    ...
    
    #Входные данные выглядят к примеру так.
    #Каждая строка - какой-то пользователь.
    #Каждый столбец - номер прослушанного трека. 1 - трек прослушан. 0 - не прослушан

    #ratings = [[1, 0, 1, 0],  # пользователь v1 
              # [0, 1, 1, 0],  # пользователь v2
              # [1, 1, 0, 1]]  # пользователь v3

    #Вектор прослушанных треков нашим юзером. 
    #user_vector = [1, 1, 0, 0]  # пользователь u

    #Пересечение множеств.

    power_per=[] #Список. Мощность (A пересечь B) с длиной равной кол-ву других юзеров.
    
    for i in range(0,ratings.shape[0],1): #Для каждого юзера 
        power_i=0
        for j in range (0,len(user_vector),1): #Для каждого элемента в векторе
            if user_vector[j]==ratings[i, j] and user_vector[j]==1:
                power_i+=1
        power_per.append(power_i)

    #Объединение множеств.

    power_ob=[]

    for i in range(0,ratings.shape[0],1): #Для каждого юзера
        power_i=0
        for j in range (0,len(user_vector),1): #Для каждого элемента в векторе
            if user_vector[j]==1 or ratings[i, j]==1:
                power_i+=1
        power_ob.append(power_i)

    jaccard_sim_arr=[]
    for i in range(0, ratings.shape[0],1):
        if power_ob[i]!=0:
            jaccard_sim_arr.append(power_per[i]/power_ob[i])
        else:
            jaccard_sim_arr.append(0)

    jaccard_sim_arr=np.array(jaccard_sim_arr)

    return jaccard_sim_arr

