import json
import pickle
import re
import numpy as np
import config


class Salary_prediction():
    def __init__(self,Gender,Age,PhD):
        self.Gender = Gender
        self.Age    = Age
        self.PhD    = PhD


    def load_model(self):
        with open(config.PKL_FILE_PATH,'rb') as f:
            self.PKL = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.JSON = json.load(f)


    def get_pred_salary(self):
        self.load_model()

        test_array=np.zeros(len(self.JSON['columns']))
        test_array[0] = self.JSON['Gender'][self.Gender]
        test_array[1] = self.Age
        test_array[2] = self.JSON['PhD'][self.PhD]

        predict_salary = self.PKL.predict([test_array])
        return predict_salary


if __name__ =='__main__':
    Gender = 'male'
    Age    = 27
    PhD    = 'yes'
    Salary_pred = Salary_prediction(Gender,Age,PhD)
    Salary_pred.get_pred_salary()

