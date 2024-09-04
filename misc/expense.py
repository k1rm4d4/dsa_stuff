class Expense:
    def __init__(self, amount: int, desc: str) -> None:
        self.amount = amount 
        self.desc = desc 

    def __repr__(self) -> str:
        return f"Expense::[Amount: {self.amount}] [Description: {self.desc}]"

    def update(self, field, value):
        self.field = value 

if __name__ == "__main__":
    e = Expense(10, "New Expense")
    print(e)
    e.update("amount", 1000)
    print(e)