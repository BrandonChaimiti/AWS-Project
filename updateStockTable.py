import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Get the reference to the Courses table
table = dynamodb.Table('StockPortfolio')

# Update the table to add new attributes
response = table.update(
    AttributeDefinitions=[
        {
            'AttributeName': 'StockSymbol',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Quantity',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'Price',
            'AttributeType': 'N'
        }
    ],
    BillingMode='PROVISIONED',  # Placeholder value
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# Print the updated table description
print("Table description after update:", response)