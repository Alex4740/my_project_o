from customer_dao.customer_dao_imp import CustomerDAOImp
from entities.customer_class import Customer
from entities.nothing_deleted import NothingDeleted

customer_dao = CustomerDAOImp()


def test_create_customer_success():
    customer = Customer(0, "first_name", "last_name")
    result = customer_dao.create_customer_record(customer)
    assert result.customer_id != 0


def test_create_customer_with_malformed_id():
    # if wrong data type of id is provided the customer object the method should still work.
    customer = Customer("one", "Timmy", "Jimmy")
    result = customer_dao.create_customer_record(customer)
    assert result.customer_id != 0


def test_delete_customer_success():
    result = customer_dao.delete_customer_record(-1)
    assert True


def test_no_customer_to_delete():
    # catch no customer is deleted by the method
    try:
        customer_dao.delete_customer_record(-1)
        assert False
    except NothingDeleted as e:
        assert str(e) == "no customer with the given id"

