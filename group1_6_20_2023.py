def enough_sleep(classes_taken, school_clubs, down_time, test_next_day):
    classes_taken = classes_taken * 2.5
    school_clubs = school_clubs * 0.5
    test_hours = 0
    if test_next_day == True:
        test_hours = 5
    else:
        test_hours = 0
    total_time = 24 - (school_clubs + classes_taken + down_time + test_hours)
    if total_time <= 6:
        return("I'm tired!")
    elif total_time > 6 and total_time < 8:
        return("That's alright.")
    else:
        return("Thank goodness...")

def birthday_party(num_attendees, avg_age):
    num_attendees = int(num_attendees)
    avg_age = int(avg_age)
    if num_attendees <= 15:
        return("Venue: Home")
    elif num_attendees <= 30:
        return("Venue: Arcade")
    else:
        if avg_age <= 14:
            return("Venue: Amusement Park ; Type of Ride: Kid Rides")
        else:
            return("Venue: Amusement Park ; Type of Ride: Regular Rides")
