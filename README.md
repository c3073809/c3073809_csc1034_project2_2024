# c3073809_csc1034_project2_2024

>## Project Overview
This program allow users to book, edit, remove, find an available rooms, and open the room timetable
The program also ensures that the booking that the users made does not overlap for the same room
and operates within the business hours. 

>## Structure
- **booking.py**: This represents an individual room booking  
- **booking_manager.py**: Contains classes and responsible for managing booking and no overlapping  
- **test_case**: To test the functionality of the booking_manager.py
- **test_booking**: To test the functionality of the booking.py 

>## Features
- **Create booking**: This allows users to create booking and validate the date, time, and room  
- **Booking management**: This class allow users to add, remove, edit, and search booking that they 
have made  
- **Room availability**: Users can check for available rooms within the time and ensure that there 
is no room that are overlapping   
- **File save and load**: The booking that the users have made can be saved and load 

>## Descriptions
### `booking.py` function
- **Room (get_room)**: The name of the room (string)
- **Start (get_start)**: Starting time of the booking (Datetime)
- **Hours (get_hours)**: Time duration of the booking (string) 
- **Title (get_title)**: The purpose of the booking (string) 
- **Contact (get_contact)**: Contact email of the booking (string)  

### `booking_manager.py` function
- **add_booking**: Add booking to the time schedule if the booking is not overlapping with other booking
- **remove_booking**: Remove an existing booking 
- **edit_booking**: Edit an existing booking
- **search_by_room**: Search function for searching a room and start time 
- **get_available_rooms**: Return a list of available room
- **save_to_file**: Saves booking to a file

>## Testing 
### test_booking.py for booking.py
- **setUp**: Initial state for the test by creating 'Booking' with attributes such as ('room', 'start',
'hours', 'title', and 'contact')
- **test_initialization**: Test if the booking initializes with the correct data
- **test_str_representation**: Test if the string of the booking is correct
- **test_hash**: Test if the hash work as expected
- **test_overlap_with_same_time**: Test if the program can detect overlapping situation when the time are 
the same
- **test_no_overlap_different_time**: Test if the program can detect for non-overlapping times
- **test_overlap_partial**: Test if the program can detect overlap for partially overlapping bookings
- **test_invalid_room_type**: Test if an exception is raised for the invalid room type 
- **test_invalid_start_type**: Test if an exception is raised for invalid start time 
- **test_invalid_hours**: Test if an exception is raised for invalid hours value
- **test_out_of_hours_booking**: Test if an exception is raised for the booking is outside of working hours
- **test_out_of_days_booking**: Test if an exception is raised for booking on weekends

### test_case.py for booking_manager.py
- **setUp**: Initial a BookingManager instance and populates it with bookings from a csv file that already
provided "sample_data.csv"
- **load_bookings_from_csv**: Adds a csv file "sample_data.csv" to the BookingManager
- **test_booking_count**: Test to make sure that none of the bookings overlap each other
- **test_remove_booking**: Test that checks the functionality to removing a booking
- **test_edit_booking**: Test check the ability for the users to edit a booking
- **test_search_by_room**: Test the functionality to search a bookings by rooms
- **test_search_by_start**: Test the functionality to search a booking by start time 
- **test_available_rooms**: Test to check if the program cna check the room availability 
- **test_multiple_room_availability**: Test that creates a new variable of BookingManager and set up a 
scenario with two bookings 










