# API Server for GitHub Copilot ChatGPT

## Project Description
A simple FastAPI-based API server that provides basic endpoints for demonstration and testing purposes. Includes endpoints for greetings, echoing data, and managing sample items.

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ttaulli/GitHub-Copilot-ChatGPT.git
   cd GitHub-Copilot-ChatGPT/7-agent-mcp/api_server
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic
   ```

### Running the API Server
```bash
uvicorn api_server:app --reload
```

## API Endpoints

### GET /hello
Returns a simple greeting message.

**Response Example:**
```json
{"message": "Hello, world!"}
```

### POST /echo
Echoes back the posted data.

**Request Example:**
```json
{"data": "Sample input"}
```
**Response Example:**
```json
{"echo": "Sample input"}
```

### GET /items/{item_id}
Retrieves a sample item by ID.

**Response Example:**
```json
{
  "item_id": 1,
  "name": "Item 1",
  "description": "A sample item.",
  "price": 9.99,
  "in_stock": true
}
```

### POST /items
Creates a new item (returns the posted data).

**Request Example:**
```json
{
  "name": "Book",
  "description": "A test item.",
  "price": 12.5,
  "in_stock": true
}
```
**Response Example:**
```json
{
  "item": {
    "name": "Book",
    "description": "A test item.",
    "price": 12.5,
    "in_stock": true
  }
}
```

## Environment Variables
No environment variables are required for local development by default. If you add any, document them here and in `.env.example`.

## Testing
You can add tests using `unittest` or `pytest`. Example:
```bash
pytest
```

## License
MIT

## Contact
For questions or contributions, open an issue or pull request on GitHub.
