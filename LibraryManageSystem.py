class Book:
    def __init__(self,book_id,author,name,price,rack_no,status,edition,date_of_purchase):
        self.book_id = book_id
        self.author = author
        self.name = name
        self.price = price
        self.rack_no = rack_no
        self.status = status
        self.edition = edition
        self.date_of_purchase = date_of_purchase
   
    def display_book_details(self):
        print(f"Book ID: {self.book_id}, Name: {self.name}, Author: {self.author}, Status: {self.status}")
  
    def update_status(self,new_status):
        self.staus = new_status
        print(f"Book Status Updated To {self.status}")
       
class Librarian:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        
    def search_book(self,book):
        book.display_book_details()
        
    def verify_member(self,member):
        print(f"Verifying Member: {member.name}")
    
    def issue_book(self,transaction):
        print(f"Issuing Book {transaction.book_id} To Member {transaction.member_id}")
        
    def create_bill(self,bill):
        print(f"Bill created with amount: {bill.amount}")
        
    def return_book(self,transaction):
        print(f"Book {transaction.book_id} returned by member{transaction.member_id}")
        
class Transaction:
    def __init__(self,trans_id,member_id,book_id,date_of_issue,due_date):
        self.trans_id = trans_id
        self.member_id = member_id
        self.book_id = book_id
        self.date_of_issue = date_of_issue
        self.due_date = due_date
        
    def create_transaction(self):
        print(f"Transaction {self.trans_id} created for book {self.book_id}")
        
    def delete_transaction(self):
        print(f"Transaction {self.trans_id} Deleted!!")
        
    def retrieve_transaction(self):
        print(f"Transaction {self.trand_id} Retrieved!!")
        
class MemberRecord:
    def __init__(self,member_id,member_type,date_of_membership,no_book_issued,max_book_limit,name,address,phone_no):
        self.member_id = member_id
        self.member_type = member_type
        self.date_of_membership = date_of_membership
        self.no_book_issued = no_book_issued
        self.max_book_limit = max_book_limit
        self.name = name
        self.address = address
        self.phonr_no = phone_no
        
    def retrieve_member(self):
        print(f"Member ID: {self.member_id}, Name: {self.name}, Type: {self.member_type}")
        
    def paybill(self,bill):
        print(f"Bill of Amount {bill.amount} Paid")
        
class Bill:
    def __init__(self,bill_no,date,member_id,amount):
        self.bill_no = bill_no
        self.date = date
        self.member_id = member_id
        self.amount = amount
        
    def bill_create(self):
        print(f"Bill {self.bill_no} created for member {self.member_id} with amount {self.amount}")
        
    def bill_update(self):
        print(f"Bill {self.bill_no} updated with new amount {self.amount}")
        
member1 = MemberRecord(1, "student", "28/03/2025", 0, 5, "Sumith", "Hyderabad", "9876543210")
book1 = Book(101, "JK Rowling", "Harry Potter Vol-2", 500, "A1", "Available", "1st Edition", "22/02/2025")
transaction1 = Transaction(1001, 1, 101, "22/02/2025", "27/02/2025")
bill1 = Bill(2001, "27/02/2025", 1, 50)
librarian = Librarian("Alice", "Pass11225")

librarian.issue_book(transaction1)
librarian.create_bill(bill1)
bill1.bill_create()  
member1.paybill(bill1)
