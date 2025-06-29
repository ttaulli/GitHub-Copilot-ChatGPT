"""
CHANGELOG
Semantic Versioning: 1.2.1
"""

## [1.4.0] - 2025-06-29
### Changed
- Expanded `api_server.py` in `7-agent-mcp/` to provide four endpoints: `/hello` (GET), `/echo` (POST), `/items/{item_id}` (GET), and `/items` (POST).
- Updated `README.md` in `7-agent-mcp/` with new endpoint documentation and usage examples.

## [1.3.0] - 2025-06-29
### Added
- Created `api_server.py` in `7-agent-mcp/` with a FastAPI server exposing `/hello` (GET) and `/echo` (POST) endpoints.
- Added `pydantic` to requirements for FastAPI data validation.
- Created `README.md` in `7-agent-mcp/` with usage and endpoint documentation.

## [1.2.1] - 2025-06-28
### Added
- Created `test_tests.py` in `7-agent-mcp/` to provide unit tests for the `calculate` function in `tests.py` using the `unittest` framework.
- Updated `README.md` with instructions for running the new test file.

## [1.2.0] - 2025-06-28
### Changed
- Replaced homepage in `weather-app` with a modern TailwindCSS form for city weather lookup.
- Added client-side validation for city input.
- Integrated OpenWeatherMap API fetch and display.
- API key now required in `.env.local` as `NEXT_PUBLIC_OPENWEATHERMAP_API_KEY` (see `.env.example`).
- Updated `.gitignore` to ensure `.env` files are excluded.
- Documented environment variable usage in `README.md`.

## [1.1.0] - 2025-06-28
### Added
- Created a modern Todo application in the Next.js project using TailwindCSS.
- Implemented Supabase integration for storing and managing tasks.
- Added functionality to add, mark as completed, and delete tasks.
- Set up environment variables for Supabase URL and anon key.
- Updated README.md with setup instructions for the Todo application.
### Added
- Replaced homepage with a modern weather form using TailwindCSS, client-side validation, and weather display.
- Created `/api/weather` endpoint to fetch weather from OpenWeatherMap API securely.
- Added `.env.local` and `.env.example` for API key management.
- Updated `README.md` with environment variable documentation.

## [1.0.2] - 2025-06-28
### Changed
- Updated .gitignore to ignore only 7-agent-mcp/weather-app/ instead of the entire 7-agent-mcp/ folder.

## [1.0.1] - 2025-06-28
### Added
- Created .gitignore to exclude 7-agent-mcp/ from version control.

## [1.0.0] - 2025-06-28
### Added
- Created a weather page in Next.js app to allow users to enter a city and view current weather using OpenWeatherMap API.
- Moved API key to environment variable and documented in .env.example and README.md.
- Added input validation and error handling for user input and API responses.
