import React, { useState } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleAnalyzeClick = async () => {
    setIsLoading(true);
    setError('');
    setResult(null);

    try {
      // API endpoint is your FastAPI server
      const response = await fetch('http://127.0.0.1:8000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error('Analysis failed. Please check if the backend is running.');
      }
      
      const data = await response.json();
      setResult(data);

    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>ToxScreener</h1>
        <p>Analyze biomedical text for toxicology relevance.</p>
        <textarea
          className="text-input"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Paste scientific abstract here..."
        />
        <button onClick={handleAnalyzeClick} disabled={isLoading}>
          {isLoading ? 'Analyzing...' : 'Analyze'}
        </button>
        {error && <div className="error-message">{error}</div>}
        {result && (
          <div className="result-container">
            <h3>Analysis Result</h3>
            <p><strong>Prediction:</strong> {result.prediction}</p>
            <p><strong>Confidence:</strong> {(result.confidence * 100).toFixed(2)}%</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
