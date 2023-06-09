import mysql.connector
import json
from flask import make_response
class user_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user="root",password="",database="flask_task")
            self.con.autocommit=True 
            self.cur = self.con.cursor(dictionary=True)
        except Exception as e:
            print(e)

    def user_getall_model(self):
        self.cur.execute("select * from user")
        data = self.cur.fetchall()
        print(data)
        if len(data) > 0:
            res = make_response({"payload":data},)
            res.headers['Access-Control-Allow-Origin'] = "*"
            return res
        else:
            return make_response({"message":"No Data Found"},)
        # return {"payload":data} if len(data) > 0 else {"message":"Something Goes wrong"}
    def user_add_model(self,data):
        self.cur.execute(f"INSERT INTO user (name,email,phone,role,password) VALUES ('{data.get('name')}','{data.get('email')}','{data.get('phone')}','{data.get('role')}','{data.get('password')}')")
        print(data.get('email'))

        return "add user "

    def user_update_model(self,data):
        self.cur.execute(f"UPDATE user SET name='{data.get('name')}',email='{data.get('email')}',phone='{data.get('phone')}',role='{data.get('role')}',password='{data.get('password')}' WHERE id='{data.get('user_id')}'")
        return"User updated." if self.cur.rowcount > 0 else "user update fail"

    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM user WHERE id='{id}'")
        return"User Deleted." if self.cur.rowcount > 0 else "Something goes wrong."

    def user_patch_model(self,id,data):
        qry = "UPDATE user SET"
        print(data)
        for i in data:
            qry += f"{i}={data[i]}"
            # print(f"{i}={data[i]}")
        print(qry) 
        return qry

        # return "This is user patch method"
        # self.cur.execute(f"UPDATE user SET name='{data.get('name')}',email='{data.get('email')}',phone='{data.get('phone')}',role='{data.get('role')}',password='{data.get('password')}' WHERE id='{data.get('user_id')}'")
        # self.cur.execute(f"DELETE FROM user WHERE id='{id}'")
        # return"User Deleted." if self.cur.rowcount > 0 else "Something goes wrong."


