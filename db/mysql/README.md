# MySQL instance

## Docker 

1. Environment variables

    ```sh
    export MYSQL_SERVER_CONTAINER=mysql-db
    export MYSQL_ROOT_PASSWORD=my-root 
    export DB_DOCKER_NETWORK=db-net
    export MYSQL_PORT=3306
    ```
   
2. CLI commands

    ```sh
    docker network create --driver bridge $DB_DOCKER_NETWORK
    docker run --detach --name=$MYSQL_SERVER_CONTAINER --net=$DB_DOCKER_NETWORK --env="MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD" -p ${MYSQL_PORT}:3306 mysql
    export DBIP="$(docker inspect ${MYSQL_SERVER_CONTAINER} | grep -i 'ipaddress' | grep -oE '((1?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.){3}(1?[0-9][0-9]?|2[0-4][0-9]|25[0-5])')"
    echo $DBIP

    docker run -it -v ${HOST_DATA}:/data --net=$DB_DOCKER_NETWORK --link ${MYSQL_SERVER_CONTAINER}:mysql --rm mysql sh -c "exec mysql -h${DBIP} -uroot -p"
        or
    mysql -u root -P 3306 -h 172.23.0.2 --protocol=tcp -p  
    ```
3. Stop & clear
 
   ```sh
   docker ps
   docker stop mysql-db
   docker rm  mysql-db
   docker network help
   docker network ls
   docker network prune
   docker network rm db-net
   docker network ls
   ```
