
from customer_dao.customer_dao_interface import CustomerDAOInterface
from entities.connection_module import connection
from entities.customer_class import Customer
from entities.nothing_deleted import NothingDeleted


class CustomerDAOImp(CustomerDAOInterface):

    def create_customer_record(self, customer: Customer) -> Customer:
        sql = "insert into customers values(default, %s, %s) returning customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name))
        connection.commit()
        returned_id = cursor.fetchone()[0]
        customer.customer_id = returned_id
        return customer

    def delete_customer_record(self, customer_id: int) -> bool:
        sql = "delete from customers where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        if cursor.rowcount != 0:
            return True
        else:
            raise NothingDeleted("no customer with the given ID")


