class Observable():
    def __init__(self):
        self.observers = []

    def register_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def notify_observers(self):
        for o in self.observers:
            o.update(self)


class Observer():
    def update(self):
        raise NotImplementedError()


class Blog(Observable):
    def __init__(self):
        super(Blog, self).__init__()
        self.articles = []

    def add_article(self, a):
        self.articles.append(a)
        self.notify_observers()

    def get_latest_article(self):
        return self.articles[-1]

    def show_articles(self):
        print(self.articles)

    def unsubscribe(self, o):
        self.remove_observer(o)

class BlogFollower(Observer):
    def __init__(self, subject):
        self.stuff_i_have_read = []
        subject.register_observer(self)

    def display_what_i_have_read(self):
        print(self.stuff_i_have_read)

    def update(self, o):
        self.stuff_i_have_read.append(o.get_latest_article())


if __name__ == "__main__":
    b = Blog()
    f1 = BlogFollower(b)
    f2 = BlogFollower(b)

    b.add_article("First post yay!")
    b.add_article("More posts huzzah!")

    b.unsubscribe(f1)

    b.add_article("It's been six months...")

    print("Articles in the blog:")
    b.show_articles()

    print("f1 read this:")
    f1.display_what_i_have_read()

    print("f2 read this:")
    f2.display_what_i_have_read()
