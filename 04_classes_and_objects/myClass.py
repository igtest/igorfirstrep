class Text:
    def __init__(self, filename):
        self.d = {}
        self.filename = filename
        self.wordException = set()

    def get_all_words(self):
        self.load_exception_set()
        if not self.d:
            word = ""
            with open(self.filename, encoding="utf8") as f:
                for line in f:
                    workLine = line.lower()
                    for x in workLine:
                        if x.isalpha():
                            word += x
                        else:
                            if len(word) >= 1 and word not in self.wordException:
                                if word not in self.d:
                                    self.d[word] = 1
                                else:
                                    count = self.d[word]
                                    count += 1
                                    self.d[word] = count
                            word = ""
                            continue
        else:
            pass
        return self.d

    def get_sorted_list(self, keys):
        self.get_all_words()
        sortedList = sorted(self.d.items(), key=lambda x: x[keys])
        if keys == 1:
            return sortedList[::-1]
        if keys == 0:
            return sortedList

    def get_most_popular_word(self):
        sortedList = self.get_sorted_list(1)
        return sortedList[:1]

    def set_new_exception_word(self, newWord):
        f = open("ListExceptionWords.txt", 'a')
        f.write(newWord + '\n')
        f.close()

    def load_exception_set(self):
        try:
            with open("ListExceptionWords.txt") as f:
                for line in f:
                    self.wordException.add(line[:-1])
        except IOError:
            f = open("ListExceptionWords.txt", 'w')
            defaultWords = ['the', 'for', 'of', 'not', 'i', 't', 'to', 'no', 'in']
            for line in defaultWords:
                f.write(line + '\n')
            f.close()

    def ge_exception_word_list(self):
        return self.wordException


class TextHtml(Text):
    def get_all_words(self):
        if not self.d:
            word = ""
            with open(self.filename, encoding="utf8") as f:
                for line in f:
                    workLine = (line.lstrip()).lower()
                    print(workLine)
                    flag = 0
                    for x in workLine:
                        if x == '<':
                            flag = 1
                            continue
                        if x == '<':
                            flag = 0
                            continue
                        if flag == 1:
                            continue
                        if flag == 0 and x.isalpha():
                            word += x
                        else:
                            if len(word) >= 3:
                                if word not in self.d:
                                    self.d[word] = 1
                                else:
                                    count = self.d[word]
                                    count += 1
                                    self.d[word] = count
                            word = ""
                            continue
        else:
            pass
        return self.d


words = Text("1.txt")
wordsFromHTML = TextHtml("new.html")
# #words.loadExceptionSet()
##print(words.getExceptionWordList())
print(words.get_all_words())
##print(words.getSortedList(1))
##print(wordsFromHTML.getAllWords())

## реализовать количество слов через len(words)
## реализовать множесто исключений с функцией добавления в множество
