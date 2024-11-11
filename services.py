import math
import re
from datetime import datetime
from models import Receipt, receipts

class ReceiptService:
    
    @staticmethod
    def create_receipt(retailer, purchase_date, purchase_time, items, total):
        # Create a new receipt instance
        receipt = Receipt(
            retailer=retailer,
            purchase_date=purchase_date,
            purchase_time=purchase_time,
            items=items,
            total=total
        )
        # Calculate points and store the receipt
        receipt.points = ReceiptService.calculate_points(receipt)
        receipts[receipt.id] = receipt
        return receipt
    
    @staticmethod
    def get_receipt_points(receipt_id):
        # Fetch the receipt by its ID
        receipt = receipts.get(receipt_id)
        if receipt:
            return receipt.points
        return None

    @staticmethod
    def calculate_points(receipt):
        points = 0
        
        # 1 point per alphanumeric character in retailer name
        points += len(re.findall(r'[a-zA-Z0-9]', receipt.retailer))

        # 50 points if total is a round dollar amount with no cents
        if receipt.total == int(receipt.total):
            points += 50

        # 25 points if total is a multiple of 0.25
        if receipt.total % 0.25 == 0:
            points += 25

        # 5 points for every two items on the receipt
        points += (len(receipt.items) // 2) * 5

        # Points for item descriptions and prices
        for item in receipt.items:
            desc = item.shortDescription.strip()
            if len(desc) % 3 == 0:
                points += math.ceil(item.price * 0.2)

        # 6 points if purchase day is odd
        date = datetime.strptime(receipt.purchase_date, "%Y-%m-%d")
        if date.day % 2 != 0:
            points += 6

        # 10 points if purchase time is between 2:00pm and 4:00pm
        time = datetime.strptime(receipt.purchase_time, "%H:%M")
        if 14 <= time.hour < 16:
            points += 10

        return points
