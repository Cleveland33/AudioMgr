# imports 
from os import error
from display import print_menu , print_header , clear
from album import Album
from song import Song
import pickle

# globals
catalog = []
album_count = 0
song_count = 1
#declare a catalog variable (list)

# functions

def serialize_data():
    try:
        writer = open('songMngr.data', 'wb')  # wb = write binary
        pickle.dump(catalog, writer)
        writer.close()
        print("** Data serialized!")
    except:
        print("** Error, data not saved")

def deserialize_data():
    global album_count

    try:
        reader = open('songMngr.data', 'rb')  # rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        for prod in temp_list:
            catalog.append(prod)

        # get the last used id, and increase by 1
        last = catalog[-1]
        album_count = last.id + 1

        how_many = len(catalog)
        print("** Read: " + str(how_many) + " albums")

    except:
        print("** Error, no data file found")


def register_album():
    global album_count
    print_header("Register new Album") 
    
    # title, genre, artist, release_year, price, album_art, related_artist, record_label
    try:
        title = input("Please provide Title: ")
        genre = input("Please provide Genre: ")
        artist = input("Please provide Artist Name: ")
        release_year = int(input("Please provide Release Year: "))
        price = float(input("Please provide Price: $"))
        album_art = input("Please provide Album Art URL: ")
        related_artist = input("Please provide Related Artist: ")
        record_label = input("Please provide Record Label: ")

        album_count += 1

        album = Album(album_count, title, genre, artist, release_year, price, album_art, related_artist, record_label)

        # push the album into the list 
        catalog.append(album)
        print("*** Album created! ***")
    
    except ValueError:
        print("** Error: Invalid Number. Try Again!**")

    except:
        print("**Unexpected Error. Try again at a Later Time!**")


def print_albums():

    print_header("Your current albums")
    for album in catalog:
        print(f"{album.id} | {album.title} | {album.release_year}")
    

def register_song():
    global song_count

    #let the user choose an album

    print_albums()
    album_id = int(input("Please choose the album Id: "))

    #find the album with that id  
    found = False
    for album in catalog:
        if(album.id == album_id):
            found = True 
            the_album = album
            # print the song of album

    if(not found):
        print("** Error: Wrong Id. Try Again")
        return

    #create the song 
    print_header("Register a new Song")    
    title = input("Please provide Title: ")
    featured_artist = input("Please provide Featured Artist: ")
    length_of_track = input("Please provide Track Length: ")
    written_by = input("List name of Song Writer: ")

    song_count += 1 

    song = Song(song_count,title, featured_artist, length_of_track, written_by)


    #push the song the album list 
    the_album.add_song(song)

    print("** Song Register **")

def display_album_songs():
    display_albums() 

    album_id = input ("Please choose an ID: ")

    found = False
    for album in catalog:
        if(album.id == album_id):
            found = True

            #print album songs
            for song in album.songs:
                print(song.title)

    if(not found):
        print(" Error: Invalid album ID")
def count_songs():
    print_header("Your total number of songs")

    total = 0
    for albums in catalog:
        songs_catalog = len(albums.songs)
        total += songs_catalog
    
    print(f"There are: {total} songs in the system")

def print_song():
    print_header("Your current songs")
    
# instructions

deserialize_data()
input("Press Enter to continue...")



opc = ''
while(opc != 'q' and opc != 'x'):
    clear()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == "1"):
        register_album()
        serialize_data()

    elif(opc == "2"):
        register_song()
        serialize_data()

    elif (opc == '3'):
        print_albums() 

    elif (opc == '4'):
        print_song()    
    
    elif (opc == '5'):
        input(" Press Enter to continue...")
