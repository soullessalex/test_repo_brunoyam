from pony.orm import *


db = Database()
db.bind(provider='sqlite', filename='db.sqlite', create_db=True)


class Client(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    phone = Optional(str, default="000000")
    orders = Set('Order')


class Order(db.Entity):
    id = PrimaryKey(int, auto=True)
    products = Required(str)
    client_id = Required(Client)



db.generate_mapping(create_tables=True)
sql_debug(True)

@db_session
def add_client(name, phone='0000000'):
    Client(name=name, phone=phone)

@db_session
def show_client():
    select((p.id, p.name) for p in Client).show()

@db_session
def update_client():
    clients = select(p for p in Client if p.name == 'Ivan')
    print(clients[:])
    for cl in clients[:]:
        cl.name = 'Alex'

@db_session
def delete_client(name):
    delete(p for p in Client if p.name == name)

if __name__ == "__main__":
    # add_client('Oleg')
    # show_client()
    # update_client()
    delete_client('Oleg')
    show_client()