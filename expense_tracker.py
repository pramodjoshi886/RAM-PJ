from pymongo import MongoClient
from datetime import datetime, timedelta
import random


def add_expense(name, amount, date, toe: str, message=" "):
    entry = {'name': name, 'amount': amount, 'date': date, 'type_of_expense': toe, 'description': message}
    client = MongoClient()
    db = client["expense"]
    collection = db.collection
    added_expense = collection.insert_one(entry)
    client.close()
    return


def edit_expense(name, new_amount, new_toe, new_message=" "):
    client = MongoClient()
    db = client["expense"]
    db.collection.update_one({"name": name}, {"$set": {"amount": new_amount, "type_of_expense": new_toe}})
    if new_message is not None:
        db.collection.update_one({"name": name}, {"$set": {'description': new_message}})


def remove_expense(name):
    client = MongoClient()
    db = client["expense"]
    db.collection.delete_one({"name": name})


def view_expense_past_n_days(n):
    client = MongoClient()
    db = client["expense"]
    current_date = datetime.now()
    past_date = current_date - timedelta(days=n)
    expenses = db.collection.find({'date': {'$gte': past_date}})

    return expenses


def view_all_expense():
    client = MongoClient()
    db = client["expense"]
    expenses = db.collection.find({})
    return expenses


if __name__ == "__main__":
    toe = ["food", "transport", "education", "rent", "games"]
    expense = [200, 100, 40, 290, 450]
    date = datetime.now()
    add_expense(random.choice(expense), date, random.choice(toe))
