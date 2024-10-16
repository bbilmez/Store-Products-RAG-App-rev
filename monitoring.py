import logging
from flask import request
from logging_loki import LokiHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Loki configuration
loki_handler = LokiHandler(
    url="http://localhost:3100/loki/api/v1/push",  # Adjust the URL to your Loki instance
    tags={"application": "flask-app"},
    version="1",
)
logger.addHandler(loki_handler)


def log_request():
    if request.content_type == "application/json":
        logger.info(
            f"Request: {request.method} {request.url} - Body: {request.get_json()}"
        )
    else:
        logger.info(f"Request: {request.method} {request.url} - Body: Non-JSON request")


def log_response(response):
    try:
        response_data = response.get_data(as_text=True)
    except RuntimeError:
        response_data = "Response data not available (passthrough mode)"
    logger.info(f"Response: {response.status_code} - Body: {response_data}")
    return response
