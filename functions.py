from collections import Counter
from datetime import datetime



def parse_user_data(line):
    """
    >>> parse_user_data('John Doe john.doe@example.com')
    ('John', 'Doe', 'john.doe', 'example.com')
    """

    first_name, last_name, email = line.split(' ')
    user, host = email.split('@')
    return first_name, last_name, user, host


def compare_lists(dir_a, dir_b):
    """
    >>> dir_a = ['hello.py', 'readme.txt']
    >>> dir_b = ['readme.txt', 'install.txt', 'hello2.py']
    >>> compare_lists(dir_a, dir_b)
    {'removed': ['hello.py'], 'added': ['hello2.py', 'install.txt']}
    """
    a, b = set(dir_a), set(dir_b)
    return {'removed': sorted(a - b), 'added': sorted([x for x in b if x not in a])}


def print_log(message, process_id, timestamp, level=5):
    """
    >>> from datetime import datetime
    >>> print_log('System started!', 1532, datetime(2019, 1, 2, 10, 30, 55).isoformat(' '))
    2019-01-02 10:30:55 [1532] [INFO] System started!
    """
    if level > 4:
        level = 5
    level2 = {0: 'TRACE', 1: 'DEBUG', 2: 'INFO', 3: 'WARN', 4: 'ERROR', 5: 'None'}
    return print(f' {timestamp} {[process_id]}  {message} {level2[level]}')


def biggest_rectangle(rectangles):
    """
    Find the biggest rectangle in a sequence.
    Rectangles are represented as tuples of (width, height).

    >>> biggest_rectangle([(2, 4), (3, 3), (4, 2)])
    (3, 3)
    """
    return max(rectangles, key=lambda item: item[1]*item[0])


def find_in_file(pattern, filename):
    """
    Find a pattern in file. Print out all lines that match the pattern
    (case-insensitive) with line numbers.

    >>> find_in_file('nevermore', 'raven.txt')
     62 Quoth the Raven, "Nevermore."
     69 With such name as "Nevermore."
     77 Then the bird said, "Nevermore."
     84 Of 'Never- nevermore'."
     92 Meant in croaking "Nevermore."
     99 She shall press, ah, nevermore!
    107 Quoth the Raven, "Nevermore."
    115 Quoth the Raven, "Nevermore."
    123 Quoth the Raven, "Nevermore."
    132 Quoth the Raven, "Nevermore."
    140 Shall be lifted- nevermore!

    max 4 lines
    """

    with open(filename, 'r') as f:
        # lines = Counter([line for line in f if pattern in line.lower()])
        for count, line in enumerate(f):
            if pattern in line.lower():
                count += 1
                print(f'{count-1} {line}')
        f.close()
        return print(f'{count-1} {line}')
        # return print(lines)
        

def read_long_words(filename, min_length):
    """
    >>> words = read_long_words('raven.txt', 5)
    >>> words[:6]
    ['midnight', 'dreary', 'pondered', 'quaint', 'curious', 'volume']
    """

    return [word.strip("r'[.,\"!-]'") for word in (open(filename).read()).split() if len(word) > min_length]


    # with open(filename, 'r') as f:
    #     try:
    #         content = f.read()
    #     finally:
    #         f.close()

    #     # Remove punctuation
    #     no_punct = []
    #     for ch in content:
    #         if ch not in r'[.,"!-]':
    #             no_punct.append(ch)
    #     content = ''.join(no_punct)
    #     result = []
    #     for word in content.split():
    #         if len(word) > min_length:
    #             result.append(word.lower())
    #     return result


def top_words(words, n=10):
    """
    Find top N words in a file. Return a list of tuples (word, count).

    >>> words = read_long_words('raven.txt', 5)
    >>> top_words(words, 5)
    [('chamber', 11), ('nevermore', 10), ('lenore', 8), ('nothing', 7), ('tapping', 5)]
    """

    # word_counts = {}
    # for word in words:
    #     if word in word_counts:
    #         word_counts[word] += 1
    #     else:
    #         word_counts[word] = 1

    # result = []
    # for word, count in word_counts.items():
    #     # Append (count, word) so that we sort by count.
    #     result.append((count, word))

    # result.sort(reverse=True)
    # result = result[:n]
    # return [(count, word) for (word, count) in result]
    words = Counter(words).items()
    return sorted(words, key=lambda item: item[1], reverse=True)[:n]


if __name__ == '__main__':
    words = read_long_words('raven.txt', 5)
    print(top_words(words, n=10))