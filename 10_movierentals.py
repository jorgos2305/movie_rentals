#!/usr/bin/env python3

import csv
import os

class Movie:
    def __init__(self, id, title, director, sinopsis, duration, genre, rating, avialable):
        self.id       = id
        self.title    = title
        self.director = director
        self.sinopsis = sinopsis
        self.duration = duration
        self.genre    = genre
        self.rating   = rating
        self.avialable = avialable

    def __str__(self):
        if self.avialable == True:
            status = 'In stock'
        else:
            status = 'Currently rented'

        d = int(self.duration)
        hours, minutes = divmod(d, 60)
        duration_in_hrs_min = '{:02d}:{:02d}'.format(hours, minutes)

        movie_information = '''
ID:                  {id}
Title:               {title}
Rating:              {rating}
Duration:            {duration}h
Director:            {director}
Genre:               {genre}
Avialability:        {avialable}
Sinopsis:
{sinopsis}
'''.format(
        id=self.id,
        title=self.title,
        director=self.director,
        sinopsis=self.sinopsis,
        duration=duration_in_hrs_min,
        genre=self.genre,rating=self.rating,
        avialable=status
        )
        return movie_information
#############################################################################################################
def check_if_exist(id):
    with open('emilias_movies.csv', 'r') as csv_file:
        list_of_IDs = list()
        reader = csv.reader(csv_file, delimiter=';')
        for line in reader:
            if line[0] == 'ID':
                continue
            list_of_IDs.append(line[0])
        if id in list_of_IDs:
            return True
        return False


def check_ID(id):
    id_exists = check_if_exist(id)
    correct_start  = id.startswith('m_')
    if len(id) > 4:
        correct_length = True
    else:
        correct_length = False
    try:
        n = int(id[2:])
        if isinstance(n, int):
            includes_numbers = True
    except:
        includes_numbers = False

    if correct_start and correct_length and includes_numbers and not id_exists:
        return True
    return False

def show_all_movies():
    if not file_exists:
        print('You currently do not have any movies in stock.')
        exit()
    else:
        with open('emilias_movies.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                movie = Movie(row['ID'], row['Title'], row['Director'], row['Sinopsis'], row['Duration'],
                row['Genre'], row['Rating'], row['Avialability'])
                print(movie)

def create_movie_entry():
    if not file_exists:
        print('You currently do not have any movies in stock.')
        exit()

    while True:
        id   = input('Enter the ID of the movie. Remember to use the format m_xxx: ')
        id_ok = check_ID(id)
        if not id_ok:
            print('The ID you entered is not valid. Please try again.')
            continue
        else:
            print('ID accepted!')
            break
    title    = input('Enter the name of the movie: ')
    director = input('Enter the director of the movie: ')
    sinopsis = input('What is the movie about? ')
    genre    = input('Enter the genre: ')
    while True:
        try:
            rating   = int(input('Enter the rating from 1 to 10: '))
            if rating < 1 or rating > 10:
                print('Rating not valid')
                continue
            break
        except:
            print('This is not a valid rating. Try again.')
            continue
    while True:
        try:
            duration = int(input('How long does the movie last? Enter the information in minutes: '))
            break
        except:
            print('The value you entered is not in minutes. Try again.')
            continue
    while True:
        in_stock = input('Is the movie in stock (1) or rented (2)? ')
        if in_stock == '1':
            avialable = True
            break
        elif in_stock == '2':
            avialable = False
            break
        else:
            print('Invalid option!')
            continue

    movie = Movie(id, title, director, sinopsis, duration,genre, rating, avialable)
    return movie

def add_movie_to_list_of_movies(movie):
    keys = ['ID', 'Title', 'Director', 'Sinopsis', 'Duration', 'Genre', 'Rating', 'Avialability']
    values = [movie.id, movie.title, movie.director, movie.sinopsis, movie.duration,
    movie.genre, movie.rating, movie.avialable]
    entry = list()
    movie_information = dict(zip(keys, values))
    entry.append(movie_information)
    with open('emilias_movies.csv', 'a') as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=keys)
        if not file_exists:
            writer.writeheader()
        writer.writerows(entry)
    print('Movie entry added for {}'.format(movie.title))

def display_movie_from(selection):
    #Display the selected movie, so that you know what you want to change
    with open('emilias_movies.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            if selection == row['ID']:
                movie = Movie(row['ID'], row['Title'], row['Director'], row['Sinopsis'], row['Duration'],
                row['Genre'], row['Rating'], row['Avialability'])
                print(movie)

def change_information_from(selection):
    #Select the movie through the ID, select the information you wnat to change and enter new information
    valid_information_to_change = ['title', 'director', 'sinopsis', 'duration' , 'genre', 'rating', 'avialability']
    while True:
        information_to_change = input('Which information would you like to change? Enter the field name: ').lower()
        if information_to_change == 'id':
            print('It is not possible to change the ID')
            continue
        if information_to_change not in valid_information_to_change:
            print('This field does not exist.')
            continue
        else:
            new_entry = input('Enter the new {}: '.format(information_to_change.capitalize()))
            break
    #Open the 'data base' and open a temporary 'data base' to make changes there
    #at the end erease the old one and rename the new one
    with open('emilias_movies.csv', 'r') as input_file, open('emilias_movies_temp.csv', 'w') as output_file:
        reader = csv.reader(input_file, delimiter=';')
        writer = csv.writer(output_file, delimiter=';')
        for line in reader:
            if selection == line[0]:
                if information_to_change == 'title':
                    line[1] = new_entry
                    writer.writerow(line)
                if information_to_change == 'director':
                    line[2] = new_entry
                    writer.writerow(line)
                if information_to_change == 'sinopsis':
                    line[3] = new_entry
                    writer.writerow(line)
                if information_to_change == 'duration':
                    line[4] = new_entry
                    writer.writerow(line)
                if information_to_change == 'genre':
                    line[5] = new_entry
                    writer.writerow(line)
                if information_to_change == 'rating':
                    line[6] = new_entry
                    writer.writerow(line)
                if information_to_change == 'avialability':
                    line[7] = new_entry
                    writer.writerow(line)
            else:
                writer.writerow(line)
    os.remove('emilias_movies.csv')
    os.rename('emilias_movies_temp.csv', 'emilias_movies.csv')
    print('{} for movie {} changed.'.format(information_to_change.capitalize(), selection))

def erease_movie(selection):
    with open('emilias_movies.csv', 'r') as input_file, open('emilias_movies_temp.csv', 'w') as output_file:
        reader = csv.reader(input_file, delimiter=';')
        writer = csv.writer(output_file, delimiter=';')
        for line in reader:
            if selection == line[0]:
                continue
            else:
                writer.writerow(line)
    os.remove('emilias_movies.csv')
    os.rename('emilias_movies_temp.csv', 'emilias_movies.csv')
    print('The movie {} has been ereased'.format(selection))

def display_list_of_movies():
    with open('emilias_movies.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            print('{} {}'.format(row['ID'], row['Title']))
#############################################################################################################
#Start of program
while True:
    print('''
     ##############################################
     ########## Emilia's movie rentals ############
     ##############################################

     Menu:
     (1) Show all movies in stock
     (2) Add a new movie to the collection
     (3) Modify the information of a movie
     (4) Erase a movie from the collection
     (5) Exit
    ''')

    valid_options = list(range(1,6))
    while True:
        try:
            option = int(input('What would you like to do? Select an option: '))
        except:
            print('This is not a valid option. Try again')
            continue
        if option not in valid_options:
            print('This is not a valid option. Try again.')
            continue
        else:
            break

    global file_exists
    file_exists = os.path.isfile('emilias_movies.csv')

    if option == 1: #Show all movies in the 'data base'
        show_all_movies()

    if option == 2: #Add movies to the 'data base'
        movie = create_movie_entry()
        add_movie_to_list_of_movies(movie)

    if option == 3: #get the values that have to be changed, after selecting a movie
        display_list_of_movies()
        while True:
            selection = input('Which movie would you like to change? Enter the ID: ')
            id_ok = check_if_exist(selection)
            if not id_ok:
                print('Invalid selection. Try again.')
                continue
            else:
                break
        display_movie_from(selection)
        change_information_from(selection)

    if option == 4: #erease an entry, by selecting the ID
        display_list_of_movies()
        while True:
            selection = input('Which movie would you like to change? Enter the ID: ')
            id_ok = check_if_exist(selection)
            if not id_ok:
                print('Invalid selection. Try again.')
                continue
            else:
                break
        display_movie_from(selection)
        erease_movie(selection)

    if option == 5:
        print('Good bye!')
        break

    while True:
        question = input('Would you like to continue? (y/n) ').lower()
        if question == 'y':
            break
        elif question == 'n':
            print('Good bye!')
            exit()
        else:
            print('Please enter only y or n')
            continue
    os.system('clear')
    continue #Keep the program running
