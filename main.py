import streamlit as st
import pickle
import pandas as pd
import requests


similarity = pickle.load(open('similarity.pkl','rb'))
movies_list=pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=aef162ae02149f6e79d25734469c29da".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



similarity = pickle.load(open('similarity.pkl','rb'))
movies_list=pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters = []

    for i in movies_list1:
        movie_idd = movies.iloc[i[0]].movie_id

        #fetch poster from API

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_idd))

    return recommended_movies,recommended_movies_posters


movies_list=pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)


st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Please enter movie name',movies['title'].values)

if st.button('Recommend'):

    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])



