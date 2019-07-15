from bs4 import BeautifulSoup
import regex as re
import string as st

class GetData():
    def __init__(self, html, div_class_to_capture):
        self.html = html
        self.div_class_to_capture = div_class_to_capture

    def strip_data(self):
        soup = BeautifulSoup(self.html, 'html.parser')

        mydiv = soup.findAll("div", {"class": self.div_class_to_capture})

        for text in mydiv:
            h1 = text.find('h1')
            p = text.find('p')

        return h1.text, p.text

    def extract_data(self):
        h1, p = self.strip_data()

        end_find = p.find(',') + 6
        start_find = p.find('n') + 1

        date = p[start_find:end_find]

        return h1, p, date
