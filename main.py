from rich.table import Table
from rich.console import Console
import os
import sqlite3
from sqlite3 import Error
from colorama import Fore
from colored import fg, attr
from datetime import date, datetime
# =============================================
con = sqlite3.connect("data.db")
os.system("cls")
# =============================================
def sql_connection(con):
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS ManagerBuy(Id INTEGER PRIMARY KEY AUTOINCREMENT,Price INTEGER, Product_Name TEXT, Date TEXT, Time TEXT)")
    con.commit()
# =============================================
def help_list():
    print(f"""{fg(50)}
███    ███  █████  ███    ██  █████   ██████  ███████ ██████      ██████  ██    ██ ██    ██ 
████  ████ ██   ██ ████   ██ ██   ██ ██       ██      ██   ██     ██   ██ ██    ██  ██  ██  
██ ████ ██ ███████ ██ ██  ██ ███████ ██   ███ █████   ██████      ██████  ██    ██   ████   
██  ██  ██ ██   ██ ██  ██ ██ ██   ██ ██    ██ ██      ██   ██     ██   ██ ██    ██    ██    
██      ██ ██   ██ ██   ████ ██   ██  ██████  ███████ ██   ██     ██████   ██████     ██   {fg(50)}
{fg(115)}===========================================================================================
**                                 Github : erfanbanaei                                  **
**                                 Twitter: @erfan_banaei                                **
**                                 YouTube: @Hero_Code                                   **
==========================================================================================={fg(115)}{attr(0)}                                                                

[{fg(50)}1{fg(50)}{attr(0)}] Init 
[{fg(50)}2{fg(50)}{attr(0)}] Add
[{fg(50)}3{fg(50)}{attr(0)}] Show
[{fg(50)}4{fg(50)}{attr(0)}] Edit
[{fg(50)}5{fg(50)}{attr(0)}] Delete
[{fg(50)}6{fg(50)}{attr(0)}] Help
[{fg(50)}7{fg(50)}{attr(0)}] Exit 
""")
# =============================================


def add(con):
    Price = int(
        input(f"[{fg(9)}?{fg(9)}{attr(0)}]Enter your purchase price : "))
    Product_Name = input(
        f"[{fg(9)}?{fg(9)}{attr(0)}] Enter your purchase name : ")
    t = datetime.now().time()
    time = f"{t.hour}:{t.minute}"
    date2 = date.today()
    full = (Price, Product_Name, date2, time)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO ManagerBuy(Price, Product_Name, Date, Time) VALUES(?,?,?,?)", full)
    con.commit()
    os.system("cls")
# =============================================
def show(con):
    cur = con.cursor()
    cur.execute('SELECT * FROM ManagerBuy')
    rows = cur.fetchall()
    console = Console()
    table = Table(title="ManagerBuy")

    table.add_column("Id", justify="center", style="cyan")
    table.add_column("Price", justify="center", style="magenta")
    table.add_column("Product Name", justify="center", style="green")
    table.add_column("Date", justify="center", style="yellow")
    table.add_column("Time", justify="center", style="blue")

    for row in rows:
        table.add_row(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]))
    console.print(table)
# =============================================
def edit(con):
    try: 
        data_id = int(input(f"[{fg(9)}?{fg(9)}{attr(0)}]Enter the ID of the product you want : "))
        new_name  = input(f"[{fg(9)}?{fg(9)}{attr(0)}]Enter the new name of the desired product : ")
        new_price = input(f"[{fg(9)}?{fg(9)}{attr(0)}]Enter the new price of the product you want :")
        full = (new_price,new_name,data_id)
        cur = con.cursor()
        cur.execute(f"UPDATE ManagerBuy SET Price = ?, Product_Name = ? WHERE Id = ?",full)
        con.commit()
    except Error as e:
        print(Fore.RED+ "Error" , e)
# =============================================
def delete_record(con):
    data_id = input(f"[{fg(9)}?{fg(9)}{attr(0)}]Enter the ID of the product you want (9999 => Remove all products) : ")
    cur = con.cursor()
    full = (int(data_id))
    if full == 9999:
        cur.execute(f"DELETE FROM ManagerBuy")
        con.commit()
        print(Fore.GREEN + "Removed all\n\n")
    else:
        cur.execute(f"DELETE FROM ManagerBuy WHERE Id = {full}")
        con.commit()
        print(Fore.GREEN + "Deleted Product\n\n")
# =============================================
def Help():
    print(f"""
Init {fg(50)}=>{fg(50)} {fg(115)}Create Database{fg(115)}{attr(0)}
Add {fg(50)}=>{fg(50)} {fg(115)}Add to Database(Price , Product Name){fg(115)}{attr(0)}
Show {fg(50)}=>{fg(50)} {fg(115)}Show all products{fg(115)}{attr(0)}
Edit {fg(50)}=>{fg(50)} {fg(115)}Product edit{fg(115)}{attr(0)}
Delete {fg(50)}=>{fg(50)} {fg(115)}Remove the product from the list{fg(115)}{attr(0)}
\n\n""")
# =============================================
while True:
    help_list()
    number = input(Fore.CYAN+"┌─["+Fore.LIGHTGREEN_EX+"ManagerBuy"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.CYAN+"""]
└──╼ """+Fore.WHITE+"$ ")
# =============================================
    if number == "1":
        os.system("cls")
        sql_connection(con)
        print(Fore.GREEN + "Created Database\n\n")
# =============================================
    elif number == "2":
        os.system("cls")
        add(con)
# =============================================
    elif number == "3":
        os.system("cls")
        show(con)
# =============================================
    elif number == "4":
        os.system("cls")
        edit(con)
# =============================================
    elif number == "5":
        os.system("cls")
        delete_record(con)
# =============================================
    elif number == "6":
        os.system("cls")
        Help()
# =============================================
    elif number == "7":
        quit()