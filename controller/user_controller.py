from app import app
from model.user_model import user_model
from flask import request
obj = user_model()

@app.route("/user/")
def user_singup_controller():
    return obj.user_getall_model()

@app.route("/user/add/",methods=["POST"])
def user_add_controller():
    print(request.form)
    return obj.user_add_model(request.form)

@app.route("/user/update/",methods=["PUT"])
def user_update_controller():
    return obj.user_update_model(request.form)

@app.route("/user/delete/<id>",methods=["DELETE"])
def user_delete_controller(id):
    return obj.user_delete_model(id)


@app.route("/user/patch/<id>",methods=["PATCH"])
def user_patch_controller(id):
    return obj.user_patch_model(id,request.form)