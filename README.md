## Simple web application based on Python-Flask and Postgres with docker-compose-based deploy

### How to:

1. Install [docker](https://docs.docker.com/engine/install/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually)
2. Create ```./secrets/postgres_password.txt``` and ```./secrets/postgres_user.txt``` with your specific auth data.
(Examples of such files you can find in ```./secrets/``` folder)
3. ```sudo docker compose build```
4. ```sudo docker compose up -d```
5. Go to localhost in your browser
6. To disable application type ```docker compose down```