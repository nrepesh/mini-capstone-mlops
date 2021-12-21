# mini-capstone-mlops

Example docker instructions

```
docker build -t mid .
docker run -p5000:5000 mid
```

The docker container should handle the containerization of the app. I hosted the container in GCP. 

In the repository, there are 2 query images to send to the endpoint. I have also included a client.py script which handles the request and response for the user.

Video: https://drive.google.com/file/d/1ed7jn9l3UqfASGzJHB-1A4Mh91u6mii5/view?usp=sharing