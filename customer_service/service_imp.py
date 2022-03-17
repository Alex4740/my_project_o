from customer_service.service_interface import CustomerServiceInterface
from entities.customer_class import Customer


class CustomerServiceImp(CustomerServiceInterface):
    def service_create_customer_record(self, customer: Customer) -> Customer:
        pass

    def service_delete_customer_record(self, customer_id: int) -> bool:
        pass