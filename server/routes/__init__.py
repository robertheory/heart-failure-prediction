from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_cors import CORS
from schemas.predict import PredictInput
from model import Preprocessor, Pipeline
from utils import convert_input_to_model_format, load_model

# API Info
info = Info(
    title="Heart Failure Prediction API",
    version="1.0.0",
    description="API for predicting heart failure using machine learning",
)

# Initialize Flask app with OpenAPI
app = OpenAPI(__name__, info=info)
CORS(app)

# API Tags
home_tag = Tag(
    name="Docs",
    description="Documentation selection: Swagger, Redoc or ReDoc"
)


@app.get('/', tags=[home_tag])
def home():
    """Redirect to /openapi, screen that allows choosing the documentation style."""
    return redirect('/openapi/swagger')


predict_tag = Tag(
    name="Predict",
    description="Predict heart disease"
)


@app.post(
    '/predict',
    tags=[predict_tag],
    summary="Predict heart disease",
)
def predict(body: PredictInput):
    """
    Predict heart disease based on input data.
    """

    preprocessor = Preprocessor()
    pipeline = Pipeline()

    X_input = preprocessor.prepare_form(body)

    print(f"Input data for prediction: {X_input}")

    model_path = './ml/heart_disease_model.pkl'

    model = pipeline.load_pipeline(model_path)

    prediction = model.predict(X_input)

    return {"heart_disease": bool(prediction[0])}
