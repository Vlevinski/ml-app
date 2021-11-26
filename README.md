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

2. Spin up the container with FastAPI:

    ```sh
    $ docker run --name ml-app ml-app:latest
    ```
3. Run ML Linear Regression Model 

     '''sh
       docker run --name ml-one -e PORT=8008 -p 8008:8008 -d ml-app:latest
       docker exec -it ml-one python model.py
       docker exec -it ml-one ls -la
       ll
       sudo docker cp ml-app:/linear_regression.png .       
       mkdir data
       cd data      
       sudo docker cp ml-one:/linear_regression.png .
       docker exec -it ml-one pwd
       docker ps
       sudo docker cp ml-one:/app/linear_regression.png .
     '''
4. 
### Without Docker

1. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

1. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    
    ```

1. Run ML Linear Regression Model:

    ```sh
    (venv)$ python model.py
    ```

1. Test:

    ```sh
    to be developed
    ```
