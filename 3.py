import string
def word_count(file_path):
    count_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                word = word.strip(string.punctuation)
                if word in count_dict:
                    count_dict[word] += 1
                else:
                    count_dict[word] = 1
    return count_dict

file_path = 'P1_data.txt'
word_counts = word_count(file_path)
print(word_counts)
print(word_counts['man'])