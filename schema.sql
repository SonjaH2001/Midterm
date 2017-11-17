-- #database table

--find instruction or research the GUI (how to add table).
-- #-->https://superuser.com/questions/461154/easy-simple-sqlite-table-database-gui
-- #-->https://github.com/coleifer/sqlite-web
--maybe just get 2 tables to start (cookie type, customer,...)


drop table if exists cookie_type;
create table cookie_type (
  id integer primary key autoincrement,
  name text not null,
  price text not null
);

drop table if exists customer;
create table customer (
  cust_id integer primary key autoincrement,
  cust_name text not null,
  cust_address text not null
);

drop table if exists orders;
create table orders (
  order_id integer primary key autoincrement,
  cookie_id text not null,
  cust_id text not null
);
INSERT INTO cookie_type (id, name, price)
  VALUES (101,"Seasonal Sensation", 8),
    (201, "Suger Hill Gang", 6),
    (301, "Chocolate Pinky Delights", 6),
    (401, "Chocolate Chip Peanut Butter Dream", 8);


--     ())


-- ###insert cookies!!!

-- define constraints/FK PK, etc