# Email Sanitizer

Single-purpose API. Stateless. Deterministic. Returns JSON only.

## Endpoints
- GET `/health`
- GET `/v1/email-sanitize?email=`

## Example

Request:
`/v1/email-sanitize?email=Test+User@GMAIL.com`

Response:
```json
{
  "input": "Test User@GMAIL.com",
  "sanitized": "testuser@gmail.com",
  "is_valid": true,
  "reason": null
}
