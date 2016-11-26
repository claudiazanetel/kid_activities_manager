import unittest

from models.participant import Participant
from services.groups_creator import GroupsCreator as unit_under_test
from datetime import datetime

class TestGroupsCreator(unittest.TestCase):

    @staticmethod
    def d(string_date):
        return datetime.strptime(string_date, '%d/%M/%Y')

    def setUp(self):
        self.participants = [
            Participant("John Doe", TestGroupsCreator.d("01/01/1908"), "2016-46"),
            Participant("Mary Doe", TestGroupsCreator.d("01/01/1907"), "2016-46"),
            Participant("Spiriton Luis", TestGroupsCreator.d("01/01/1909"), "2016-46"),
            Participant("Alfred Luis", TestGroupsCreator.d("01/01/1907"), "2016-46"),
            Participant("Gustav Olsson", TestGroupsCreator.d("01/01/1908"), "2016-46")
        ]

    def test_create_groups_by_age(self):
        result = unit_under_test.by_age(self.participants, 3)

        self.assertEqual(1909, result[0][0].dob.year)
        self.assertEqual(1908, result[1][0].dob.year)
        self.assertEqual(1907, result[1][1].dob.year)
        self.assertEqual(1908, result[2][0].dob.year)
        self.assertEqual(1907, result[2][1].dob.year)

    def test_create_groups_by_age_more_groups_then_participants(self):
        result = unit_under_test.by_age(self.participants, 6)

        self.assertTrue(len(result[0]) == 0)
        self.assertEqual(1909, result[1][0].dob.year)
        self.assertEqual(1908, result[2][0].dob.year)
        self.assertEqual(1908, result[3][0].dob.year)
        self.assertEqual(1907, result[4][0].dob.year)
        self.assertEqual(1907, result[5][0].dob.year)

    def test_create_groups_mixed(self):
        result = unit_under_test.mixed(self.participants, 3)

        self.assertEqual(1909, result[0][0].dob.year)
        self.assertEqual(1908, result[1][0].dob.year)
        self.assertEqual(1907, result[1][1].dob.year)
        self.assertEqual(1908, result[2][0].dob.year)
        self.assertEqual(1907, result[2][1].dob.year)

    def test_create_groups_mixed_more_groups_then_participants(self):
        result = unit_under_test.mixed(self.participants, 6)

        self.assertTrue(len(result[0]) == 0)
        self.assertEqual(1909, result[1][0].dob.year)
        self.assertEqual(1908, result[2][0].dob.year)
        self.assertEqual(1908, result[3][0].dob.year)
        self.assertEqual(1907, result[4][0].dob.year)
        self.assertEqual(1907, result[5][0].dob.year)
