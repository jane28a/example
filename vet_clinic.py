from datetime import datetime, timedelta

class Animal:

    def __init__(self, kind, name, age):

        self.kind = kind
        self.name = name
        self.age = age

    def __str__(self):
        return 'This is a {} named {} {} years old'.format(
                                                        self.kind,
                                                        self.name,
                                                        self.age)

    def __repr__(self):
        return 'Animal("{}", "{}", {})'.format(
                                            self.kind,
                                            self.name,
                                            self.age)

    @classmethod
    def dog(cls):
        name = input('Your dog name is ')
        age = input('How old is it? ')
        size = input('Size of your dog: ')
        dog = cls('dog', name, age)
        dog.size = size
        return dog

    @staticmethod
    def year_ago():
        return datetime.now() - timedelta(days=365)

    @staticmethod
    def two_years_ago():
        return datetime.now() - timedelta(days=730.5)

    def get_vaccinated(self):
        if self.kind in ['dog', 'cat']:
            if getattr(self, 'vaccination_date', self.two_years_ago()) < self.year_ago():
                self.vaccination_date = datetime.now()
        else:
            print("We will not vaccinate your animal!")


if __name__ == '__main__':

    the_dog = Animal.dog()
    print(the_dog, the_dog.size)

    the_humster = Animal('humster', 'Mike', 2)
    print(the_humster)








