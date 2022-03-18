from abc import ABC, abstractmethod

from entities.account_class import Account


class AccountDAOInterface(ABC):

    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    # read
    @abstractmethod
    def select_account_by_account_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def select_all_accounts_by_customer_id(self, customer_id: int) -> list[Account]:
        pass

    # update
    @abstractmethod
    def update_account_by_account_id(self, account: Account) -> Account:
        pass

    @abstractmethod
    def transefer(self, sender_id: int, reciever_id: int, amount: float) -> bool:
        pass

    # delete
    @abstractmethod
    def delete_account_by_account_id(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def delete_all_customer_accounts(self, customer_id: int) -> bool:
        pass
