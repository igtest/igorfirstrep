
class Text:
    def __init__(self, filename):
        self.d = {}
        self.filename = filename
        self.wordException = set()
        self.load_exception_set()

    def __len__(self):
        self.get_all_words()
        return len(self.d)

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
                            if len(word) > 1 and word not in self.wordException:
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
        if len(self.d) == 0:
            self.get_all_words()
        sortedList = sorted(self.d.items(), key=lambda x: x[0])
        if keys == 1:
            sortedList.sort(key=lambda x:x[1], reverse=True)
            return sortedList
        if keys == 0:
            sortedList.sort(key=lambda x:x[1])
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
            defaultWords = ['the', 'for', 'of', 'not', 'i', 'to', 'no', 'in']
            for line in defaultWords:
                f.write(line + '\n')
            f.close()

    def get_exception_word_list(self):
        return self.wordException


class TextHtml(Text):
    def get_all_words(self):
        if not self.d:
            word = ""
            temp_tag = ""
            with open(self.filename, encoding="utf8") as f:
                for line in f:
                    workLine = (line.lstrip()).lower()
                    flag = 0
                    for x in workLine:
                        if x == '<':
                            flag = 1
                            continue
                        if x == '>':
                            flag = 0
                            tag = temp_tag
                            continue
                        if flag == 1:
                            temp_tag += x
                            continue
                        if flag == 0 and x.isalpha() and tag != "script":
                            word += x
                        else:
                            if len(word) > 1 and word not in self.wordException:
                                if word not in self.d:
                                    self.d[word] = 1
                                else:
                                    count = self.d[word]
                                    count += 1
                                    self.d[word] = count
                            word = ""
                    temp_tag = ""
        else:
            pass
        return self.d

if __name__ == '__main__':
    words = Text("1.txt")
    wordsFromHTML = TextHtml("new.html")
    # #words.loadExceptionSet()
    print(words.get_all_words())
    print("Количество слов: " + str(len(wordsFromHTML)))
    print(words.get_sorted_list(1))
    print("*************************************")
    print("*************************************")
    print(wordsFromHTML.get_all_words())
    print("*************************************")
    print("*************************************")
    print(wordsFromHTML.get_sorted_list(1))

#
## реализовать количество слов через len(words)
## реализовать множесто исключений с функцией добавления в множество
