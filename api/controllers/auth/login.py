from flask import request, jsonify
from models.users import Users

def api_login():
    data = request.get_json()
    user = Users.query.filter_by(email=data.get('email')).first()

    if user and user.check_password(data.get('password')):
        return jsonify({
            "success": True,
            "message": "Selamat anda berhasil login"
            }), 200
    elif not user:
        return jsonify({"message": "Email tidak ditemukan, mohon periksa kembali email Anda"}), 404
    elif not user.check_password(data.get('password')):
         return jsonify({"message": "Password salah, mohon periksa kembali password Anda"}), 401
    else:
        return jsonify({"message": "Login gagal mohon periksa kembali email dan password Anda"}), 
        

# def api_login_by_google():