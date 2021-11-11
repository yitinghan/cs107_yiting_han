# Group: Diwei Zhang, Yiting Han

class Sentence: # An iterable
    def __init__(self, text): 
        self.text = text
        self.words = text.split()

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for i in self.words:
            yield i

def main():
    s = Sentence('This is a sentence.')
    for word in s:
        print(word)

if __name__ == '__main__':
    main()