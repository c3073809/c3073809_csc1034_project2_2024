import pickle
from datetime import timedelta

class BookingManager:
    def __init__(self, bookings=None):
        self._bookings = bookings if bookings is not None else []

    def get_bookings(self):
        return self._bookings

    def __str__(self) -> str:
        return f"BookingManager with {len(self._bookings)} bookings."

    def __repr__(self) -> str:
        return self.__str__()

    def add_booking(self, booking):
        for existing_booking in self._bookings:
            if existing_booking.overlaps_with(booking):
                return False
        self._bookings.append(booking)
        return True

    def remove_booking(self, booking):
        if booking in self._bookings:
            self._bookings.remove(booking)
            print('Booking that is removed:', booking)
            return True
        return False

    def edit_booking(self, old_booking, new_booking):
        if old_booking in self._bookings:
            self.remove_booking(old_booking)
            self.add_booking(new_booking)
            print('Old booking:', old_booking)
            print('New booking:', new_booking)
        else:
            raise ValueError("Old booking not found.")

    def search_by_room(self, room):
        return [b for b in self._bookings if b.get_room() == room]

    def search_by_start(self, start):
        return [b for b in self._bookings if b.get_start() == start]

    def search_for_room_timetable(self, date_from, date_to, room):
        return [
            b for b in self._bookings
            if b.get_room() == room and date_from <= b.get_start() <= date_to
        ]

    def get_available_rooms(self, start_time, hours, rooms):
        available_rooms = []
        requested_end_time = start_time + timedelta(hours=hours)

        for room in rooms:
            print('ALl rooms:',rooms)
            for booking in self._bookings:
                if booking.get_room() == room:
                    booking_start = booking.get_start()
                    booking_end = booking_start + timedelta(hours=booking.get_hours())

                    if requested_end_time <= booking_start or start_time >= booking_end:

                        available_rooms.append(room)

        print('Rooms that is available:', available_rooms)
        return available_rooms


    def save_to_file(self, file_name):
        with open(file_name, 'wb'):
            pickle.dump(self._bookings, file_name)