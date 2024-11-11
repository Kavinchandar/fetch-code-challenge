# fetch-code-challenge
My submission to Fetch Backend Engineer Aprenticeship postion

Table of Contents

    Code Structure
    How to Run the Code
    How to Docker Build and Docker Run
    Design Decisions

Code Structure

The project follows a modular structure to ensure clarity, maintainability, and scalability. Here’s a breakdown of the key directories and files:

project/
│
├── controller/                # Controller layer for routing and request handling
│   ├── app.py                 # Main application entry point
│   ├── config.py              # Configuration settings
│
├── handler/                   # Request handlers for specific routes and logic
│   ├── receipt_handler.py     # Handles receipt-related logic
│
├── models/                    # Data models that define the structure of the data
│   ├── receipt.py             # Defines the receipt model and related operations
│
├── services/                  # Business logic layer and service functions
│   ├── receipt_service.py     # Contains logic for processing receipts, calculating points, etc.
│
├── tests/                     # Unit and integration tests
│   ├── test_receipt.py        # Test cases for the receipt-related API endpoints
│
├── Dockerfile                 # Instructions to build a Docker image for the project
├── requirements.txt           # Python dependencies for the project
└── README.md                  # Project documentation (this file)

Key Directories and Files

    controller/: The controller layer defines the routes and the entry points for incoming requests. It’s responsible for calling the appropriate handler and returning a response.

    handler/: This layer contains the logic that handles requests and performs operations like creating a receipt, processing payments, etc. Each handler corresponds to a specific action (e.g., processing a receipt).

    models/: Defines the structure of the data used in the application. For instance, the receipt.py file defines the attributes of a receipt, such as items, retailer, total cost, and the methods that manipulate this data.

    services/: Contains business logic for operations such as calculating points for a receipt, validating data, and more. These are used by the handlers to process data and make decisions.

    tests/: Contains test cases for validating the functionality of the project. Each test file focuses on a specific module (e.g., test_receipt.py tests receipt-related functionalities).

    Dockerfile: Contains the instructions to build the Docker image for this project.

    requirements.txt: A list of Python dependencies required to run the project.

How to Run the Code

To run the code locally, follow these steps:

    Clone the repository:

git clone https://github.com/yourusername/project.git
cd project

Install the dependencies:

You need Python 3.x and pip installed. Install the dependencies listed in the requirements.txt file:

pip install -r requirements.txt

Run the application:

Once the dependencies are installed, you can run the app with the following command:

    python controller/app.py

    This will start the application, and you can access the API at http://localhost:5000.

How to Docker Build and Docker Run

The project includes a Dockerfile that allows you to build and run the application in a Docker container.

    Build the Docker image:

    To build the Docker image, run the following command in the root of the project:

docker build -t project-name .

Run the Docker container:

After building the image, you can run the Docker container with the following command:

    docker run -p 5000:5000 project-name

    This will start the application inside the container, and you can access it on http://localhost:5000.

Design Decisions
Why Layers for Controller, Handler, Models, and Services?

    Separation of Concerns (SoC): The project is divided into separate layers to keep the code modular and maintainable. Each layer is responsible for a specific concern:
        Controller handles the routing and request/response cycle.
        Handler is responsible for the core business logic of specific operations.
        Models define the data structures, ensuring consistency across the application.
        Services implement the business logic and interact with models and handlers.

    Scalability and Maintainability: By separating responsibilities into different layers, it becomes easier to scale and maintain the code. For example, if you need to add new functionalities or modify existing logic, you can easily pinpoint which part of the code needs to be updated.

    Testability: Dividing the code into these layers allows for easier unit testing. Each component can be tested in isolation, reducing the complexity of tests and making them more reliable. For instance, the receipt processing logic in the service layer can be independently tested, without worrying about HTTP request/response handling.

    Readability and Organization: This structure provides clarity on where certain code belongs. Developers can easily navigate through the project and understand where to look for specific functionalities or operations.

    Reusability: By structuring the code into services and handlers, these modules can be reused across different parts of the project. For example, the logic for processing receipts could be used in different API endpoints, or in future microservices.
