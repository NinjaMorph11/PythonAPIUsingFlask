from flask import Flask, request, jsonify

# jsonify is to creare a JSON Response
app = Flask(__name__)

# Route is an endpoint which is  location our our API


@app.route("/")  # Default root location
def home():
    return "Home"


@app.route('/data', methods=['POST'])
def process_data():
    data = request.json
    # Process the data
    return jsonify({'message': 'Data processed successfully'})

# Create HTTP which are other methods to connect on the internet. Among them are GET, POST, PUT & DELETE
# GET is to request data from a specified resource
# POST is to create  a resource
# PUT is to update a resource
# DELETE is to delete a resource

# Path parameter where we can give a URL


@app.route("/get-user/<user_id>")
def get_user(user_id, name_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200  # 200 Is the default status code of Success


# The methods arguments is for us to able to accept a POST request
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(), 201
    # if request.method == "POST"

# Receive data from request that id in JSON format


# Running our flask server
if __name__ == "__main__":
    app.run(debug=True)

# Run this and enter the url.
