import configparser
import json
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# ---------------------------
# MongoDB Connection
# ---------------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["devops_config"]
collection = db["configs"]

# ---------------------------
# Read config.ini and store in MongoDB
# ---------------------------
def read_config_and_store():
    try:
        config = configparser.ConfigParser()
        config.read("config.ini")

        data = {}

        for section in config.sections():
            data[section] = dict(config[section])

        # Clear old config and insert new
        collection.delete_many({})
        collection.insert_one(data)

        print("Configuration stored successfully in MongoDB")

    except Exception as e:
        print("Error:", e)

# ---------------------------
# API Endpoint
# ---------------------------
@app.route("/config", methods=["GET"])
def get_config():
    doc = collection.find_one({}, {"_id": 0})
    if doc:
        return jsonify(doc)
    else:
        return jsonify({"error": "No config found"}), 404


# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    read_config_and_store()
    app.run(port=5000)
