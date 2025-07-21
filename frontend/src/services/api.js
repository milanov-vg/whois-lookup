import axios from 'axios';
import { API_URL } from '../utils/env';

export const fetchWhoisData = async (domain, type) => {
  const response = await axios.post(`${API_URL}/whois/`, { domain, type });
  return response.data;
};
