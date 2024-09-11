# AWS-Project
# Stock Portfolio Management Application

The Stock Portfolio Management Application helps users efficiently manage their stock portfolios. It allows users to view, add, remove, and update stocks, check stock prices, and store portfolio data in AWS S3 for easy access.

## Features

- **View Portfolio:** See the current portfolio for a specific user.
- **Add Stock:** Add new stocks with quantity and price to the portfolio.
- **Remove Stock:** Remove a stock from the portfolio.
- **Update Stock:** Modify the quantity of an existing stock.
- **Check Stock Price:** View the current price of a stock.
- **Upload to S3:** Save portfolio data to an AWS S3 bucket for backup.
- **Download from S3:** Retrieve portfolio data from the S3 bucket.

## How to Use the Application

1. **View Portfolio for a User:**
   - Choose option `1`.
   - Enter the User ID.
  
2. **Add Stock to Portfolio:**
   - Choose option `2`.
   - Enter the User ID.
   - Provide the Stock Symbol, Quantity, and Price.

3. **Remove Stock from Portfolio:**
   - Choose option `3`.
   - Enter the User ID and Stock Symbol.

4. **Update Stock Quantity:**
   - Choose option `4`.
   - Enter the User ID, Stock Symbol, and the new Quantity.

5. **Check Stock Price:**
   - Choose option `5`.
   - Enter the Stock Symbol.

6. **Upload to S3 Bucket:**
   - Choose option `6`.
   - Enter the User ID.
   - Enter the Stock Symbol, Quantity, and Price for each stock. Type `done` to finish.

7. **Download from S3 Bucket:**
   - Choose option `7`.
   - Enter the User ID.

8. **Exit the Application:**
   - Choose option `8` to close the app.

## Concept Development

The application was developed to provide users with a simple yet effective tool for stock portfolio management. It leverages AWS DynamoDB for data storage and AWS S3 for portfolio backups, ensuring secure and accessible data management.

## Testing

1. **Functionality Testing:**
   - Each menu option was thoroughly tested for accuracy.
   - Valid and invalid inputs were tested to ensure proper error handling.

2. **Integration Testing:**
   - The integration between DynamoDB and S3 was tested for smooth data storage and retrieval.
   - Data consistency and integrity were verified.

3. **User Experience Testing:**
   - The user interface and prompts were tested for clarity.
   - Error handling was implemented for a smooth experience.

4. **Edge Case Testing:**
   - Tested with large data uploads/downloads to ensure robustness.
   - Extreme cases were handled to ensure the application remains stable.

## Technologies Used

- **Python**: Core programming language for the application.
- **AWS DynamoDB**: Storing user portfolio data.
- **AWS S3**: Storing and retrieving portfolio backups.
