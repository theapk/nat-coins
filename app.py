from flask import Flask, render_template, request, jsonify
from decimal import Decimal
import json
from types import SimpleNamespace

app = Flask(__name__)


# this is a round to solve for float subtraction issue
# def round_decimals_up(number:float, decimals:int=2):
#     """
#     Returns a value rounded up to a specific number of decimal places.
#     """
#     if not isinstance(decimals, int):
#         raise TypeError("decimal places must be an integer")
#     elif decimals < 0:
#         raise ValueError("decimal places has to be 0 or more")
#     elif decimals == 0:
#         return math.ceil(number)
#
#     factor = 10 ** decimals
#     return math.ceil(number * factor) / factor


# API URL
@app.route('/change', methods=['POST'])
def make_change():
    details = request.data
    json_detail = json.loads(details, object_hook=lambda d: SimpleNamespace(**d))
    user_input = json_detail.input
    options = {
        'silver_dollar': 1.00,
        'half_dollar': 0.50,
        'quarter': 0.25,
        'dime': 0.10,
        'nickel': 0.05,
        'penny': 0.01
    }
    results = {
        'silver_dollar': 0,
        'half_dollar': 0,
        'quarter': 0,
        'dime': 0,
        'nickel': 0,
        'penny': 0
    }
    subtraction = float(user_input)
    print(subtraction)
    for k, v in options.items():
        while subtraction > 0.00:
            print(f'Subtraction Before IF: {subtraction}')
            output = Decimal(subtraction) - Decimal(v)
            if output > Decimal(0.00):
                subtraction = subtraction - v
                # print(f'Trunc: {trunc}')
                # subtraction = round_decimals_up(float(trunc), 2)
                print(f'subtrac in IF: {subtraction}')
                results[k] += 1
            else:
                break

    print(results)
    return results


@app.route('/')
def coins():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
