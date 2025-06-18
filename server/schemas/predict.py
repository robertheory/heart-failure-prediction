from pydantic import BaseModel, Field, conint, confloat
from typing import Literal


class PredictInput(BaseModel):
    Age: int = Field(..., ge=1, le=120,
                     description="Age of the patient in years")
    Sex: Literal['M', 'F'] = Field(...,
                                   description="Sex of the patient: M (Male), F (Female)")
    ChestPainType: Literal['TA', 'ATA', 'NAP',
                           'ASY'] = Field(..., description="Chest pain type")
    RestingBP: int = Field(..., ge=0, le=300,
                           description="Resting blood pressure (mm Hg)")
    Cholesterol: int = Field(..., ge=0, le=1000,
                             description="Serum cholesterol (mg/dl)")
    FastingBS: Literal[0, 1] = Field(
        ..., description="Fasting blood sugar: 1 if >120 mg/dl, 0 otherwise")
    RestingECG: Literal['Normal', 'ST', 'LVH'] = Field(
        ..., description="Resting electrocardiogram results")
    MaxHR: int = Field(..., ge=60, le=202,
                       description="Maximum heart rate achieved")
    ExerciseAngina: Literal['Y', 'N'] = Field(
        ..., description="Exercise-induced angina: Y (Yes), N (No)")
    Oldpeak: float = Field(..., ge=0, le=10,
                           description="Oldpeak = ST depression")
    ST_Slope: Literal['Up', 'Flat', 'Down'] = Field(
        ..., description="Slope of the peak exercise ST segment")


class ModelInput(BaseModel):
    Age: int = Field(..., ge=1, le=120,
                     description="Age of the patient in years")
    Sex: int = Field(...,
                     description="Sex of the patient: 1 (Male), 0 (Female)")
    RestingBP: int = Field(..., ge=0, le=300,
                           description="Resting blood pressure (mm Hg)")
    Cholesterol: int = Field(..., ge=0, le=1000,
                             description="Serum cholesterol (mg/dl)")
    FastingBS: int = Field(...,
                           description="Fasting blood sugar: 1 if >120 mg/dl, 0 otherwise")
    MaxHR: int = Field(..., ge=60, le=202,
                       description="Maximum heart rate achieved")
    ExerciseAngina: int = Field(...,
                                description="Exercise-induced angina: 1 (Yes), 0 (No)")
    Oldpeak: float = Field(..., ge=0, le=10,
                           description="Oldpeak = ST depression")
    ChestPainType_ASY: int = Field(
        ..., description="Chest pain type: ASY (1 if true, 0 otherwise)")
    ChestPainType_ATA: int = Field(
        ..., description="Chest pain type: ATA (1 if true, 0 otherwise)")
    ChestPainType_NAP: int = Field(
        ..., description="Chest pain type: NAP (1 if true, 0 otherwise)")
    ChestPainType_TA: int = Field(...,
                                  description="Chest pain type: TA (1 if true, 0 otherwise)")
    RestingECG_LVH: int = Field(...,
                                description="Resting ECG: LVH (1 if true, 0 otherwise)")
    RestingECG_Normal: int = Field(...,
                                   description="Resting ECG: Normal (1 if true, 0 otherwise)")
    RestingECG_ST: int = Field(...,
                               description="Resting ECG: ST (1 if true, 0 otherwise)")
    ST_Slope_Down: int = Field(...,
                               description="ST Slope: Down (1 if true, 0 otherwise)")
    ST_Slope_Flat: int = Field(...,
                               description="ST Slope: Flat (1 if true, 0 otherwise)")
    ST_Slope_Up: int = Field(...,
                             description="ST Slope: Up (1 if true, 0 otherwise)")
