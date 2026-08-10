bank_accounts = {
    1010: {
        "name" : "Russel Masaoay",
        "pin": "0000",
        "balance": 5000.00,
        "transactions": [
            {"type" :"deposit", "amount": 1500, "category": "Salary", "date": "2026-05-25"},
            {"type" :"withdrawal","amount": 50, "category": "Food", "date": "2026-05-26"}
        ]
    }
}



def create_bank_account(username, pin):
    bank_randomize = (1000 + 2)* len(bank_accounts)

    new_account = {
    bank_randomize:  {
        "name" : username,
        "pin" : pin,
        "balance" : 0.00,
        "transactions": []
    }}

    bank_accounts.update(new_account)