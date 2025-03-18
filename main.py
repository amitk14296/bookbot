
import sys
#from stats import get_num_words
from stats import count_char
from stats import report
from stats import sort_on


#This function will take file path and return contents of the file as string
def get_book_text(path_to_file):
    #open the file hold that file in f
    with open(path_to_file) as f:
        #read the file and store the strings(content) to file_contents
        file_contents = f.read()
    #return the file_contents
    return file_contents



def main():


    unsorted_list=[]
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)#exit with error code if incorrect number of argument are passed

    filepath = sys.argv[1]
    unsorted_list = report(count_char(filepath))

        #List of dictionary
    unsorted_list.sort(key=sort_on, reverse=True)
    for items in unsorted_list:
        for key, value in items.items():
            print(f"{key}: {value}")



main()
