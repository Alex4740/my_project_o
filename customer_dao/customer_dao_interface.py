from abc import ABC, abstractmethod

from entities.customer_class import Customer


class CustomerDAOInterface(ABC):

    @abstractmethod
    def create_customer_record(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def delete_customer_record(self, customer_id: int) -> bool:
        pass




