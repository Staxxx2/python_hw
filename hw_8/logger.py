import csv
import model
import view

def add_new(employee, id):
    try:
        with open('hw_8/book.txt', 'a', encoding='utf-8') as book:
            book.write(f'\n{employee}')
        with open('hw_8/book.csv', 'a') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows([employee.split(' || ')])
    except FileNotFoundError:
         with open('hw_8/book.txt', 'w', encoding='utf-8') as book:
            book.write(f'\n{employee}')
         with open('hw_8/book.csv', 'w') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows([employee.split(' || ')])

def get_base():
    with open('hw_8/book.txt', 'r', encoding='utf-8') as book:
        return book.read()
        
def log_csv(employee, id):
    employee = f'{id} || ' + employee
    employee = [employee.split(' || ')]
    try:
        with open('hw_8/book.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(employee)
    except FileNotFoundError:
        with open('hw_8/book.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')  
            writer.writerows(employee)  
 
def update_base(new_info):
    new_info_csv = [i.split(' || ' for i in new_info)]
    with open('hw_8/book.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
       # for row in new_info_csv:
        writer.writerows(new_info_csv)
    with open('hw_8/book.txt', 'w', encoding='utf-8') as book:
        book.write("\n".join(new_info))





# def add_new(contact):
#     try:
#         with open('book.txt', 'a', encoding='utf-8') as book:
#             book.write(f'\n{contact}')
#         with open('book.csv', 'a') as f:
#             writer = csv.writer(f, delimiter=';')
#             writer.writerows([contact.split(' || ')])
#     except FileNotFoundError:
#          with open('hw_4/book.txt', 'w', encoding='utf-8') as book:
#             book.write(f'\n{contact}')
#          with open('hw_4/book.csv', 'w') as f:
#             writer = csv.writer(f, delimiter=';')
#             writer.writerows([contact.split(' || ')])

# def get_base():
#     with open('book.txt', 'r', encoding='utf-8') as book:
#         return book.read()