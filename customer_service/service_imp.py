from customer_service.service_interface import CustomerServiceInterface
from entities.customer_class import Customer
from exceptions.bad_customer_info import BadCustomerInfo


class CustomerServiceImp(CustomerServiceInterface):

    def service_create_customer_record(self, customer: Customer) -> Customer:
        if type(customer.first_name) != str or type(customer.last_name) != str:
            raise BadCustomerInfo("Invalid customer information, please try again")
        elif len(customer.first_name) > 20 or len(customer.last_name) > 20:
            raise BadCustomerInfo("Invalid customer information, please try again")
        else:
            return self.customer_dao.create_customer_record(customer)

    def service_delete_customer_record(self, customer_id: int) -> bool:
        try:
            return self.customer_dao.delete_customer_record(int(customer_id))

        except ValueError:
            raise BadCustomerInfo("Invalid customer information, please try again")
