import unittest
import zad3pannagabriella as gaba


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(gaba.Resolver("Kristen", "Bell", "Kraina lodu").resolve(), gaba.ExitStatus.FOUND)
        self.assertEqual(gaba.Resolver("Johnny", "Depp", "Charlie").resolve(), gaba.ExitStatus.FOUND)
        self.assertEqual(gaba.Resolver("Jola", "Rutowicz", "Charlie").resolve(), gaba.ExitStatus.NOT_FOUND)
        self.assertEqual(gaba.Resolver("Anna", "Wesołowska", "Sędzia").resolve(), gaba.ExitStatus.FOUND)
        self.assertEqual(gaba.Resolver("Sacha", "Cohen", "Dyktator").resolve(), gaba.ExitStatus.FOUND)
        self.assertEqual(gaba.Resolver("Charlie", "Chaplin", "Dyktator").resolve(),
                         gaba.ExitStatus.FOUND_ACTOR_WITH_THAT_LAST_NAME)
        self.assertEqual(gaba.Resolver("Abelard", "Giza", "Wożonko").resolve(), gaba.ExitStatus.FOUND)
        self.assertEqual(gaba.Resolver("Jarosław", "Kaczyński", "O dwóch takich co ukradli księżyc").resolve(),
                         gaba.ExitStatus.FOUND)
        self.assertEqual(gaba.Resolver("Sylvester", "Stallone", "Ranczo").resolve(), gaba.ExitStatus.NOT_FOUND)
        self.assertEqual(gaba.Resolver("Sylvester", "Stallone", "Rambo").resolve(), gaba.ExitStatus.FOUND)
        self.assertEqual(gaba.Resolver("Sylvestro", "Stallone", "Rambo").resolve(),
                         gaba.ExitStatus.FOUND_ACTOR_WITH_THAT_LAST_NAME)


if __name__ == '__main__':
    unittest.main()
