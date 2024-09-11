import boto3
from decimal import Decimal

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Get the reference to the StockPortfolio table
table = dynamodb.Table('StockPortfolio')

# Define mock data to insert
mock_data = [
    {
        'UserID': 'user1',
        'Timestamp': '2024-03-07T10:00:00',
        'StockSymbol': 'AAPL',
        'Quantity': 100,
        'Price': Decimal('150.25')  # Use Decimal type
    },
    {
        'UserID': 'user2',
        'Timestamp': '2024-03-07T10:00:00',
        'StockSymbol': 'GOOGL',
        'Quantity': 50,
        'Price': Decimal('2500.75')  # Use Decimal type
    },
    {
        'UserID': 'user3',
        'Timestamp': '2024-03-07T10:00:00',
        'StockSymbol': 'MSFT',
        'Quantity': 75,
        'Price': Decimal('300.50')
    },
    {
        'UserID': 'user4',
        'Timestamp': '2024-03-07T11:00:00',
        'StockSymbol': 'AMZN',
        'Quantity': 20,
        'Price': Decimal('3500.00')
    },
    {
        'UserID': 'user5',
        'Timestamp': '2024-03-07T11:00:00',
        'StockSymbol': 'TSLA',
        'Quantity': 30,
        'Price': Decimal('700.25')
    },
    {
        'UserID': 'user6',
        'Timestamp': '2024-03-07T11:00:00',
        'StockSymbol': 'NFLX',
        'Quantity': 40,
        'Price': Decimal('550.75')
    },
    {
        'UserID': 'user7',
        'Timestamp': '2024-03-07T11:00:00',
        'StockSymbol': 'GOOGL',
        'Quantity': 25,
        'Price': Decimal('2500.45')
    },
    {
        'UserID': 'user8',
        'Timestamp': '2024-03-07T11:00:00',
        'StockSymbol': 'VOO',
        'Quantity': 50,
       'Price': Decimal('380.75')
    }
]

# Insert mock data into the table
for item in mock_data:
    table.put_item(Item=item)

print("Mock data inserted successfully!")
