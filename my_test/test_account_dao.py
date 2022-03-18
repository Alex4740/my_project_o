from account_dao.Account_dao_imp import AccountDAOImp
from entities.account_class import Account

from exceptions.bad_account_info import BadAccountInfo

account_dao = AccountDAOImp()


def test_create_account_success():
    account = Account(0, -1, 500.00)
    result = account_dao.create_account(account)
    assert result.account_id != 0


def test_create_account_with_bad_id():
    account = Account("zero", -2, 500.00)
    result = account_dao.create_account(account)
    assert result.account_id != 0


def test_select_account_by_account_id_success():
    result = account_dao.select_account_by_account_id(-1)
    assert result.account_id == -1


def test_select_account_by_id_doesnt_exist():
    try:
        account_dao.select_account_by_account_id(-1000)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "No account with Id"


def test_select_all_account_by_customer_id_success():
    accounts = account_dao.select_all_accounts_by_customer_id(-3)
    assert len(accounts) >= 2


def test_select_all_accounts_by_customer_no_accounts_found():
    try:
        account_dao.select_all_accounts_by_customer_id(-1000)
        assert False

    except BadAccountInfo as e:
        assert str(e) == "No account with Id"


# update

def test_update_account_by_id_success():
    new_info = Account(-4, -3, 600.00)
    result = account_dao.update_account_by_account_id(new_info)
    assert result.account_balance == 600.00


def test_update_account_by_id_account_not_found():
    try:
        new_info = Account(-1000, -3, 600.00)
        account_dao.select_all_accounts_by_customer_id(new_info)
        assert False

    except BadAccountInfo as e:
        assert str(e) == "No account with Id"


def test_transfer_success():
    result = account_dao.transefer(-5, -6, 100.00)
    assert result


def test_transfer_sender_account_non_existant():
    try:
        account_dao.transefer(-1000, -6, 100.00)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "Sender account id not found"


def test_transfer_receiver_account_non_existant():
    try:
        account_dao.transefer(-5, -600, 100.00)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "Reciver account id not found"


def delete_account_by_id_success():
    result = account_dao.delete_account_by_account_id(-7)
    assert result

def test_delete_account_by_id_no_account_found():
    try:
        account_dao.delete_account_by_account_id(-1000)
        assert False
    except BadAccountInfo as e:
        assert str(e) == "No account with that Id found"
