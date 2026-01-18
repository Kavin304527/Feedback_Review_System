import React from 'react'
import FeedbackForm from './components/FeedbackForm.jsx'
import FeedbackList from './components/FeedbackList.jsx'
import './App.css'

function App() {
  return (
    <div className="app">
      <header className="header">
        <h1>Feedback System</h1>
      </header>
      <main className="main">
        <FeedbackForm />
        <FeedbackList />
      </main>
    </div>
  )
}

export default App
