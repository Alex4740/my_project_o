from account_dao.account_dao_interface import AccountDAOInterface
from entities.account_class import Account


class AccountDAOImp(AccountDAOInterface):

    def create_account(self, account: Account) -> Account:
        pass

    def select_account_by_account_id(self, account_id: int) -> Account:
        pass

    def select_all_accounts_by_customer_id(self, customer_id: int) -> list[Account]:
        pass

    def update_account_by_account_id(self, account: Account) -> Account:
        pass

    def transefer(self, sender_id: int, reciever_id: int, amount: float) -> bool:
        pass

    def delete_account_by_account_id(self, account_id: int) -> bool:
        pass

    def delete_all_customer_accounts(self, customer_id: int) -> bool:
        pass
