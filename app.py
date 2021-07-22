from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

from maths.basic_calcuations import BasicCalculation


parser = reqparse.RequestParser()
parser.add_argument('first_num',type=int, default = 0)
parser.add_argument('second_num', type=int, default = 0)


class CalculationController(Resource):

    def get(self):
        args = parser.parse_args()
        first_num = args['first_num']
        second_num = args['second_num']
        calculation = BasicCalculation(first_num, second_num)
        
        return {"title":f"Basic calculations with {first_num} and {second_num}",
        "add_rslt": calculation.addition(),
        "subs_rslt": calculation.substract(),
        "multi_rslt": calculation.multiply(),
        "div_rslt": calculation.divide()} 

def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(CalculationController, '/calculation')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)