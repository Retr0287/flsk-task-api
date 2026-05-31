import jwt
from flask import request, jsonify
from config import Config
def get_user_id():
    auth=request.headers.get("Authorization")
    if not auth:
        return jsonify({"error":"no token"}), 401
    elif not auth.startswith("Bearer "):
        return jsonify({"error": "invalid token"}), 401
    
    token=auth.split(None, 1)[1]
    
    try:
        data=jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
    except:
        return jsonify({"error": "invalid token"}), 401
    
    return data["user_id"]