# eCommerce API using AWS Lambda, API Gateway, and DynamoDB

## Overview
This project is a **serverless eCommerce API** built using **AWS Lambda, API Gateway, and DynamoDB**. It allows users to perform CRUD operations on products, manage orders, and handle user authentication in a cost-effective, scalable manner.

## Features
- **Product Management**: Add, update, delete, and retrieve products.
- **Order Processing**: Create and track orders.
- **Serverless Architecture**: No need to manage servers, fully scalable.
- **AWS Free Tier Friendly**: Designed to stay within AWS's free limits.

## Tech Stack
- **AWS Lambda** - Backend logic
- **API Gateway** - Exposes HTTP endpoints
- **DynamoDB** - NoSQL database for storing data
- **IAM Roles** - Secure access to AWS services

## API Endpoints
| Method | Endpoint               | Description                  |
|--------|------------------------|------------------------------|
| POST   | `/products`            | Add a new product            |
| GET    | `/products`            | Retrieve all products        |
| GET    | `/products/{id}`       | Retrieve a product by ID     |
| PUT    | `/products/{id}`       | Update a product by ID       |
| DELETE | `/products/{id}`       | Delete a product by ID       |
| POST   | `/orders`              | Create a new order           |
| GET    | `/orders/{orderId}`    | Retrieve order details       |

## Setup & Deployment

### Prerequisites
- **AWS Account**
- **AWS CLI Installed & Configured**


## Testing the API
Use **Postman** or **Curl** to test API endpoints. Example:
```sh
curl -X GET https://your-api-id.execute-api.region.amazonaws.com/dev/products
```

## Future Enhancements
- Add **Stripe Payment Gateway** for transactions.
- Implement **Cognito User Authentication**.
- Introduce **GraphQL Support** for better query efficiency.


