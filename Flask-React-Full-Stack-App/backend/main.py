from flask import request, jsonify
from models import Contact
from config import app, db

#CRUD endpoints for the contact model.


#Get all contacts.
@app.route("/contacts/", methods=["GET"])
def get_contacts():
    contacts=Contact.query.all()
    json_contacts=list(map(lambda y: y.to_json(),contacts))
    return jsonify({"contacts":json_contacts}), 200

#Get one contact by id.
@app.route("/contacts/<int:contact_id>", methods=["GET"])
def get_contact(contact_id):
    contact=Contact.query.get(contact_id)
    if not contact:
        return jsonify({"message":"Contact with given id not found."}), 404
    return jsonify({"contact":contact.to_json()})

#Create
#Required values for create endpoint -> first_name, last_name and email.
@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name=request.json.get("firstName")
    last_name=request.json.get("lastName")
    email=request.json.get("email")
    if not first_name or not last_name or not email:
        return jsonify({"message":"You must include all three first_name, last_name and email to create a new contact."}), 400

    new_contact=Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message":str(e)}), 400

    return jsonify({"message":"Contact created successfully."}), 201


@app.route("/update_contact/<int:contact_id>", methods=["PATCH"])
def update_contact(contact_id):
    contact=Contact.query.get(contact_id)
    if not contact:
        return jsonify({"message":"Contact with given id not found."}), 404

    data=request.json
    contact.first_name=data.get("firstName", contact.first_name)
    contact.last_name=data.get("lastName", contact.last_name)
    contact.email=data.get("email", contact.email)
    try:
        db.session.commit()
    except Exception as e:
        return jsonify({"message":str(e)})
    return jsonify({"message":"Contact updated successfully."}), 200

#Delete one contact.
@app.route("/delete_contact/<int:contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    contact=Contact.query.get(contact_id)
    if not contact:
        return jsonify({"message":"Contact with given id not found."})
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message":"Contact deleted successfully."}), 204






if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
