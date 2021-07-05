"""
CANNR TM analytics container building tool example showing Python function that
decides whether someone can be scheduled for a hypothetical vaccine for a
hypothetical disease, based on risk factors.
Copyright 2021 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

import numpy
import math

# Cutoff for deciding that predicted mortality qualifies someone for the vaccine.
mortCutoff = 0.10

# Cutoff for deciding that predicted lost years of life qualifies someone for the vaccine.
yearsCutoff = 5

# Coefficients of a hypothetical logistic regression model for P(Death|Risk Factors)
mortCoefs = numpy.array([
    -8.68233,   # Constant
    0.08878,    # Age
    1.23936,    # Hypertension
    0.35158,    # Cardio
    1.21281,    # Pulmonary
    1.86774,    # Diabetes
    2.12715])   # Obesity

# Coefficients of a hypothetical model for expected life years remaining for someone based on their risk factors.
# Model uses a logistic function to predict expected years of life as a fraction of years left to age 100.
yearsCoefs = numpy.array([
    0.940725,   # Constant
    0.001434,   # Age
    -0.661604,  # Hypertension
    -1.012414,  # Cardio
    -1.71273,   # Pulmonary
    -0.843038,  # Diabetes
    -0.696056]) # Obesity

# Logistic function
def logistic(x):
    return math.exp(x)/(1+math.exp(x))

# Returns the predicted value from the logistic model, given the predictors (xPreds) and model parameters (params).
def logistModel(xPreds, params):
    return logistic(numpy.dot(xPreds, params))

# Model for mortality from the disease, given the person is infected.
def mortModel(xPreds):
    age = xPreds[0]
    if age >= 100 or age <= 0:
        return 0.0
    else: 
        return logistModel(numpy.append([1], xPreds), mortCoefs)

# Hypothetical model for remaining years of life, given the person's age and other risk factors.
def yearsModel(xPreds):
    age = xPreds[0]
    if age >= 100 or age <= 0:
        return 0.0
    else:
        return (100 - age)*logistModel(numpy.append([1], xPreds), yearsCoefs)


# Decides whether someone should get the vaccine, based on their risk factors:
# age - The person's age in years
# hypertension - Boolean indicating hypertension
# cardio - Boolean indicating cardiovascular disease like arteriosclerosis
# pulmonary - Boolean indicating pulmonary disease like COPD or asthma
# diabetes - Boolean indicating diabetes
# obesity - Boolean indicating obesity defined by a BMI of at least 30.0 
# 
# In addition, the boolean flag years indicates whether the decision should be
# made based on predicted lost life years (True), or just mortality (False).
# To be exposed as a service.
def vaxDecision(inputDict):
    
    # Convert the risk factors into an array (list).
    xPreds = [
        inputDict.get('age', 0.0),
        int(inputDict.get('hypertension', False)),
        int(inputDict.get('cardio', False)),
        int(inputDict.get('pulmonary', False)),
        int(inputDict.get('diabetes', False)),
        int(inputDict.get('obesity', False))
        ]
    
    # If decision is to be based on life years, calculate predicted life years
    # lost and check whether greater than cutoff.
    if inputDict.get('years', False):
        return mortModel(xPreds)*yearsModel(xPreds) >= yearsCutoff
    # Otherwise, just use mortality.
    else:
        return mortModel(xPreds) >= mortCutoff

# Sample input for vaxDecision.
# To be exposed as a service.
def sampleInput():
    return {
        'age': 50,
        'hypertension': False,
        'cardio': False,
        'pulmonary': False,
        'diabetes': True,
        'obesity': True,
        'years': True
        }


xPreds = [50, 0, 0, 0, 1, 1]

print(mortModel(xPreds))

print(yearsModel(xPreds))

print(mortModel(xPreds)*yearsModel(xPreds))

print(vaxDecision(sampleInput()))

