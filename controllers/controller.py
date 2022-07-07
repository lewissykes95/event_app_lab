from crypt import methods
from flask import render_template, request, redirect
from app import app
from models.event import Event
from models.event_list import events, add_new_event, del_event

@app.route("/events")
def index():
    return render_template("index.html", events=events)

@app.route("/events", methods=["POST"])
def add_event():
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_num_guest= request.form["num_guest"]
    event_room = request.form["room"]
    event_description = request.form["description"]
    event_recurring = request.form["recurring"]
    new_event = Event(event_date, event_name, event_num_guest, event_room, event_description, event_recurring)
    add_new_event(new_event)
    return redirect("/events")

@app.route("/events/delete", methods=["POST"])
def delete_event():
    selected_event = request.form["delete_event"]
    del_event(selected_event)   
    return redirect("/events") 
    







# @app.route('/orders/<int:index>')
# def order(index):
#     return render_template('order.html', order=customer_orders[index])


    