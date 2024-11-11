import uuid

# In-memory storage for receipts
receipts = {}

class Item:
    def __init__(self, shortDescription, price):
        self.shortDescription = shortDescription
        self.price = float(price)

class Receipt:
    def __init__(self, retailer, purchase_date, purchase_time, items, total):
        self.retailer = retailer
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.items = [Item(**item) for item in items]
        self.total = float(total)
        self.points = 0
        self.id = str(uuid.uuid4())
