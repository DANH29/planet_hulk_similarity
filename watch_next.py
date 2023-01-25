# program that uses Spacy to compare movie descriptions and find the 2 most similar

import spacy

nlp = spacy.load('en_core_web_md')

def watch_next():
    # variables to store highest similarity movie value and movie name
    most_similar = 0
    next_movie = ""

    # loop through each line in movies.txt
    # strip movie into just the description
    # compare similarity with planet hulk description

    for movie in movies:
        similarity = nlp(movie[9:]).similarity(planet_hulk)

        # if movie similarity is greater than most_similar
        # most_similar changes to movie similarity
        # store movie name as next_movie

        if similarity > most_similar:
            most_similar = similarity
            next_movie = movie[:7]

    # print next movie to watch

    print(f"The next recommended movie to watch is: {next_movie}")


# read in movies.txt and split into lines
movies_txt = open("movies.txt", "r")
movies = movies_txt.read().splitlines()

# variable to store planet hulk description using nlp()

planet_hulk = nlp("Will he save their world or destroy it?"
                  "When the Hulk becomes too dangerous for the Earth, "
                  "the Illuminati trick hulk into a shuttle and launch him into space "
                  "to a planet where the Hulk can live in peace. "
                  "Unfortunately, Hulk lands on the planet Sakaar where he is sold "
                  "into slavery and trained as a gladiator.")

# call watch_next function
watch_next()
