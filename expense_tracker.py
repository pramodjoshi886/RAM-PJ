from pymongo import MongoClient
from datetime import datetime
import random


def add_expense(amount, date, toe: str, message=" "):
    entry = {'amount': amount,'date': date, 'type_of_expense': toe, 'description': message}
    client = MongoClient()
    db = client["expense"]
    collection = db.collection
    added_expense = collection.insert_one(entry)
    client.close()
    return




if __name__ == "__main__":
    toe = ["food", "transport", "education", "rent", "games"]
    expense = [200, 100, 40, 290, 450]
    date = datetime.now()
    add_expense(random.choice(expense), date, random.choice(toe))
