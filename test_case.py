import unittest
from datetime import datetime
from booking import Booking
from booking_manager import BookingManager
import csv

class TestBookingSystem(unittest.TestCase):

    def setUp(self):
        self.manager = BookingManager()
        self.load_bookings_from_csv("sample_data.csv")

    def load_bookings_from_csv(self, file_name):
        with open(file_name, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                room = row['room']
                date_str = row['date']
                time_str = row['time']
                hours = int(row['hours'])
                title = row['title']
                contact = row['contact']

                start_time = datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M")

                booking = Booking(room, start_time, hours, title, contact)
                self.manager.add_booking(booking)

    def test_booking_count(self):
        self.assertEqual(len(self.manager.get_bookings()), 12)

    def test_no_overlap_in_bookings(self):
        bookings = self.manager.get_bookings()
        for i in range(len(bookings)):
            for j in range(i + 1, len(bookings)):
                self.assertFalse(bookings[i].overlaps_with(bookings[j]),
                                 f"Booking {bookings[i]} overlaps with {bookings[j]}")

    def test_remove_booking(self):
        booking_to_remove = self.manager.get_bookings()[0]
        self.manager.remove_booking(booking_to_remove)
        self.assertNotIn(booking_to_remove, self.manager.get_bookings())
        self.assertEqual(len(self.manager.get_bookings()), 11)

    def test_edit_booking(self):
        old_booking = self.manager.get_bookings()[0]
        new_start_time = datetime(2024, 11, 15, 14, 0)
        new_booking = Booking(old_booking.get_room(), new_start_time, 1,
                              "Edited Lecture", old_booking.get_contact())
        self.manager.edit_booking(old_booking, new_booking)
        self.assertNotIn(old_booking, self.manager.get_bookings())
        self.assertIn(new_booking, self.manager.get_bookings())

    def test_search_by_room(self):
        room_bookings = self.manager.search_by_room("FDC.G.41")
        self.assertTrue(all(b.get_room() == "FDC.G.41" for b in room_bookings))

    def test_search_by_start(self):
        search_time = datetime.strptime("22/10/2024 12:30", "%d/%m/%Y %H:%M")
        start_bookings = self.manager.search_by_start(search_time)
        self.assertTrue(all(b.get_start() == search_time for b in start_bookings))

    def test_available_rooms(self):
        start_time = datetime.strptime("22/10/2024 14:30", "%d/%m/%Y %H:%M")
        hours = 1
        rooms = ["FDC.G.41", "USB.1.006", "ABC.1.001"]
        available_rooms = self.manager.get_available_rooms(start_time, hours, rooms)
        self.assertIn("ABC.1.001", available_rooms)  # Assuming ABC.1.001 is not booked

    def test_multiple_room_availability(self):
        manager = BookingManager()

        rooms = ["USB.1.006", "FDC.G.41", "ABC.1.001"]

        booking1 = Booking(
            room="USB.1.006",
            start=datetime(2024, 10, 24, 9, 0),
            hours=2,
            title="CSC1010 Lecture",
            contact="lecturer@example.com"
        )

        booking2 = Booking(
            room="FDC.G.41",
            start=datetime(2024, 10, 24, 11, 0),
            hours=1,
            title="CSC1011 Lecture",
            contact="lecturer@example.com"
        )

        manager.add_booking(booking1)
        manager.add_booking(booking2)
        available_rooms = manager.get_available_rooms(datetime(2024, 10, 24, 10, 0), 1, rooms)

        self.assertIn("FDC.G.41", available_rooms, "FDC.G.41 should be available at 10:00.")
        self.assertNotIn("USB.1.006", available_rooms, "USB.1.006 should not be available at 10:00.")
        self.assertIn("ABC.1.001", available_rooms, "ABC.1.001 should be available at 10:00.")




if __name__ == "__main__":
    unittest.main()
