from flask import Flask, request

app = Flask(__name__)


# Create the appropriate app.route functions. Test and see if they work

# Make an app.route() decorator here for when the client sends the URI "/puppies"
@app.route("/puppies", methods=["GET", "POST", "DELETE"])
def puppiesFunction():
    if request.method == "GET":
        return getAllPuppies()
    elif request.method == "POST":
        return makeNewPuppy()


# Make another app.route() decorator here that takes in an integer named 'id' for when the client visits a URI like "/puppies/5"
@app.route("/puppies/<int:id>")
def puppiesFunctionId(id):
    if request.method == "GET":
        return getPuppy(id)
    elif request.method == "POST":
        return updatePuppy(id)
    elif request.method == "DELETE":
        return deletePuppy(id)
    return deletePuppy(id)


def getAllPuppies():
    return "Get all puppies"


def makeNewPuppy():
    return "Get a puppy"


def deletePuppy(id):
    return "Delete a puppy with id %s" % id


def getPuppy(id):
    return "Get a puppy with id %s" % id


def updatePuppy(id):
    return "Update a puppy with id %s" % id


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
