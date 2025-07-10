from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from predict import DonorAvailabilityPredictor

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return {"message": "Welcome to JeevaAI Backend v.0.0.1"}

api = Api(app, version='1.0', title="JeevaAI", description="JeevaAI API(s)", doc="/docs")
ns = api.namespace("jeevaAI", description="Blood Donor Prediction & AI Care ChatBot")

code_model = api.model("DonorData", {
    "region": fields.String(required=True, description="Region of the donor"),
    "days_since_last_donation": fields.Integer(required=True, description="Days since last blood donation"),
    "willing_to_donate": fields.Integer(required=True, description="Willing to donate again (1 for Yes, 0 for No)")
})


@ns.route("/predict")
class DonorPredictor(Resource):
    @ns.expect(code_model)
    def post(self):
        data = request.get_json()
        required_fields = ["region", "days_since_last_donation", "willing_to_donate"]
        
        for field in required_fields:
            if field not in data:
                return {"error": f"Missing field: {field}"}, 400

        region = data["region"]
        days = data["days_since_last_donation"]
        willing = data["willing_to_donate"]

        try:
            predictor = DonorAvailabilityPredictor()
            result = predictor.predict_availability(region, days, willing)
        except Exception as e:
            return {"error": f"Prediction failed: {str(e)}"}, 500

        return result, 200

if __name__ == "__main__":
    app.run(debug=True, port=8000)
