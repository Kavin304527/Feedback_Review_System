import React, { useState, useEffect } from 'react'
import './FeedbackList.css'

const FeedbackList = () => {
  const [feedbacks, setFeedbacks] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchFeedbacks()
  }, [])

  const fetchFeedbacks = async () => {
    try {
      const response = await fetch('http://localhost:8080/feedbacks/')
      const data = await response.json()
      setFeedbacks(data)
    } catch (error) {
      console.error('Error fetching feedbacks:', error)
    } finally {
      setLoading(false)
    }
  }

  const updateStatus = async (id, newStatus) => {
    try {
      await fetch(`http://localhost:8080/feedbacks/${id}/status`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: newStatus })
      })
      fetchFeedbacks()
    } catch (error) {
      console.error('Error updating status:', error)
    }
  }

  if (loading) return <div className="loading">Loading feedbacks...</div>

  return (
    <div className="feedback-list">
      <h2>Feedbacks ({feedbacks.length})</h2>
      <div className="feedbacks-container">
        {feedbacks.map(feedback => (
          <div key={feedback.id} className={`feedback-item status-${feedback.status.toLowerCase().replace(' ', '-')}`}>
            <div className="feedback-header">
              <h3>{feedback.user_name}</h3>
              <span className="rating">{'★'.repeat(feedback.rating)}</span>
              <span className={`status-badge ${feedback.status.toLowerCase()}`}>
                {feedback.status}
              </span>
            </div>
            <p className="feedback-message">{feedback.message}</p>
            <div className="feedback-actions">
              <button
                onClick={() => updateStatus(feedback.id, 'Approved')}
                disabled={feedback.status === 'Approved'}
              >
                Approve
              </button>
              <small>{new Date(feedback.created_at).toLocaleString()}</small>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default FeedbackList
