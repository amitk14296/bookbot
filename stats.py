
def get_num_words(file_contents):
    words = file_contents.split()
    count = len(words)

    return count

#Count number of time each character appear in the book
def count_char(path_to_file):
    count_dict = dict()
    with open(path_to_file) as f:
        temp = f.read()
        file_contents = temp.lower()

        for i in file_contents:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1

    return count_dict



def report(count_dict):
    unsorted_list = []
    for key, value in count_dict.items():
        if key.isalpha() == True:
            temp_dict = {key: value}
            unsorted_list.append(temp_dict)

    return unsorted_list

def sort_on(item):
    return list(item.values())[0]
    # sorting_values=[]
    # for i in unordered_list:
    #     for j in i:
    #         #print(i[j])
    #         sorting_values.append(i[j])
    # return sorting_values
