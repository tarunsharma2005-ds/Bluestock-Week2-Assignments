# REST API → JSON → CSV

## Goal
Call a public practice API, check the JSON response, and save the returned records as a CSV for analysis.

**Endpoint:** `https://api.jsonplaceholder.dev/posts`  
**HTTP method:** GET  
**Authentication:** Not required for this public demonstration API.  
**Expected fields:** `userId`, `id`, `title`, `body`  
**Data note:** This is sample/testing content, not real financial-market data.

## Key concepts
- **API:** a defined way for software systems to request or exchange information.
- **GET:** requests data from a server.
- **JSON:** structured data format often returned by APIs.
- **Query parameter:** an option added to a URL, often after `?`, such as `?userId=1`.
- **Authentication:** verifies who or what is making a request. Never commit real API keys to GitHub.

## Run on macOS
From the project root, activate the virtual environment and install requests as described in the root README, then run:

```bash
python api_project/api_data_extraction.py
```

The script prints the HTTP status, record count, and first three rows, then writes `data/api_posts.csv`.

## Postman test
1. Open Postman.
2. Create a new HTTP request.
3. Select `GET`.
4. Enter `https://api.jsonplaceholder.dev/posts`.
5. Click Send.
6. Inspect the JSON response and status code.

Optional query parameter: add key `userId` and value `1` in the Params tab.

## Error handling included
The Python script checks HTTP errors, network errors and unexpected response structure.
