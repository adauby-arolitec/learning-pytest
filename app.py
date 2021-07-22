from maths.basic_calcuations import BasicCalculation
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class CalculationController(Resource):

    def get(self, first_num:int=0, second_num:int=0):
        calculation = BasicCalculation(first_num, second_num)
        return {"add_rslt": calculation.addition(),
        "subs_rslt": calculation.substract(),
        "multi_rslt": calculation.multiply(),
        "div_rslt": calculation.divide()} 

api.add_resource(CalculationController, '/calculation')

if __name__ == '__main__':
    app.run(debug=True)