from pymongo import MongoClient


def add_expense(amount, date, toe: str, message=" "):
    entry = {'amount': amount,'date': date, 'type_of_expense': toe, 'description': message}
    client = MongoClient()
    db = client["expense"]
    collection = db.collection
    added_expense = collection.insert_one(entry)
    client.close()
    return


if __name__ == "__main__":
    add_expense(200, "food", "spent at ein/aus-stand")
