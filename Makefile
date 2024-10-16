install:
	pip install -r requirements.txt

run:
	python monitoring.py
	python app.py

test:
	pytest test.py

start-elasticsearch:
	docker run -it \
		--rm \
		--name elasticsearch \
		-p 9200:9200 \
		-p 9300:9300 \
		-e "discovery.type=single-node" \
		-e "xpack.security.enabled=false" \
		docker.elastic.co/elasticsearch/elasticsearch:8.4.3

start-loki:
	cd loki && docker-compose -f docker-compose.yaml up

lint:
	flake8

format:
	black .