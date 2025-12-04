from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Expose standard Prometheus metrics at /metrics
metrics = PrometheusMetrics(app)

# Static information metric for build/version tracking
metrics.info('app_info', 'Application Information', version='1.0.0')


@app.route('/')
def hello_world():
    return 'Hello, DevOps World!'


@app.route('/health')
def health():
    """Liveness probe endpoint for Kubernetes / Docker."""
    return jsonify(status='healthy'), 200


@app.route('/ready')
def ready():
    """Readiness probe endpoint for Kubernetes / load balancers."""
    return jsonify(status='ready'), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
