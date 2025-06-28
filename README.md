# AI-Assisted-Programming-Book
![Book Cover](https://github.com/ttaulli/AI-Assisted-Programming-Book/blob/main/images/book_cover.png?raw=true)

## Tom's Book and Course

- [AI-Assisted Programming: Better Planning, Coding, Testing, and Deployment](https://amzn.to/48qeAa9)
- [GitHub Copilot Shortcuts - Video Edition](https://learning.oreilly.com/playlists/52fae684-596f-4862-a900-a60478a58901/) (Note:  You need a subscription to O'Reilly Media)

## AI-Assisted Programming Tools

- [GitHub Copilot](https://github.com/features/copilot)
- [Amazon CodeWhisperer](https://aws.amazon.com/codewhisperer/)
- [Google's Gemini Code Assist](https://cloud.google.com/products/gemini/code-assist?hl=en)
- [Tabnine](https://www.tabnine.com/)
- [Cursor](https://cursor.sh/)
- [Cody](https://sourcegraph.com/cody)
- [Replit](https://replit.com/)
- [Codium](https://codeium.com/)


## YouTube Videos

- [GitHub Universe 2023 opening keynote- Copilot in the Age of AI](https://www.youtube.com/watch?v=NrQkdDVupQE&t=2s)
- [Empowering devs with AI: How Shopify made GitHub Copilot core to its culture](https://www.youtube.com/watch?v=wVKBwcm5dbw)

## Research

- [Pluralsight research finds 74% of software developers are planning to upskill in AI-assisted coding](https://www.pluralsight.com/newsroom/press-releases/pluralsight-research-finds-74--of-software-developers-are-planni)
- [Evaluating the Code Quality of AI-Assisted Code Generation Tools: An Empirical Study on GitHub Copilot, Amazon CodeWhisperer, and ChatGPT](https://arxiv.org/abs/2304.10778)
- [Coding on Copilot: 2023 Data Suggests Downward Pressure on Code Quality](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality)
- [AI code, security, and trust in modern development](https://snyk.io/reports/ai-code-security/)

## Weather App Environment Variables

To use the weather lookup feature, you must provide an OpenWeatherMap API key.

1. Copy `.env.example` to `.env.local` in the `weather-app` directory:
   ```sh
   cp .env.example .env.local
   ```
2. Edit `.env.local` and set your API key:
   ```env
   NEXT_PUBLIC_OPENWEATHERMAP_API_KEY=your_api_key_here
   ```

The app will not work without a valid API key.
