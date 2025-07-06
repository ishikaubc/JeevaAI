import express from 'express';
import cors from 'cors';

const app = express();
app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Backend is running');
});

app.listen(5001, () => {
  console.log('🔁 Server running on http://localhost:5001');
});
