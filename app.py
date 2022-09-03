from flask import Flask, current_app, jsonify, make_response

__all__ = ["create_app"]


def create_app(config=None, app_name=None, blueprints=None):
    app = Flask(__name__)

    @app.route("/")
    def hello_from_root():
        return jsonify(message="Hello from root!")

    @app.route("/hello")
    def hello():
        current_app.logger.info("Hello from path!")
        return jsonify(message="Hello from path!")

    @app.errorhandler(404)
    def resource_not_found(e):
        return make_response(jsonify(error="Not found!"), 404)

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
