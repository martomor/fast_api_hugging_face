# FastAPI and Hugging Face Integration

Provide a word as input and the model will reply back with the sentiment estimation. If you use the word "bad_word" the model will raise a 500 error.

## How to setup the service in a local server

Clone this repository to your local environment. Once you you do that run the below commands:

### Move to you repo

`cd fast_api_hugging_face`

### For buidling the docker image:

`docker build -t fast_api_hug .`

### For running the container:

`docker run -dp 8000:8000 fast_api_hug`

Thats it! atfer a minute or so you should be able to access the service on port 8000: http://0.0.0.0:8000/docs




