from functions_passenger import *
from functions_driver import *
from functions_status import *
from functions_order import *

level = 0
cur_header = -1

headers = ["passenger", 'driver', "status", "order"]

queries = ["create", "update", "delete", "get", "get_all", "back"]

while True:
    if (level == 0):
        print("Choose table")
        print('Passenger/Driver/Status/Order')
        type = input()
        type = type.lower()
        if (type in headers):
            cur_header = type
            level += 1
    if level == 1:
        print("Choose query")
        print('Create/Update/Delete/Get/Get_all/Back')
        type = input()
        type = type.lower()
        if (type not in queries):
            continue
        if type == "back":
            level -= 1
        if (cur_header == "passenger"):
            if type == "create":
                print("Enter name")
                name = input()
                print(create_passenger(name))
            if type == "update":
                print("Enter id & name")
                id = int(input())
                name = input()
                print(update_passenger(id,name))
            if type == "delete":
                print("Enter id")
                id = int(input())
                print(delete_passenger(id))
            if type == "get":
                print("Enter id & name (optional)")
                name = input()
                print(get_passenger(name))
            if type == "get_all":
                print(get_all_passengers())
        if (cur_header == "driver"):
            if type == "create":
                print("Enter sign & name")
                sign = input()
                name = input()
                print(create_driver(sign,name))
            if type == "update":
                print("Enter id & sign & name")
                id = int(input())
                sign = input()
                name = input()
                print(update_driver(id,sign,name))
            if type == "delete":
                print("Enter id")
                id = int(input())
                print(delete_driver(id))
            if type == "get":
                print("Enter id & sign & name (optional)")
                sign = input()
                name = input()
                print(get_driver(sign,name))
            if type == "get_all":
                print(get_all_drivers())
        if (cur_header == "status"):
            if type == "create":
                print("Enter name")
                name = input()
                print(create_status(name))
            if type == "update":
                print("Enter id & name")
                id = int(input())
                name = input()
                print(update_status(id,name))
            if type == "delete":
                print("Enter id")
                id = int(input())
                print(delete_status(id))
            if type == "get":
                print("Enter id & name (optional)")
                name = input()
                print(get_status(name))
            if type == "get_all":
                print(get_all_statuses())
        if (cur_header == "order"):
            if type == "create":
                print("Enter adress1 & adress2 & driver & passenger & status")
                adress1 = input()
                adress2 = input()
                driver = input()
                passenger = input()
                status = input()
                print(create_order(adress1,adress2,driver,passenger,status))
            if type == "update":
                print("Enter id & adress1 & adress2 & driver & passenger & status")
                id = int(input())
                adress1 = input()
                adress2 = input()
                driver = input()
                passenger = input()
                status = input()
                print(update_order(id,adress1,adress2, driver,passenger,status))
            if type == "delete":
                print("Enter id")
                id = int(input())
                print(delete_order(id))
            if type == "get":
                print("Enter id & adress1 & adress2 & driver & passenger & status (optional)")
                adress1 = input()
                adress2 = input()
                driver = input()
                passenger = input()
                status = input()
                print(get_order(adress1,adress2,driver,passenger,status))
            if type == "get_all":
                print(get_all_orders())