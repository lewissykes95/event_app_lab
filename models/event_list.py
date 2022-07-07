from models.event import Event
from datetime import date

event1 = Event(date(2022,7,20), "Jimmy Carr: Live", 500, "Main Stage", "Comedy show at the Festival Theatre main stage")
event2 = Event(date(2022, 7, 28), "CodeClan Live", 50, "Room E59", "Coding noobs struggling with Python")
event3 = Event(date(2022, 8, 1), "Mental Health Talk", 20, "Room Johnson", "Talking about mental health and well-being")

events = [event1, event2, event3]


