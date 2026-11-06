import eel

@eel.expose
def get_app_status() -> dict:
    return {"ok": True, "data": {"application": "Data-Flow", "status": "ready"}, "error": None}

def register_system_api() -> None:
    return None
