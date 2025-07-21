import React from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Tooltip
} from '@mui/material';

const renderCell = (key, value) => {
  const strValue = String(value ?? '');
  const shouldTruncate = key === 'hostnames' && strValue.length > 25;

  if (shouldTruncate) {
    return (
      <Tooltip title={strValue} arrow placement="top">
        <span style={{ cursor: 'pointer', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', display: 'inline-block', maxWidth: 200 }}>
          {strValue.substring(0, 25) + '...'}
        </span>
      </Tooltip>
    );
  }

  return <span>{strValue}</span>;
};

const TableDisplay = ({ data }) => (
  <TableContainer component={Paper} className="mt-4">
    <Table>
      <TableHead>
        <TableRow>
          {Object.keys(data).map((key) => (
            <TableCell key={key} style={{ fontWeight: 'bold' }}>
              {key}
            </TableCell>
          ))}
        </TableRow>
      </TableHead>
      <TableBody>
        <TableRow>
          {Object.entries(data).map(([key, value]) => (
            <TableCell key={key}>
              {renderCell(key, value)}
            </TableCell>
          ))}
        </TableRow>
      </TableBody>
    </Table>
  </TableContainer>
);

export default TableDisplay;
