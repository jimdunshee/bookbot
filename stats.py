def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_char_counts(dict):
    sorted = []
    for k,v in dict.items():
        sorted.append({"char": k, "count": v})
    def sort_on(dict):
        return dict["count"]
    sorted.sort(reverse=True, key=sort_on)
    return sorted
