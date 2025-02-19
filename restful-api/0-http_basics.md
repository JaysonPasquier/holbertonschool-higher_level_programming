# HTTP/HTTPS Basics

## HTTP vs HTTPS Comparison

| Feature | HTTP | HTTPS |
|---------|------|-------|
| Port | 80 | 443 |
| Encryption | None | SSL/TLS encryption |
| Security | Data sent in plaintext | Data is encrypted |
| URL Prefix | http:// | https:// |
| Speed | Slightly faster | Minimal overhead due to encryption |
| Certificate | Not required | SSL/TLS certificate required |

## HTTP Request Structure

```
GET /api/users HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: application/json
```

## HTTP Response Structure

```
HTTP/1.1 200 OK
Content-Type: application/json
Date: Mon, 23 Oct 2023 10:00:00 GMT

{"status": "success", "data": [...]}
```

## Common HTTP Methods

1. **GET**
   - Purpose: Retrieve data
   - Use case: Fetching webpage content, retrieving API data
   - Example: `GET /api/users`

2. **POST**
   - Purpose: Create new resources
   - Use case: Submitting forms, creating new records
   - Example: `POST /api/users`

3. **PUT**
   - Purpose: Update existing resources
   - Use case: Updating entire user profile
   - Example: `PUT /api/users/123`

4. **DELETE**
   - Purpose: Remove resources
   - Use case: Deleting user account
   - Example: `DELETE /api/users/123`

## Common HTTP Status Codes

1. **200 OK**
   - Description: Request successful
   - Scenario: Successfully fetching data from API

2. **201 Created**
   - Description: Resource created successfully
   - Scenario: New user account created

3. **404 Not Found**
   - Description: Resource not found
   - Scenario: Accessing non-existent webpage

4. **400 Bad Request**
   - Description: Invalid request syntax
   - Scenario: Submitting form with invalid data

5. **500 Internal Server Error**
   - Description: Server encountered an error
   - Scenario: Database connection failure

## Security Implications

- HTTP traffic can be intercepted and read by attackers
- HTTPS provides:
  - Data encryption
  - Server authentication
  - Data integrity
  - Protection against man-in-the-middle attacks

## Practical Example

Using cURL to demonstrate HTTP vs HTTPS:

```bash
# HTTP Request
curl -v http://example.com

# HTTPS Request
curl -v https://example.com
```