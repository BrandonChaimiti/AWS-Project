import boto3
from decimal import Decimal
from datetime import datetime
import json

# Initialize DynamoDB client and the S3 client
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

# Get the reference to the StockPortfolio table and the bucket
table = dynamodb.Table('StockPortfolio')
stock_bucket = 'myprojectstockbucket'

# Define S3 functions
def upload_to_s3(file_name, data):
    # Uploads data to the specified S3 bucket
    s3.put_object(Bucket=stock_bucket, Key=file_name, Body=data)
def download_from_s3(file_name):
    # Downloads data from the specified S3 bucket
    response = s3.get_object(Bucket=stock_bucket, Key=file_name)
    return response['Body'].read()

# The menu for the stock portfolio program
def display_menu():
    # Displays the menu options for the user
    print("Menu:")
    print("1. View Portfolio for a User")
    print("2. Add Stock to Portfolio")
    print("3. Remove Stock from Portfolio")
    print("4. Update Stock Quantity")
    print("5. Check Stock Price")
    print("6. Upload to S3 bucket")
    print("7. Download from S3 bucket")
    print("8. EXIT")

# Function used to view the portfolio, utilizing the userID as identification
def view_portfolio():
    # Retrieves and displays the portfolio for a given user ID
    user_id = input("Enter User ID: ")
    response = table.query(
        KeyConditionExpression='UserID = :user_id',
        ExpressionAttributeValues={
            ':user_id': user_id
        }
    )
    items = response.get('Items', [])
    if items:
        print("Portfolio for User ID:", user_id)
        for item in items:
            print(item)
    else:
        print("No portfolio found for User ID:", user_id)

# Function to add stock to portfolio
def add_stock_to_portfolio():
    # Adds a new stock entry to the user's portfolio
    user_id = input("Enter User ID: ")
    stock_symbol = input("Enter Stock Symbol: ")
    quantity = int(input("Enter Quantity: "))
    price = Decimal(input("Enter Price: "))  # Use Decimal type for price
    timestamp = datetime.now().isoformat()  # Get current timestamp

    table.put_item(
        Item={
            'UserID': user_id,
            'Timestamp': timestamp,
            'StockSymbol': stock_symbol,
            'Quantity': quantity,
            'Price': price
        }
    )
    print("Stock added to portfolio successfully!")

# Function to remove stock from the portfolio
def remove_stock_from_portfolio():
    # Removes a stock entry from the user's portfolio
    user_id = input("Enter User ID: ")
    stock_symbol = input("Enter Stock Symbol to remove: ")

    response = table.delete_item(
        Key={
            'UserID': user_id,
            'StockSymbol': stock_symbol
        }
    )
    print("Stock removed from portfolio successfully!")

# Function to update the stock amount
def update_stock_quantity():
    # Updates the quantity of a particular stock in the user's portfolio
    user_id = input("Enter User ID: ")
    stock_symbol = input("Enter Stock Symbol to update: ")
    new_quantity = int(input("Enter new Quantity: "))

    table.update_item(
        Key={
            'UserID': user_id,
            'StockSymbol': stock_symbol
        },
        UpdateExpression='SET Quantity = :q',
        ExpressionAttributeValues={
            ':q': new_quantity
        }
    )
    print("Stock quantity updated successfully!")

# Function to check the stock price
def check_stock_price():
    # Checks the current price of a given stock
    stock_symbol = input("Enter Stock Symbol to check price: ")

    response = table.get_item(
        Key={
            'StockSymbol': stock_symbol
        }
    )
    item = response.get('Item')
    if item:
        print(f"Current price for {stock_symbol}: {item['Price']}")
    else:
        print(f"No information found for stock symbol: {stock_symbol}")

# Function to upload portfolio data to S3
def upload_portfolio_to_s3(user_id):
    # Allows users to upload their portfolio data to an S3 bucket
    portfolio_data = {'stocks': []}

    while True:
        stock_symbol = input("Enter Stock Symbol (or 'done' to finish): ")
        if stock_symbol == 'done':
            break

        quantity = int(input("Enter Quantity: "))
        price = Decimal(input("Enter Price: "))

        stock_info = {
            'symbol': stock_symbol,
            'quantity': quantity,
            'price': str(price)  # Convert Decimal to string
        }

        portfolio_data['stocks'].append(stock_info)

    file_name = f"{user_id}_portfolio.json"
    upload_to_s3(file_name, json.dumps(portfolio_data))

    print(f"Portfolio data for User ID {user_id} uploaded to S3 successfully!")

# Function to download portfolio data from S3
def download_portfolio_from_s3(user_id):
    # Enables users to download their portfolio data from S3
    file_name = f"{user_id}_portfolio.json"
    data = download_from_s3(file_name)
    print(f"Portfolio data for User ID {user_id} downloaded from S3 successfully!")
    return data.decode()

# Main function to display the menu and run the program
def main():
    while True:
        # Display the menu
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_portfolio()
        elif choice == '2':
            add_stock_to_portfolio()
        elif choice == '3':
            remove_stock_from_portfolio()
        elif choice == '4':
            update_stock_quantity()
        elif choice == '5':
            check_stock_price()
        elif choice == '6':
            user_id = input("Enter User ID: ")
            upload_portfolio_to_s3(user_id)
        elif choice == '7':
            user_id = input("Enter User ID: ")
            portfolio_data = download_portfolio_from_s3(user_id)
            print("Portfolio Data:", portfolio_data)
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
