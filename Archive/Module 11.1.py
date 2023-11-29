class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"book: {self.name}\nauthor: {self.author}\npage count: {self.page_count}\n")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"magazine: {self.name}\nchief editor: {self.chief_editor}\n")


publications = [Magazine("Donald Duck", "Aki Hyyppä"), Book("Compartment No. 6", "Rosa Liksom", 192)]

for publication in publications:
    publication.print_information()
