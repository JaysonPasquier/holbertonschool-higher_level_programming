# Using curl for API Interactions

## Installation and Version Check

```bash
# Install curl on Ubuntu/Debian
sudo apt-get update
sudo apt-get install curl

# Check curl version
curl --version
```

## Basic GET Requests

```bash
# Basic webpage fetch
curl http://example.com

# Fetch posts from JSONPlaceholder
curl https://jsonplaceholder.typicode.com/posts

# Fetch with pretty JSON output (requires jq)
curl https://jsonplaceholder.typicode.com/posts | jq '.'
```

## Working with Headers

```bash
# View only response headers
curl -I https://jsonplaceholder.typicode.com/posts

# Add custom headers to request
curl -H "Content-Type: application/json" \
     -H "Authorization: Bearer token123" \
     https://jsonplaceholder.typicode.com/posts
```

## POST Requests

```bash
# Basic POST with form data
curl -X POST \
     -d "title=Test Post&body=This is content&userId=1" \
     https://jsonplaceholder.typicode.com/posts

# POST with JSON data
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"title": "Test Post", "body": "This is content", "userId": 1}' \
     https://jsonplaceholder.typicode.com/posts
```

## Common Options Reference

| Option | Description | Example |
|--------|-------------|---------|
| `-X` | Specify HTTP method | `curl -X POST url` |
| `-H` | Add header | `curl -H "Content-Type: application/json" url` |
| `-d` | Send data | `curl -d "name=value" url` |
| `-i` | Include response headers | `curl -i url` |
| `-v` | Verbose output | `curl -v url` |
| `-o` | Save output to file | `curl -o output.json url` |

## Practice Examples

1. **Fetch a Single Post**
```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

2. **Create a New Post**
```bash
curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"title": "New Post", "body": "Content", "userId": 1}' \
     https://jsonplaceholder.typicode.com/posts
```

3. **Update a Post**
```bash
curl -X PUT \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Title", "body": "Updated Content", "userId": 1}' \
     https://jsonplaceholder.typicode.com/posts/1
```

## Expected Outputs

### Version Check
```
curl 7.68.0 (x86_64-pc-linux-gnu) libcurl/7.68.0 OpenSSL/1.1.1f zlib/1.2.11 brotli/1.0.7 ...
```

### GET Request Response
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati",
  "body": "quia et suscipit suscipit recusandae..."
}
```

### POST Request Response
```json
{
  "id": 101,
  "title": "Test Post",
  "body": "This is content",
  "userId": 1
}
```