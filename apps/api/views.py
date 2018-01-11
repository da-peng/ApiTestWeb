#encoding=utf-8
from . import api

from flask_login import (
    login_required
)
from flask import (
    jsonify,
    current_app,
    request,
    redirect,
    url_for
)
from apps.models import InterfaceDetail  as Intf

from apps import db
from apps.common.message_manager import Message

success ={
    'ret':1
}

fail ={
    'ret':0
}

@api.route('/del_inter/<int:interface_id>', methods=['POST'])
@login_required
def del_interface(interface_id):
    interface = Intf.query.filter_by(id=interface_id).first()
    name =interface.interface_name
    if name:
        db.session.delete(interface)
        db.session.commit()
        return jsonify(success)
    return jsonify(fail)


@api.route('/update_inter/<int:interface_id>', methods=['POST'])
@login_required
def update_interface(interface_id):
    print request
    result = request.json()
    print(result)
    data = {
        Intf.interface_name:result['Name'],
        Intf.interface_type: result['Type'],
        Intf.host: result['Host'],
        Intf.url: result['Url'],
        Intf.cookie: result['Cookie'],
        Intf.header: result['Header'],
        Intf.is_sign: result['Sign'],
        Intf.request_sample: result['Request_Sample'],
    }
    db.query(Intf).filter(Intf.id == interface_id).update(data)
    db.commit()
    return redirect(url_for("home.interface"))

@api.route('/add_inter', methods=['POST'])
@login_required
def add_interface():
    result = request.json

    interface = Intf(interface_name=result['name'],
                     interface_type=result['type'],
                     host = result['host'],
                     url = result['url'],
                     request_sample =result['sample']
                     )
    db.session.add(interface)
    db.session.commit()
    return jsonify(success)


@api.route('/debug_inter/<int:interface_id>', methods=['POST'])
@login_required
def debug_interface(interface_id):

    interface = Intf.query.filter_by(id=interface_id).first()


    header = interface.header
    cookie = interface.cookie
    type = interface.interface_type
    is_sign = interface.is_sign
    host = interface.host
    url = interface.url
    pre_body = interface.request_sample

    if not is_sign:
        request_body = pre_body
    else:
        # toDo
        request_body = None

    ms = Message('http',type,header,cookie,host,url)

    result = {}
    return jsonify(result)