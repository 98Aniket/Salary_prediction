from flask import Flask, render_template, jsonify, render_template_string,request
import config
from Salary_Data.utils import Salary_prediction

app = Flask(__name__)


@app.route('/')     # Home API

def hello_flask():
    print('Welcome to Data Science')
    return 'asdf'

@app.route('/Salary_predict')

def Salary_predicted():
    Gender = 'male'
    Age    = 27
    PhD    = 'yes'

    Salary_pred = Salary_prediction(Gender,Age,PhD)
    Salary = Salary_pred.get_pred_salary()
    
    
    return jsonify({'Result':f'Predicted Salary is{Salary}'})


if __name__ == '__main__':
    app.run()   

