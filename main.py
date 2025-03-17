
from stats import get_num_words
from stats import count_char
from stats import report
from stats import sort_on
book = "books/frankenstein.txt"
#This function will take file path and return contents of the file as string
def get_book_text(path_to_file):
    #open the file hold that file in f
    with open(path_to_file) as f:
        #read the file and store the strings(content) to file_contents
        file_contents = f.read()
    #return the file_contents
    return file_contents



def main():

    book = "books/frankenstein.txt"
    unsorted_list=[]

        #Printing number of words in a book
    num_words = get_num_words(get_book_text(book))
    print(f"Found {num_words} total words")

        #Calculating occurence of each character in the book
    character = count_char(book)
    print(character)



        #List of dictionary
    unsorted_list = report(character)
    unsorted_list.sort(key=sort_on, reverse=True)
    for items in unsorted_list:
        for key, value in items.items():
            print(f"{key}: {value}")



main()
