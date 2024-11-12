# c3073809_csc1034_practical-2_2023

## Project Overview
This program allow users to book, edit, remove, find an available rooms, and open the room timetable
The program also ensures that the booking that the users made does not overlap for the same room
and operates within the business hours. 

## Structure
- **booking.py**: This represents an individual room booking  
- **booking_manager.py**: Contains classes and responsible for managing booking and no overlapping  
- **test_case**: To test the functionality of the booking.py and booking_manager.py

## Features
- **Create booking**: This allow users to create booking and validate the date, time, and room  
- **Booking management**: This class allow users to add, remove, edit, and search booking that they 
have made  
- **Room availability**: Users can check for available rooms within the time and ensure that there 
is no room that are overlapping   
- **File save and load**: The booking that the users have made can be saved and load 

## Descriptions (Attributes)
- **Room**: String (The name of the room)  
- **Start**: Datetime (Starting time of the booking)
- **Integer**: Integer (Time duration of the booking)  
- **Title**: String (The purpose of the booking)  
- **Contact**: String (Contact email for the booking)  

## `booking_manager.py` classes
- **add_booking**: Add booking to the time schedule if the booking is not overlapping with other booking
- **remove_booking**: Remove an existing booking 
- **edit_booking**: Edit an existing booking
- **search_by_room**: Search function for searching a room and start time 
- **get_available_rooms**: Return a list of available room
- **save_to_file**: Saves booking to a file

# Evidence of correct testing
![Evidence of Correct Testing](C:\Users\natan\OneDrive\Documents\Newcastle Uni\project2ss.png)  
From this image we can see that all of the test_case already passed (9 out of 9 tests) and also all of 
the print statement from booking that is removed, old booking, new booking, and all of the rooms that is 
available. 









