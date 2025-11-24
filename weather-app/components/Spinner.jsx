import React from 'react'

export default function Spinner({ size = 28 }) {
  const style = {
    width: size,
    height: size,
  }
  return <div className="spinner" style={style} aria-hidden="true" />
}
