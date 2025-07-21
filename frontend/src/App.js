import React, { useState } from 'react';
import {
  Button,
  CircularProgress,
  Alert,
  TextField,
  Radio,
  FormControlLabel,
  Typography
} from '@mui/material';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

import TableDisplay from './components/TableDisplay';
import { fetchWhoisData } from './services/api';

function App() {
  const [domain, setDomain] = useState('');
  const [type, setType] = useState('domain');
  const [data, setData] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    setData(null);

    try {
      const res = await fetchWhoisData(domain, type);
      setData(res);
    } catch (err) {
      setError(err.response?.data?.error || 'An unexpected error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mt-5">
      <Typography variant="h4" className="mb-4 text-center">
        WHOIS Lookup Tool
      </Typography>
      <form onSubmit={handleSubmit} className="mb-3">
        <TextField
          fullWidth
          variant="outlined"
          label="Enter domain (e.g. amazon.com)"
          value={domain}
          onChange={(e) => setDomain(e.target.value)}
          className="mb-3"
        />

        <div className="mb-3">
          <FormControlLabel
            control={
              <Radio
                checked={type === 'domain'}
                onChange={() => setType('domain')}
                value="domain"
              />
            }
            label="Domain Info"
          />
          <FormControlLabel
            control={
              <Radio
                checked={type === 'contact'}
                onChange={() => setType('contact')}
                value="contact"
              />
            }
            label="Contact Info"
          />
        </div>

        <Button
          variant="contained"
          color="primary"
          type="submit"
          disabled={loading}
        >
          {loading ? <CircularProgress size={24} /> : 'Lookup'}
        </Button>
      </form>

      {error && <Alert severity="error">{error}</Alert>}
      {data && <TableDisplay data={data} />}
    </div>
  );
}

export default App;
