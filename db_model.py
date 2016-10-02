"""
    Connect to a vertica database and run queries
"""
from flask import g
from cli import *

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_db()
        db.cursor().execute('set search_path to team11_schema, "$user", public;')
    return db

def available_items():
    """
        Select 1 from database
    """
    sql = "SELECT * FROM items where available = 'true'"
    results = query_db(sql)
    print results
    return results

def search_contracts(username):
    sql = "select * from contracts inner join items using (iid) where orginial_owner = %s and approved = 'false"
    results = query_db(sql, args=(username))
    print results
    return results

def approve_contract(username, password, cid):
    sql = "select password from accounts where username = %s"
    results = query_db(sql, args=(username))
    if results == password:
        sql = "update contract set approved = 'true' where cid = %d"
        results = query_db(sql, args=(cid))
        return results
    return "Password not accepted."

def create_account(username,password,geography):
    """Create an account"""
    sql = "insert into accounts(username,password,geography,balance_owed,balance_invested) values ("\
            "%s,%s,%s,0.00,0.00);"
    results = query_db(sql, args=(username,password,geography))
    return results

def post_item(item_name,price,geography,photo,original_owner):
    """Post Item to Timeshare"""
    sql = "insert into items(item_name,price,geography,available,original_owner,photo) values ("\
           "%s,%s,%s,true,%s,%s);"
    results = query_db(sql, args=(item_name,price,geography,photo,original_owner))
    return results

def create_request(item,user,w_day,start_time,end_time):
    """Create contract with an item"""
    sql = "select count(cid) from contracts where approved = 'true' group by %d"
    results = query_db(sql, args=(item))
    if (results <= 3):
      sql = "insert into request(item,user,w_day,time_interval,approved) values (%d,%s,%s,%d,%d,false)"
      results = query_db(sql, agrs=(item,user,w_day,time_interval))
    else:
      sql = "update items set available = 'false' where iid = %d"
      results = query_db(sql, args=(item))
    return results
"""
create table accounts(
    username varchar(50) not null, 
    password varchar(50) not null,
    geography varchar(50),
    balance_owed decimal(8,2),
    balance_invested decimal(8,2),
    primary key (username));

create table items(
    iid auto_increment,
    item_name varchar(50) not null,
    price decimal(8,2),
    geography varchar(100),
    available boolean,
    original_owner varchar(50),
    primary key(iid),
    foreign key (original_owner) references accounts);

create table request(
    cid auto_increment,
    item int not null,
    owner varchar(50) not null,
    w_day varchar(50),
    start_time time,
    end_time time,
    approved boolean,
    primary key (cid),
    foreign key (item) references items,
    foreign key (owner) references accounts);
"""

# @app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
