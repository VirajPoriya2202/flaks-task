from app import app
from model.user_model import user_model
from flask import request
obj = user_model()
from datetime import datetime
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


@app.route("/user/getall/limit/<limit>/page/<page>",methods=["GET"])
def user_pagination_controller(limit,page):
    return obj.user_pagination_model(limit,page)

@app.route("/user/<uid>/upload/avatar",methods=["PUT"])
def user_upload_avatar_controller(uid):
    file = request.files['avatar']

    # file.save(f"uploads/{file.filename}")
    # return str(datetime.now().timestamp()).replace(".","")
    u_name = str(datetime.now().timestamp()).replace(".","")
    file_name = file.filename.split(".")
    ext =  file_name[len(file_name)-1]
    final_name = f"uploads/{u_name}.{ext}"
    file.save(final_name)
    return obj.user_upload_avatar_model(uid,final_name)