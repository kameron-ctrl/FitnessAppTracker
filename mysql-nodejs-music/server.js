const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());
app.use(express.static(__dirname));
//app.use(express.static('public')); // to serve static files like HTML, CSS, JS

// MySQL connection
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'music'
});

connection.connect((err) => {
  if (err) throw err;
  console.log('Connected to MySQL Server!');
});

const port = 3002;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

// Serve the static HTML file
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/musicians.html');
});

app.get('/findbyid', (req, res) => {
  const id = req.query.id;
  if (id) {
    connection.query('SELECT * FROM musicians WHERE ID = ?', [id], (err, results) => {
      if (err) throw err;
      res.json(results);
    });
  } else {
    // If no ID is provided, return all musicians
    connection.query('SELECT * FROM musicians', (err, results) => {
      if (err) throw err;
      res.json(results);
    });
  }
});


app.get('/findall', (req, res) => {
  connection.query('SELECT * FROM musicians', (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});

