from flask import Flask, render_template, flash, redirect, render_template, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake


app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False 
# app.config["TESTING"] = True
# app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]

debug = DebugToolbarExtension(app)

connect_db(app)



# GET /api/cupcakes

#     Get data about all cupcakes.

#     Respond with JSON like: {cupcakes: [{id, flavor, size, rating, image}, ...]}.

#     The values should come from each cupcake instance.
# GET /api/cupcakes/[cupcake-id]

#     Get data about a single cupcake.

#     Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}.

#     This should raise a 404 if the cupcake cannot be found.
# POST /api/cupcakes

#     Create a cupcake with flavor, size, rating and image data from the body of the request.

#     Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}.

# Test that these routes work in Insomnia.

# We’ve provided tests for these three routes; these test should pass if the routes work properly.

# You can run our tests like:

# (venv) $ python -m unittest -v tests


@app.route("/api/cupcakes")
def get_all_cupcakes():
    """Show homepage with all cupcakes."""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    

    return jsonify(cupcakes=all_cupcakes)

@app.route("/api/cupcakes/<int:id>")
def get_cupcake():
    """Show single cupcake."""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())
  
@app.route("/api/cupcakes", methods=["POST"])
def post_a_cupcake():
    """Show form to create a cupcake."""
    # if request.json["image"]:
    #     image = request.json["image"]
    # else:
    #     image = "https://tinyurl.com/demo-cupcake"
        
    # if not request.json["flavor"]:
    #     return (jsonify(message="Need to add a flavor"), 404)
    # elif not request.json["size"]:
    #     return (jsonify(message="Need to add a size"), 404)
    # elif not request.json["rating"]:
    #     return (jsonify(message="Need to add a rating"), 404)
    # else: 
    cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], rating=request.json["rating"], image=request.json["image"])
    db.session.add(cupcake)
    db.session.commit()    
    response_json = jsonify(cupcake=cupcake.serialize())

    return (response_json, 201)  


# @app.route("/add", methods=["GET", "POST"])
# def add_pet():
#     """Pet add form; handle adding."""

#     form = AddPetForm()

#     if form.validate_on_submit():
#         name = form.name.data
#         species = form.species.data
#         photo = form.photo.data
#         age = form.age.data
#         notes = form.notes.data
#         available = form.available.data
        
#         new_pet = Pet(name=name, species=species, photo=photo, age=age, notes=notes, available=available)
#         db.session.add(new_pet)
#         db.session.commit()
#         flash(f"Added {name} the {species}", "success")
#         return redirect("/add")

#     else:

#         return render_template(
#             "add_pet.html", form=form)


# @app.route("/edit/<int:pet_id>", methods=["GET", "POST"])
# def edit_pet(pet_id):
#     """Edit the pet listing."""
#     pet = Pet.query.get_or_404(pet_id)
#     form = AddPetForm(obj=pet)

#     if form.validate_on_submit():
#         pet.name = form.name.data
#         pet.species = form.species.data
#         pet.photo = form.photo.data
#         pet.age = form.age.data
#         pet.notes = form.notes.data
#         pet.available = form.available.data
        
#         db.session.commit()
#         flash(f"Updated {pet.name} the {pet.species}", "success")
#         return redirect(f"/edit/{pet_id}")

#     else:

#         return render_template(
#             "edit_pet.html", form=form, pet=pet)

# @app.route("/add", methods=["GET", "POST"])
# def add_snack():
#     """Snack add form; handle adding."""

#     form = AddSnackForm()

#     if form.validate_on_submit():
#         name = form.name.data
#         price = form.price.data
#         flash(f"Added {name} at {price}")
#         return redirect("/add")

#     else:
#         return render_template(
#             "snack_add_form.html", form=form)


# @app.route("/users/<int:uid>/edit", methods=["GET", "POST"])
# def edit_user(uid):
#     """Show user edit form and handle edit."""

#     user = User.query.get_or_404(uid)
#     form = UserForm(obj=user)

#     if form.validate_on_submit():
#         user.name = form.name.data
#         user.email = form.email.data
#         db.session.commit()
#         flash(f"User {uid} updated!")
#         return redirect(f"/users/{uid}/edit")

#     else:
#         return render_template("user_form.html", form=form)
