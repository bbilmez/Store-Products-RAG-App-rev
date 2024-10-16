This is a submission of the final project for DataTalksClub's [LLM Zoomcamp 2024](https://github.com/DataTalksClub/llm-zoomcamp). 
The purpose of the project is to demonstrate the ability to apply LLM technology to a selected problem domain while following the best practices taught in the course (code refactoring, testing, linting etc.)

This project is a proof-of-concept for a RAG application for querying information on store products. 

**Features**<br>
This project is a Flask application that integrates Elasticsearch for product search and a Hugging Face LLM for generating responses based on product descriptions.

**Dataset - `store_products.csv`**<br>
This is an AI-generated toy dataset containing product info: *id*, *name*, *category*, and *description*. It can be replaced by real-world data with the same fields.

**Dependencies - `requirements.txt`**
<ul>
<li>flask</li>
<li>flask_cors</li>
<li>elasticsearch</li>
<li>transformers</li>
<li>pandas</li>
<li>pytest</li>
<li>requests</li>
<li>flake8</li>
<li>black</li>
<li>python-logging-loki</li>
</ul>

**Usage**

Clone the repo and use the Makefile to set up the environment and launch and test the app. 
1. Clone the repo.
2. Run `make install` in the terminal to install all the dependencies in `requirements.txt`.
3. Run  `make start-elasticsearch` to spin up the docker container hosting elasticsearch.
4. Run `make start-loki` to set up Grafana connection.
5. Run `make run` to run the logging script in `monitoring.py` and launch the RAG app (`app.py`).
6. Optionally, run `make test` to test the connection with the flask backend using the default test case.
7. Go to http://localhost:5000 to interact with the RAG app through the web UI. Alternatively, you can query the endpoint directly, e.g. by running curl commands in the bash terminal:<br>
`curl -X POST http://localhost:5000/query
     -H "Content-Type: application/json"
     -d '{"query": "any laptop"}'`
8. Log in to Grafana on http://localhost:3000 and create a new data source with Loki (that connects with http://localhost:3100). Go to the Explore tab, set "Label filters" to "logger=monitoring", and click "Run query" to view all queries to the app. 

