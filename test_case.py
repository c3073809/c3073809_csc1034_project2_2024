import unittest
from datetime import datetime, timedelta
from booking import Booking
from booking_manager import BookingManager

class TestBookingSystem(unittest.TestCase):
    def setUp(self):
        self.booking1 = Booking("FDC.G.41", datetime(2024, 10, 22, 12, 30), 2, "CSC1034 Lecture", "jennifer.warrender@newcastle.ac.uk")
        self.booking2 = Booking("FDC.G.42", datetime(2024, 10, 22, 14, 30), 1, "CSC1034 Lab", "jennifer.warrender@newcastle.ac.uk")
        self.manager = BookingManager([self.booking1])

    def test_add_booking(self):
        result = self.manager.add_booking(self.booking2)
        self.assertTrue(result)
        self.assertIn(self.booking2, self.manager.get_bookings())

    def test_overlapping_booking(self):
        overlapping_booking = Booking("FDC.G.41", datetime(2024, 10, 22, 13, 30), 1, "Overlapping", "test@newcastle.ac.uk")
        result = self.manager.add_booking(overlapping_booking)
        self.assertFalse(result)

    def test_remove_booking(self):
        result = self.manager.remove_booking(self.booking1)
        self.assertTrue(result)
        self.assertNotIn(self.booking1, self.manager.get_bookings())

    def test_remove_nonexistent_booking(self):
        non_existent_booking = Booking("FDC.G.43", datetime(2024, 10, 23, 10, 0), 1, "Nonexistent", "contact@newcastle.ac.uk")
        result = self.manager.remove_booking(non_existent_booking)
        self.assertFalse(result)

    def test_edit_booking(self):
        new_booking = Booking("FDC.G.41", datetime(2024, 10, 22, 15, 30), 1, "CSC1034 Seminar", "jennifer.warrender@newcastle.ac.uk")
        self.manager.edit_booking(self.booking1, new_booking)
        self.assertNotIn(self.booking1, self.manager.get_bookings())
        self.assertIn(new_booking, self.manager.get_bookings())

    def test_search_by_room(self):
        result = self.manager.search_by_room("FDC.G.41")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.booking1)

    def test_search_by_start_time(self):
        result = self.manager.search_by_start(datetime(2024, 10, 22, 12, 30))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.booking1)

    def test_search_for_room_timetable(self):
        date_from = datetime(2024, 10, 22, 0, 0)
        date_to = datetime(2024, 10, 23, 23, 59)
        result = self.manager.search_for_room_timetable(date_from, date_to, "FDC.G.41")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.booking1)

    def test_get_available_rooms(self):
        available_rooms = self.manager.get_available_rooms(datetime(2024, 10, 22, 15, 30), 1, ["FDC.G.41", "FDC.G.42"])
        self.assertIn("FDC.G.41", available_rooms)
        self.assertNotIn("FDC.G.42", available_rooms)

if __name__ == '__main__':
    unittest.main()
