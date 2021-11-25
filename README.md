# Deploying a Machine Learning Linear Regression Model

## Want to learn how to build this?

Check out the [post](https://scikit-learn.org/stable/modules/linear_model.html).

## Want to use this project?

### With Docker
     (on development)
     
1. Build and tag the Docker image:

    ```sh
    $ docker build -t ml-app .
    ```

1. Spin up the container:

    ```sh
    $ docker run --name ml-app ml-app:latest
    ```

1. Train the model with random data:

    ```sh
    $ docker exec -it ml-app python

    ```

1. Test:

    ```sh
     to be developed
    ```

### Without Docker

1. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

1. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    
    ```

1. Run the app:

    ```sh
    (venv)$ python ml-app.py
    ```

1. Test:

    ```sh
    to be developed
    ```
