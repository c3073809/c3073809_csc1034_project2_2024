from datetime import datetime, timedelta

class Booking:
    def __init__(self, room: str, start: datetime, hours: int, title: str, contact: str):
        # Validation checks for inputs based on constraints
        if not isinstance(room, str):
            raise ValueError("Room must be a string")
        if not isinstance(start, datetime):
            raise ValueError("Start must be a datetime object")
        if not isinstance(hours, int) or hours <= 0:
            raise ValueError("Hours must be a positive integer")
        if not isinstance(title, str):
            raise ValueError("Title must be an string")
        if not isinstance(contact, str):
            raise ValueError("Contact must be a string")
        if start.weekday() >= 5 or not (datetime.strptime("09:00", "%H:%M").time() <= start.time() <= datetime.strptime("18:00", "%H:%M").time()):
            raise ValueError("Bookings must be within Mon-Fri, 09:00-18:00")

        self._room = room
        self._start = start
        self._hours = hours
        self._title = title
        self._contact = contact

    def get_room(self) -> str:
        return self._room

    def get_start(self) -> datetime:
        return self._start

    def get_hours(self) -> int:
        return self._hours

    def get_title(self) -> str:
        return self._title

    def get_contact(self) -> str:
        return self._contact

    def __str__(self) -> str:
        return f"Booking({self._room}, {self._start}, {self._hours}, {self._title}, {self._contact})"

    def __repr__(self) -> str:
        return self.__str__()

    # Equality and hash
    def __eq__(self, other) -> bool:
        return isinstance(other, Booking) and self._room == other.get_room() and self._start == other.get_start()


    def __hash__(self) -> int:
        return hash((self._room, self._start))

    # Check if two bookings overlap
    def overlaps_with(self, other) -> bool:
        if self._room != other.get_room():
            return False

        end_time = self._start + timedelta(hours=self._hours)
        other_end_time = other.get_start() + timedelta(hours=other.get_hours())

        return self._start < other_end_time and other.get_start() < end_time
