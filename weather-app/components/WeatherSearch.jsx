"use client"
import React, { useState } from 'react'
import Spinner from './Spinner'

const API_KEY = process.env.NEXT_PUBLIC_OPENWEATHER_API_KEY

export default function WeatherSearch() {
  const [query, setQuery] = useState('')
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function handleSubmit(e) {
    e.preventDefault()
    if (!query.trim()) {
      setError('Please enter a city name')
      return
    }
    setLoading(true)
    setError('')
    setData(null)
    try {
      const res = await fetch(
        `/api/openweather?q=${encodeURIComponent(query)}`
      )
      if (!res.ok) {
        const txt = await res.text()
        throw new Error(txt || 'Failed to fetch')
      }
      const json = await res.json()
      setData(json)
    } catch (err) {
      setError(String(err.message || err))
    } finally {
      setLoading(false)
    }
  }

  function iconUrl(code) {
    return code ? `https://openweathermap.org/img/wn/${code}@2x.png` : ''
  }

  return (
    <div className="weather-card">
      <form onSubmit={handleSubmit} aria-label="Search weather">
        <label htmlFor="city" style={{ display: 'none' }}>City</label>
        <input
          id="city"
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="City or City,country (e.g. Portland,US)"
          aria-label="City or City and country code"
        />
        <button type="submit" aria-label="Search">{loading ? <Spinner size={18} /> : 'Search'}</button>
      </form>

      {error && <p className="error" role="status">{error}</p>}

      {data && (
        <div className="result">
          <div className="result-grid">
            <div>
              <h2 style={{ margin: 0 }}>{data.name} {data.sys?.country ? `— ${data.sys.country}` : ''}</h2>
              <p className="meta">{data.weather?.[0]?.description}</p>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
              <img className="weather-icon" src={iconUrl(data.weather?.[0]?.icon)} alt={data.weather?.[0]?.description || 'weather icon'} />
              <div>
                <p className="temp">{Math.round(data.main.temp)}°F</p>
                <div className="pills">
                  <span className="pill">Feels like {Math.round(data.main.feels_like)}°F</span>
                  <span className="pill">Humidity {data.main.humidity}%</span>
                  <span className="pill">Wind {Math.round(data.wind?.speed || 0)} mph</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
      {loading && (
        <div style={{ marginTop: 14 }}>
          <Spinner />
        </div>
      )}
    </div>
  )
}
