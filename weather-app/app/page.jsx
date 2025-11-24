import React from 'react'
import WeatherSearch from '../components/WeatherSearch'
import './globals.css'

export default function Home() {
  return (
    <main className="container">
      <h1 className="title">Weather App</h1>
      <p className="subtitle">Search current weather by city (and optional country code)</p>
      <WeatherSearch />
    </main>
  )
}
