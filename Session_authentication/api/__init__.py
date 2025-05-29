from flask import jsonify, abort, request

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """GET user by id or 'me' for current authenticated user."""
    from models.user import User
    if user_id == "me":
        if not hasattr(request, "current_user") or request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_dict())
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())

def to_dict(self):
    """Return a dictionary representation of the User."""
    return {
        "id": self.id,
        "email": self.email,
        "session_id": self.session_id,
        "reset_token": self.reset_token
    }