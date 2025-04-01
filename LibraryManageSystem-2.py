class Book:
    def __init__(self, book_id, author, name, price, rack_no, status, edition, date_of_purchase):
        self.book_id = book_id
        self.author = author
        self.name = name
        self.price = price
        self.rack_no = rack_no
        self.status = status
        self.edition = edition
        self.date_of_purchase = date_of_purchase

    def display_book_details(self):
        print(f'Book ID: {self.book_id}, Name: {self.name}, Author: {self.author}, Status: {self.status}')

    def update_status(self, new_status):
        self.status = new_status
        print(f'Book Status Updated To {self.status}')

class Journals(Book):
    def __init__(self, book_id, author, name, price, rack_no, status, edition, date_of_purchase, issue_frequency):
        super().__init__(book_id, author, name, price, rack_no, status, edition, date_of_purchase)
        self.issue_frequency = issue_frequency  

    def display_book_details(self):
        super().display_book_details()
        print(f'Issue Frequency: {self.issue_frequency}')

class Magazines(Book):
    def __init__(self, book_id, author, name, price, rack_no, status, edition, date_of_purchase, genre):
        super().__init__(book_id, author, name, price, rack_no, status, edition, date_of_purchase)
        self.genre = genre  

    def display_book_details(self):
        super().display_book_details()
        print(f'Genre: {self.genre}')

class StudyBook(Book):
    def __init__(self, book_id, author, name, price, rack_no, status, edition, date_of_purchase, subject):
        super().__init__(book_id, author, name, price, rack_no, status, edition, date_of_purchase)
        self.subject = subject  

    def display_book_details(self):
        super().display_book_details()
        print(f'Subject: {self.subject}')

class MemberRecord:
    def __init__(self, member_id, member_type, date_of_membership, no_book_issued, max_book_limit, name, address, phone_no):
        self.member_id = member_id
        self.member_type = member_type
        self.date_of_membership = date_of_membership
        self.no_book_issued = no_book_issued
        self.max_book_limit = max_book_limit
        self.name = name
        self.address = address
        self.phone_no = phone_no

    def retrieve_member(self):
        return f'Member ID: {self.member_id}, Name: {self.name}, Type: {self.member_type}'

    def paybill(self, bill):
        print(f'Bill of Amount {bill.amount} Paid')

class Student(MemberRecord):
    def __init__(self, member_id, member_type, date_of_membership, no_book_issued, max_book_limit, name, address, phone_no, courses_enrolled):
        super().__init__(member_id, member_type, date_of_membership, no_book_issued, max_book_limit, name, address, phone_no)
        self.courses_enrolled = courses_enrolled  

    def display_student_info(self):
        print(f'Student Name: {self.name}, Courses Enrolled: {", ".join(self.courses_enrolled)}')

class Faculty(MemberRecord):
    def __init__(self, member_id, member_type, date_of_membership, no_book_issued, max_book_limit, name, address, phone_no, department):
        super().__init__(member_id, member_type, date_of_membership, no_book_issued, max_book_limit, name, address, phone_no)
        self.department = department  

    def display_faculty_info(self):
        print(f'Faculty Name: {self.name}, Department: {self.department}')

class Transaction:
    def __init__(self, trans_id, member, book, date_of_issue, due_date):
        self.trans_id = trans_id
        self.member = member
        self.book = book
        self.date_of_issue = date_of_issue
        self.due_date = due_date

    def create_transaction(self):
        print(f'{self.member.member_type}: {self.member.name} (ID: {self.member.member_id}) purchased a Book: "{self.book.name}" (ID: {self.book.book_id})')

class Bill:
    def __init__(self, bill_no, date, member, amount):
        self.bill_no = bill_no
        self.date = date
        self.member = member
        self.amount = amount

    def bill_create(self):
        print(f'Bill {self.bill_no} created for member {self.member.name} with amount {self.amount}')

class Librarian:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def issue_book(self, transaction):
        transaction.create_transaction()

faculty1 = Faculty(1, "Faculty", "28/03/2025", 0, 5, "Sam", "Delhi", "9876543210", "Computer Science")
student1 = Student(2, "Student", "15/01/2024", 0, 3, "Alex", "Mumbai", "9876543211", ["Math", "Physics"])

magazine1 = Magazines(101, "Author X", "The Revival", 200, "B1", "Available", "2nd Edition", "20/02/2025", "Technology")
journal1 = Journals(102, "Author Y", "Science Weekly", 150, "C1", "Available", "1st Edition", "15/01/2025", "Monthly")
studybook1 = StudyBook(103, "Author Z", "Advanced Math", 300, "D1", "Available", "3rd Edition", "10/03/2025", "Mathematics")

transaction1 = Transaction(1001, faculty1, magazine1, "22/02/2025", "27/02/2025")
bill1 = Bill(2001, "27/02/2025", faculty1, 50)
librarian = Librarian("Wilson", "Pass11225")

librarian.issue_book(transaction1)
bill1.bill_create()
faculty1.paybill(bill1)

student1.display_student_info()
faculty1.display_faculty_info()

magazine1.display_book_details()
journal1.display_book_details()
studybook1.display_book_details()
