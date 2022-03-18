from customer_dao.customer_dao_imp import CustomerDAOImp
from customer_service.service_imp import CustomerServiceImp
from entities.customer_class import Customer
from exceptions.bad_customer_info import BadCustomerInfo

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)

"""
create service
"""


def test_catch_non_string_first_name():
    try:
        customer = Customer(0, 40, "Tome")
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Invalid customer information, please try again"


def test_catch_non_string_last_name():
    try:
        customer = Customer(0, "Bab", 40)
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Invalid customer information, please try again"


def test_first_name_too_long():
    try:
        customer = Customer(0, "the longest name ever in the world", "Tom")
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Invalid customer information, please try again"


def test_last_name_too_long():
    try:
        customer = Customer(0, "Bab", "the longest name ever in the world")
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Invalid customer information, please try again"


"""
delete service test
"""


def test_catch_invalid_id():
    try:
        customer_service.service_delete_customer_record("one")
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Invalid customer information, please try again"
