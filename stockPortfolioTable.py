import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Define table schema
table = dynamodb.create_table(
    TableName='StockPortfolio',
    KeySchema=[
        {
            'AttributeName': 'UserID',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'Timestamp',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'UserID',
            'AttributeType': 'S'  # String
        },
        {
            'AttributeName': 'Timestamp',
            'AttributeType': 'S'  # String
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,   # Adjust according to your read/write requirements
        'WriteCapacityUnits': 5   # Adjust according to your read/write requirements
    }
)

# Wait for the table to be created
table.meta.client.get_waiter('table_exists').wait(TableName='StockPortfolio')

print("Table created successfully!")
