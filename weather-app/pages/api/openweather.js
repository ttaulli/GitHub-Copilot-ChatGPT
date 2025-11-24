// Minimal proxy API route to keep API key server-side.
// It forwards the query to OpenWeatherMap using the server-only env var.

export default async function handler(req, res) {
  const { q } = req.query
  const key = process.env.OPENWEATHER_API_KEY || process.env.NEXT_PUBLIC_OPENWEATHER_API_KEY
  if (!q) return res.status(400).send('Missing query')
  if (!key) return res.status(500).send('API key not configured')

  try {
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(q)}&appid=${key}&units=imperial`
    const r = await fetch(apiUrl)
    const text = await r.text()
    const status = r.status
    // forward status and body
    res.status(status).send(text)
  } catch (err) {
    res.status(500).send(String(err.message))
  }
}
