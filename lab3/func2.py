movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]


#ex1
def rate(name):
    for movie in movies:
        if movie["name"] == name:
            if movie["imdb"] > 5.5:
                return True
            else:
                return False
            
#ex2
def rate(name):
    high = []
    for movie in movies:
        if movie["imbd"] > 5.5:
            high.append(movie)
    return high

#ex3

def categ(category):
    n = []
    for movie in movies:
        if movie["category"] == category:
            n.append(movie)
    return n
 
#ex4
def average_score():
    sum = 0
    for movie in movies:
        sum += movie["imbd"]
        l = len(movie)
    return sum/l

#ex5
def categ(category):
    sum = 0
    for movie in movies:
        if movie["category"] == category:
            sum += movie["imbd"]
            l = len(movie)
    return sum/l

