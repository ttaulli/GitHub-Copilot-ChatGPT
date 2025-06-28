"""
CHANGELOG
Semantic Versioning: 1.0.0
"""

## [1.0.0] - 2025-06-28
### Added
- Created a weather page in Next.js app to allow users to enter a city and view current weather using OpenWeatherMap API.
- Moved API key to environment variable and documented in .env.example and README.md.
- Added input validation and error handling for user input and API responses.

## [1.0.1] - 2025-06-28
### Added
- Created .gitignore to exclude 7-agent-mcp/ from version control.

## [1.0.2] - 2025-06-28
### Changed
- Updated .gitignore to ignore only 7-agent-mcp/weather-app/ instead of the entire 7-agent-mcp/ folder.

## [1.1.0] - 2025-06-28
### Added
- Replaced homepage with a modern weather form using TailwindCSS, client-side validation, and weather display.
- Created `/api/weather` endpoint to fetch weather from OpenWeatherMap API securely.
- Added `.env.local` and `.env.example` for API key management.
- Updated `README.md` with environment variable documentation.

## [1.2.0] - 2025-06-28
### Changed
- Replaced homepage in `weather-app` with a modern TailwindCSS form for city weather lookup.
- Added client-side validation for city input.
- Integrated OpenWeatherMap API fetch and display.
- API key now required in `.env.local` as `NEXT_PUBLIC_OPENWEATHERMAP_API_KEY` (see `.env.example`).
- Updated `.gitignore` to ensure `.env` files are excluded.
- Documented environment variable usage in `README.md`.

## [1.1.1] - 2025-06-28
### Added
- Added `add_numbers(a: float, b: float) -> float` function to `5-writing-code/sample.py` to sum two numbers.
