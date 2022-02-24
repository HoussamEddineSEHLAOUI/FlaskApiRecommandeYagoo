from flask import Flask, request, jsonify

app = Flask(__name__)
urlApi = "/api-yagoo/"


@app.route(urlApi+"Poste", methods=['GET', 'POST'])
def set_onPoste():
    content = request.json
    return {
        "userID": content['userID'],
        "PosteID": content['PosteID'],
        "isClickOnPoste": content['isClickOnPoste'],
        "isLikePoste": content['isLikePoste'],
        "isClickClosebtnPoste": content['isClickClosebtnPoste'],
    }


@app.route(urlApi+"rate-poste", methods=['PUT'])
def setRating_onPoste():
    content = request.json
    return {
        "userID": content['userID'],
        "PosteID": content['PosteID'],
        "RateOnPoste": content['RateOnPoste']
    }


@app.route(urlApi+"cilck-poste_marker-map", methods=['POST'])
def set_onPoste_ClickMarker_onMap():
    content = request.json
    return {
        "userID": content['userID'],
        "PosteID": content['PosteID'],
        "isClickMarkerOnMAp": content['isClickMarkerOnMAp']
    }


@app.route(urlApi+"click-webSite-poste", methods=['POST'])
def set_onPoste_ifVisteWebSite():
    content = request.json
    return {
        "userID": content['userID'],
        "PosteID": content['PosteID'],
        "isClickWebSite": content['isClickWebSite']
    }


if __name__ == "__main__":
    app.run(debug=True)
