from flask import Flask,jsonify,request
import csv
all_movies=[]

with open('movies.csv',encoding='utf-8') as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

liked_movies=[]
not_liked_movies=[]
did_not_watch=[]

app=Flask(__name__)
@app.route('/get-movie')
def get_movie():
    return jsonify({
        'data':all_movies[0],
        'status':'Success'
    })

@app.route('/liked-movie',methods=['POST'])
def liked_movie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        'status':"Success"
    }),201

@app.route('/did_not_watch',methods=['POST'])
def did_not_watch():
    global all_movies
    movie=all_movies[0]
    all_movies=all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        'status':"Success"
    }),201

@app.route('/not_liked_movie',methods=['POST'])
def not_liked_movie():
    global all_movies
    movie=all_movies[0]
    all_movies=all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        'status':"Success"
    }),201  

if __name__=='__main__':
    app.run()
