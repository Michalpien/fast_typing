from fast_typing.text_meneger import TextGetter, Statistics


def test_create_TextGetter():
    _ = TextGetter()


def test_get_random_file(monkeypatch):
    def return_tekst08(_):
        return 'tekst08.txt'
    monkeypatch.setattr('fast_typing.text_meneger.TextGetter.random_file', return_tekst08)
    file = TextGetter().random_file()
    assert file == 'tekst08.txt'


def test_get_words(monkeypatch):
    def return_tekst03(_):
        return 'tekst03.txt'
    monkeypatch.setattr('fast_typing.text_meneger.TextGetter.random_file', return_tekst03)
    words = TextGetter().get_words()
    assert words[0] == 'Minął'
    assert words[3] == 'samochód'


def test_get_lines(monkeypatch):
    def return_tekst08(_):
        return 'tekst08.txt'
    monkeypatch.setattr('fast_typing.text_meneger.TextGetter.random_file', return_tekst08)
    text = TextGetter().get_lines()
    assert text[0].split()[0] == 'Jestem'


def test_create_Statistics():
    entered_text = ['Marek', 'Stanisław']
    text = ['Marek', 'Agata']
    time = 10
    statistics = Statistics(time, entered_text, text)
    assert statistics._text == ['Marek', 'Agata']


def test_create_Statistics_empty():
    statistics = Statistics()
    assert statistics._entered_text == []


def test_mistakes():
    entered_text = ['Marek', 'Stanisław']
    text = ['Marek', 'Agata']
    statistics = Statistics(10, entered_text, text)
    assert statistics.mistakes() == 4


def test_chars_per_minute():
    entered_text = ['Marek', 'Stanisław']
    text = ['Marek', 'Stanisław']
    statistics = Statistics(60, entered_text, text)
    assert statistics.chars_per_minute() == 14


def test_chars_per_minute_mistakes():
    entered_text = ['Marek', 'Agata']
    text = ['Marek', 'Stanisław']
    statistics = Statistics(60, entered_text, text)
    assert statistics.chars_per_minute() == 6


def test_words_per_minute():
    entered_text_1 = ['Marek', 'Agata']
    entered_text_2 = ['Marek', 'Agata', 'Stanisław']
    text = ['Marek', 'Stanisław']
    statistics_1 = Statistics(60, entered_text_1, text)
    statistics_2 = Statistics(30, entered_text_2, text)
    assert statistics_1.words_per_minute() == 2
    assert statistics_2.words_per_minute() == 6
