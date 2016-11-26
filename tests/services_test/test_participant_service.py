import unittest
from mock import MagicMock
from services.participant_service import ParticipantService
import io
import os

class TestParticipantService(unittest.TestCase):

    def setUp(self):
        self.dao_mock = MagicMock()
        self.unit_under_test = ParticipantService(self.dao_mock)

    def test_upload_and_store_paticipants(self):
        file = MagicMock()
        file.stream = io.open("./tests/test_data/correct_participants_file.csv")
        week = "2016_46"
        actual = self.unit_under_test.store_participants_from_file(file, week)
        # asserts database called 5 times
        self.assertEqual(5, self.dao_mock.store_participant.call_count)
        # assert number of stored participants is 5
        self.assertEqual(5, actual)

    def test_upload_and_store_paticipants_throw_error_when_missing_file(self):
        file = None
        week = "2016_46"
        with self.assertRaises(ValueError):
            self.unit_under_test.store_participants_from_file(file, week)

    def test_upload_and_store_paticipants_from_file_with_some_errors(self):
        file = MagicMock()
        file.stream = io.open("./tests/test_data/participants_file_with_errors.csv")
        week = "2016_46"
        actual = self.unit_under_test.store_participants_from_file(file, week)
        # asserts database called 5 times
        self.assertEqual(2, self.dao_mock.store_participant.call_count)
        # assert number of stored participants is 5
        self.assertEqual(2, actual)