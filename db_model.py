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

def create_account(username,password,geography):
    """Create an account"""
    sql = "insert into accounts(username,geography,photo,balanced_owed,balance_invested) values ("\
            + username + "," + password + ","+ geography + ",0.00,0.00);"
    results = query_db(sql)
    return results

def post_item():
    """Post Item to Timeshare"""
    sql = "insert into items(item_name,price,geography,photo,available,original_owner) values ("\
           + item_name + "," + price + "," + geography + "," + photo + ",true," + original_owner +");"
    results = query_db(sql)
    return results

def create_request():
    """Create contract with an item"""
    sql = "select count(cid) from contracts where approved = 'true' group by " + item
    results = query_db(sql)
    if (results <= 3):
      sql = "insert into request(item,user,w_day,time_interval,approved) values ("+ item + "," + user + "," + w_day + "," + time_interval + ",false)"
      results = query_db(sql)
    else:
      sql = "update items set available = 'false' where iid = " + item
      results = query_db(sql)
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
    time_interval interval,
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
