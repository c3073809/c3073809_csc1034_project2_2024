from datetime import datetime, timedelta

class Booking:
    def __init__(self, room: str, start: datetime, hours: int, title: str, contact: str):
        # Validation checks for inputs based on constraints
        if not isinstance(room, str):
            raise TypeError("Room must be a string")
        if not isinstance(start, datetime):
            raise TypeError("Start must be a datetime object")
        if not isinstance(hours, int) or hours <= 0:
            raise TypeError("Hours must be a positive integer")
        if not isinstance(title, str):
            raise TypeError("Title must be an string")
        if not isinstance(contact, str):
            raise TypeError("Contact must be a string")
        if start.weekday() >= 5 or not (datetime.strptime("09:00", "%H:%M").time() <= start.time() <= datetime.strptime("18:00", "%H:%M").time()):
            raise TypeError("Bookings must be within Mon-Fri, 09:00-18:00")
        if start.weekday() >= 5:
            raise TypeError("Bookings must be within Monday to Friday.")

        self._room = room
        self._start = start
        self._hours = hours
        self._title = title
        self._contact = contact

    def get_room(self) -> str:
        print('Room that is tested:', self._room)
        return self._room

    def get_start(self) -> datetime:
        print('Start time:', self._start)
        return self._start

    def get_hours(self) -> int:
        print('Hours:', self._hours)
        return self._hours

    def get_title(self) -> str:
        print('Title:', self._title)
        return self._title

    def get_contact(self) -> str:
        print('Contact:', self._contact)
        return self._contact

    def __str__(self) -> str:
        return f"Booking({self._room}, {self._start}, {self._hours}, {self._title}, {self._contact})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        return isinstance(other, Booking) and self._room == other.get_room() and self._start == other.get_start()


    def __hash__(self) -> int:
        return hash((self._room, self._start))

    def overlaps_with(self, other) -> bool:
        if self._room != other.get_room():
            return False

        end_time = self._start + timedelta(hours=self._hours)
        other_end_time = other.get_start() + timedelta(hours=other.get_hours())
        print('End time:', other_end_time)

        return self._start < other_end_time and other.get_start() < end_time
