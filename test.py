import unittest
from Resolver import Resolver
from Resolver import ExitStatus

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Resolver("Kristen", "Bell", "Kraina lodu").resolve(), ExitStatus.FOUND)
        self.assertEqual(Resolver("Johnny", "Depp", "Charlie").resolve(), ExitStatus.FOUND)
        self.assertEqual(Resolver("Jola", "Rutowicz", "Charlie").resolve(), ExitStatus.NOT_FOUND)
        self.assertEqual(Resolver("Anna", "Wesołowska", "Sędzia").resolve(), ExitStatus.FOUND)
        self.assertEqual(Resolver("Sacha", "Cohen", "Dyktator").resolve(), ExitStatus.FOUND)
        self.assertEqual(Resolver("Charlie", "Chaplin", "Dyktator").resolve(),
                         ExitStatus.FOUND_ACTOR_WITH_THAT_LAST_NAME)
        self.assertEqual(Resolver("Abelard", "Giza", "Wożonko").resolve(), ExitStatus.FOUND)
        self.assertEqual(Resolver("Jarosław", "Kaczyński", "O dwóch takich co ukradli księżyc").resolve(),
                         ExitStatus.FOUND)
        self.assertEqual(Resolver("Sylvester", "Stallone", "Ranczo").resolve(), ExitStatus.NOT_FOUND)
        self.assertEqual(Resolver("Sylvester", "Stallone", "Rambo").resolve(), ExitStatus.FOUND)


if __name__ == '__main__':
    unittest.main()
