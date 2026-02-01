from fastapi import FastAPI, Query
from pydantic import BaseModel
from email_validator import validate_email, EmailNotValidError

app = FastAPI(title="Email Sanitizer", version="v1")

class Health(BaseModel):
    ok: bool

class EmailSanitizeResponse(BaseModel):
    input: str
    sanitized: str | None
    is_valid: bool
    reason: str | None = None

@app.get("/health", response_model=Health)
def health():
    return {"ok": True}

@app.get("/v1/email-sanitize", response_model=EmailSanitizeResponse)
def email_sanitize(email: str = Query(..., description="Email address to sanitize/normalize")):
    raw = email.replace(" ", "+")
    try:
        v = validate_email(raw, check_deliverability=False)
        return {
            "input": raw,
            "sanitized": v.normalized,
            "is_valid": True,
            "reason": None,
        }
    except EmailNotValidError as e:
        return {
            "input": raw,
            "sanitized": None,
            "is_valid": False,
            "reason": str(e),
        }
