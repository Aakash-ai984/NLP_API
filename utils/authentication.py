import secrets
from fastapi import Request, HTTPException

# API Keys स्टोर करने के लिए Dictionary (आप इसे Database से भी जोड़ सकते हैं)
api_keys = {
    "user1": secrets.token_hex(32),  
    "user2": secrets.token_hex(32)  
}

# API Key को वेरीफाई करने का फ़ंक्शन
def verify_api_key(request: Request):
    api_key = request.headers.get("x-api-key")
    if api_key not in api_keys.values():
        raise HTTPException(status_code=401, detail="Invalid API Key")
