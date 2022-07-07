from models.event import Event
from datetime import date

event1 = Event(date(2022,7,20), "Jimmy Carr: Live", 500, "Main Stage", "Comedy show at the Festival Theatre main stage", False)
event2 = Event(date(2022, 7, 28), "CodeClan Live", 50, "Room E59", "Coding noobs struggling with Python", True)
event3 = Event(date(2022, 8, 1), "Mental Health Talk", 20, "Room Johnson", "Talking about mental health and well-being", True)

events = [event1, event2, event3]


def add_new_event(event):
    events.append(event)

def del_event(event_name):
    for event in events:
        if event_name == event.event_name: 
            events.remove(event)