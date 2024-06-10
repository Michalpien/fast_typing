from random import choice
import os


class EmptyFileError(Exception):
    def __init__(self, file) -> None:
        super().__init__(f'File {file}')


class TextGetter:
    '''
    class TextGetter
    '''
    def __init__(self) -> None:
        pass

    def random_file(Self):
        '''
        draw random file from folder 'teksty'
        '''
        list_of_files = os.listdir('teksty')
        file = choice(list_of_files,)
        return file

    def get_words(self):
        '''
        draw a random file from "teksty" and return list of words in it
        '''
        random_file = self.random_file()
        with open(f'./teksty/{random_file}', 'r') as text:
            sentence = ""
            for line in text:
                sentence += line
            words = sentence.split(" ")
        if not words:
            raise EmptyFileError(random_file)
        else:
            return list(words)

    def get_lines(self):
        ''''
        Returns list of lines from random file of length about 60 characters
        '''
        text = []
        counter = 0
        words = self.get_words()
        for word in words:
            if len(text) == 0:
                text.append(word + ' ')
            elif len(text[counter]) < 60:
                text[counter] += word + ' '
            else:
                text[counter] = text[counter][:-1]
                text.append(word + ' ')
                counter += 1
        return text


class Statistics:
    '''
    class Statistics. Contains attributes:
    :param time: entering text time in seconds
    :type time: int

    :param entered_text: text entered by user
    :type entered_text: list

    :param text: text to compare
    :type text: list

    '''
    def __init__(self, time=None, entered_text=None, text=None) -> None:
        if not entered_text:
            self._entered_text = []
        else:
            self._entered_text = entered_text
        if not text:
            self._text = []
        else:
            self._text = text
        if not time:
            self._time = 1
        else:
            self._time = time

    def mistakes(self):
        '''
        Returns number of differences, comparing entered_text to text
        If one is shorter, compare only to the end of this one
        '''
        compared = list(zip(self._entered_text, self._text))
        mistakes = 0
        for pair in compared:
            tekst_chars = [char for char in pair[1]]
            inscribed_chars = [char for char in pair[0]]
            chars_pairs = list(zip(tekst_chars, inscribed_chars))
            for char_pair in chars_pairs:
                if char_pair[0] != char_pair[1]:
                    mistakes += 1
        return mistakes

    def chars_per_minute(self):
        '''
        Returns number of valid characters entered per minute
        time entered in seconds
        '''
        chars = 0
        for line in self._entered_text:
            chars += len(line)
        chars_per_minute = (chars - self.mistakes()) / (float(self._time) / 60)
        return chars_per_minute

    def words_per_minute(self):
        '''
        Returns number of words entered per minute
        '''
        counter = 0
        for line in self._entered_text:
            words = line.split(' ')
            counter += len(words)
        words_per_minute = counter / (float(self._time) / 60)
        return words_per_minute
