
from flask import Flask, request, jsonify

from customer_dao.customer_dao_imp import CustomerDAOImp
from customer_service.service_imp import CustomerServiceImp
from entities.customer_class import Customer
from entities.nothing_deleted import NothingDeleted
from exceptions.bad_customer_info import BadCustomerInfo

app: Flask = Flask(__name__)

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)


@app.route("/customer", methods=["POST"])
def create_customer_record():
    try:
        customer_info = request.get_json()
        customer = Customer(
            customer_info["customerId"],
            customer_info["firstName"],
            customer_info["lastName"]
        )
        returned_customer = customer_service.service_create_customer_record(customer)
        dictionary_customer = returned_customer.customer_to_dictionary()
        customer_json = jsonify(dictionary_customer)
        return customer_json, 201
    except BadCustomerInfo as e:
        return_massage = {
            "massage": str(e)
        }
        return jsonify(return_massage), 404


@app.route("/customer/<customer_id>", methods=["DELETE"])
def delete_customer_record(customer_id: str):
    try:
        result = customer_service.service_delete_customer_record(customer_id)
        message = {"result": result}
        return jsonify(message), 200
    except BadCustomerInfo as e:
        return_message = {
            "message": str(e)
        }
    except NothingDeleted as e:
        return_message = {
            "message": str(e)
        }
        return jsonify(return_message), 404


app.run()
