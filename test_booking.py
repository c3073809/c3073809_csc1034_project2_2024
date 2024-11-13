import unittest
from datetime import datetime
from booking import Booking

class TestBooking(unittest.TestCase):

    def setUp(self):
        # Sample booking data from sample_data.csv
        self.room = "FDC.G.41"
        self.start = datetime(2024, 10, 22, 12, 30)
        self.hours = 1
        self.title = "CSC1034 Lecture"
        self.contact = "jennifer.warrender@newcastle.ac.uk"
        self.booking = Booking(self.room, self.start, self.hours, self.title, self.contact)

    def test_initialization(self):
        self.assertEqual(self.booking.get_room(), self.room)
        self.assertEqual(self.booking.get_start(), self.start)
        self.assertEqual(self.booking.get_hours(), self.hours)
        self.assertEqual(self.booking.get_title(), self.title)
        self.assertEqual(self.booking.get_contact(), self.contact)

    def test_str_representation(self):
        expected_str = f"Booking({self.room}, {self.start}, {self.hours}, {self.title}, {self.contact})"
        self.assertEqual(str(self.booking), expected_str)

    def test_equality(self):
        another_booking = Booking(self.room, self.start, self.hours, self.title, self.contact)
        self.assertEqual(self.booking, another_booking)

    def test_hash(self):
        another_booking = Booking(self.room, self.start, self.hours, self.title, self.contact)
        self.assertEqual(hash(self.booking), hash(another_booking))

    def test_overlap_with_same_time(self):
        overlapping_booking = Booking(self.room, self.start, self.hours, "Another Lecture", "another.contact@university.edu")
        self.assertTrue(self.booking.overlaps_with(overlapping_booking))

    def test_no_overlap_different_time(self):
        different_start = datetime(2024, 10, 22, 14, 30)
        non_overlapping_booking = Booking(self.room, different_start, self.hours, "Another Lecture", "another.contact@university.edu")
        self.assertFalse(self.booking.overlaps_with(non_overlapping_booking))

    def test_overlap_partial(self):
        overlapping_start = datetime(2024, 10, 22, 13, 0)  # 30 minutes overlap
        partially_overlapping_booking = Booking(self.room, overlapping_start, self.hours, "Overlap Test", "test@university.edu")
        self.assertTrue(self.booking.overlaps_with(partially_overlapping_booking))

    def test_invalid_room_type(self):
        with self.assertRaises(TypeError):
            Booking(123, self.start, self.hours, self.title, self.contact)

    def test_invalid_start_type(self):
        with self.assertRaises(TypeError):
            Booking(self.room, "2024-10-22 12:30", self.hours, self.title, self.contact)

    def test_invalid_hours(self):
        with self.assertRaises(TypeError):
            Booking(self.room, self.start, -1, self.title, self.contact)

    def test_out_of_hours_booking(self):
        start_outside_hours = datetime(2024, 10, 22, 19, 0)
        with self.assertRaises(TypeError):
            Booking(self.room, start_outside_hours, self.hours, self.title, self.contact)

    def test_out_of_days_booking(self):
        weekend_start = datetime(2024, 10, 20, 10, 0)  # Assuming it's a weekend (Sunday 10 ct)
        with self.assertRaises(TypeError):
            Booking(self.room, weekend_start, self.hours, self.title, self.contact)

if __name__ == "__main__":
    unittest.main()
