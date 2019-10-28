from urllib.request import urlopen


def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_words(story_words):
    for word in story_words:
        print(word)


def main():
    words = fetch_words()
    print_words(words)

# this will print the module name as "word_list" when it is imported
# ex: by import statement in REPL only in the first import
print(__name__)

# when this module is executed from the command line __name__ will print __main__
# instead of the module name


# looks like __name__ is there for every module, but I had to quote __main__
if __name__ == '__main__':
    main()

# so using the __name__ value is a method to determine if the module is executed form the
# command line or not


