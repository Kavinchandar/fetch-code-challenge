# Receipt Processor (Fetch code challenge - My Submission)
Built backend using Flask with a Dockerized setup to run the code

# Table of Contents

1. [How to run the application](#how-to-run-the-application)
   1. [Clone the Repository](#1-clone-the-repository)
   2. [Build Docker Image](#2-build-docker-image)
   3. [Docker run to start a container to run the app](#3-docker-run-to-start-a-container-to-run-the-app)
   4. [Test Endpoints (Check summary of API)](#4-test-endpoints-check-summary-of-api)
2. [Design Decisions](#design-decisions)
3. [Summary of API Specification](#summary-of-api-specification)
   1. [Endpoint: Process Receipts](#endpoint-process-receipts)
   2. [Endpoint: Get Points](#endpoint-get-points)



## How to run the application

# Running the Application

Follow these steps to run the application on a new machine.

## 1. Clone the Repository

First, clone the repository to your local machine. Open a terminal and run:
```
git clone https://github.com/your-username/your-repository.git
```

## 2. Build Docker Image
```
docker build -t receipt-processor-app .
```

## 3. Docker run to start a container to run the app
```
docker run -p 8080:8080 receipt-processor-app
```

## 4. Test Endpoints (Check summary of API)

Test 
1. POST `http://127.0.0.1:8080/receipts/process` with 
body
```
{
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
```

2. GET `http://localhost:8080/receipts/<receipt_id>/points`

The <receipt_id> is generated on posting a receipt.

## Design Decisions

The decision to split the codebase into distinct layers of **controllers**, **services**, **models**, and **tests** follows established software engineering principles aimed at improving maintainability, scalability, and readability. Here's why each layer is utilized:

### 1. **Controller Layer** `controller.py`
The **controller** layer is responsible for handling incoming HTTP requests, managing the interaction with clients, and returning the appropriate responses. This layer serves as the interface between the external world and the core business logic of the application. By keeping the controller's responsibility focused only on handling HTTP requests and responses, we ensure that it remains thin and focused. This design also makes it easier to modify or replace the HTTP layer without affecting the core logic.

Key Benefits:
- **Separation of Concerns**: The controller only processes the incoming request and delegates business logic to the service layer.
- **Simplicity**: Keeping controllers light and delegating logic to services makes the codebase easier to understand and extend.

### 2. **Service Layer** `services.py`
The **service** layer contains the core business logic and is responsible for performing actions based on the input it receives from the controller. By centralizing the business logic here, we promote code reuse and make it easier to manage complex interactions between different parts of the application. The service layer interacts with the **model** layer to fetch or store data and applies necessary business rules or transformations.

Key Benefits:
- **Reusability**: Logic can be reused across multiple controllers or other services without duplication.
- **Maintainability**: Business logic can be modified independently from the HTTP-related concerns, reducing the risk of introducing bugs in unrelated parts of the application.
- **Testability**: The service layer can be tested in isolation from the web framework and controller, which improves test coverage and reduces complexity in testing.

### 3. **Model Layer** `models.py`
The **model** layer is responsible for representing the application's data structure and interacting with the database or other data sources. In this case, models are typically responsible for validating and structuring the receipt data, ensuring that it conforms to the required format before being processed. The model layer abstracts away database-specific details and offers a clean interface for interacting with data.

Key Benefits:
- **Encapsulation**: By placing data structures and database interactions in models, we keep the application code clean and avoid cluttering the service or controller layers with database logic.
- **Consistency**: The model layer ensures that data integrity is maintained, and validation is centralized.

### 4. **Test Layer** `test_controller.py`
Tests are an essential part of the development process to ensure the correctness and reliability of the application. The test layer is organized to mirror the structure of the application, with unit and integration tests covering the controller, service, and model layers. Tests help verify that each part of the application behaves as expected, both individually and when integrated.

Key Benefits:
- **Test Isolation**: By testing each layer independently (e.g., service layer logic can be tested without involving the controller or database), we can quickly identify and fix issues.
- **Continuous Confidence**: Automated tests provide confidence that future changes won’t break existing functionality, enabling more frequent and safer deployments.
- **Documenting Behavior**: Well-written tests serve as documentation for expected behavior, making it easier for new developers to understand how the application is supposed to work.

### Conclusion
Splitting the application into these distinct layers—controllers, services, models, and tests—helps us adhere to the **Single Responsibility Principle** (SRP) and promotes **separation of concerns**. This makes the codebase more organized, scalable, and easier to maintain in the long term. Additionally, this structure facilitates unit testing and makes the app more adaptable to future changes or feature additions.

## Summary of API Specification

### Endpoint: Process Receipts

* Path: `/receipts/process`
* Method: `POST`
* Payload: Receipt JSON
* Response: JSON containing an id for the receipt.

Description:

Takes in a JSON receipt (see example in the example directory) and returns a JSON object with an ID generated by your code.

The ID returned is the ID that should be passed into `/receipts/{id}/points` to get the number of points the receipt
was awarded.

Example Response:
```json
{ "id": "7fb1377b-b223-49d9-a31a-5a02701dd310" }
```

## Endpoint: Get Points

* Path: `/receipts/{id}/points`
* Method: `GET`
* Response: A JSON object containing the number of points awarded.

A simple Getter endpoint that looks up the receipt by the ID and returns an object specifying the points awarded.

Example Response:
```json
{ "points": 32 }
```








