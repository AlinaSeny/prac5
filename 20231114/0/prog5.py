class Asker:
    @staticmethod
    def askall(lst):
        for i in lst:
            i.report()


class Sender:
    first = 1

    @classmethod
    def report(cls):
        if cls.first:
            print("Greetings!")
            cls.first = 0
        else:
            print("Get away!")


Asker.askall([Sender() for i in range(3)]*2)
