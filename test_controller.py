import unittest
from controller import app
from services import ReceiptService, receipts

class TestReceiptEndpoints(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up test client
        cls.client = app.test_client()
        cls.client.testing = True

    def setUp(self):
        receipts.clear()
        pass

    def test_handle_process_receipt_success(self):
        # Test data
        data = {
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-03-20",
            "purchaseTime": "14:33",
            "items": [
                {
                "shortDescription": "Gatorade",
                "price": "2.25"
                },{
                "shortDescription": "Gatorade",
                "price": "2.25"
                },{
                "shortDescription": "Gatorade",
                "price": "2.25"
                },{
                "shortDescription": "Gatorade",
                "price": "2.25"
                }
            ],
            "total": "9.00"
            }

        # Call the endpoint
        response = self.client.post('/receipts/process', json=data)

        # Assert response
        self.assertEqual(response.status_code, 200)
        
        # get receipt_id
        receipt_id = response.json.get("id")
        self.assertIsNotNone(receipt_id)

        # Check that the receipt was actually added to the receipts dictionary
        self.assertIn(receipt_id, receipts)
        
        #get receipt
        receipt = receipts[receipt_id]
        
        # Check if data integrity is maintained
        self.assertEqual(str(receipt.retailer), str(data["retailer"]))
        self.assertEqual(str(receipt.purchase_date), str(data["purchaseDate"]))
        self.assertEqual(str(receipt.purchase_time), str(data["purchaseTime"]))
        self.assertEqual(float(receipt.total), float(data["total"]))
        self.assertEqual(len(receipt.items), len(data["items"]))

    def test_handle_get_points_success(self):
        # Create a mock receipt manually in the `receipts` dictionary
        receipt_id = "12345"  # Example receipt ID
        receipts[receipt_id] = ReceiptService.create_receipt(
                retailer="M&M Corner Market", 
                purchase_date="2022-03-20", 
                purchase_time="14:33", 
                items=[
                    {"shortDescription": "Gatorade", "price": 2.25},
                    {"shortDescription": "Gatorade", "price": 2.25},
                    {"shortDescription": "Gatorade", "price": 2.25},
                    {"shortDescription": "Gatorade", "price": 2.25}
                ],
                total=9.00
            )
        expected_points = 109
        # receipts[receipt_id].points = 109
        # Call the endpoint with the valid receipt_id
        response = self.client.get(f'/receipts/{receipt_id}/points')
       
        # Assert response
        self.assertEqual(response.status_code, 200)

        # Check the points returned in the response
        receipt = receipts[receipt_id]  # Retrieve the receipt from the dictionary
        self.assertEqual(response.json, {"points": expected_points})

if __name__ == "__main__":
    unittest.main()