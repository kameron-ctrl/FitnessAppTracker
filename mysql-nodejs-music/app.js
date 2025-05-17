document.getElementById('searchForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const musicianId = document.getElementById('musicianId').value;
  let url = musicianId ? `/findbyid?id=${musicianId}` : '/findall';
  
  fetch(url)
    .then(response => response.json())
    .then(data => {
      const resultsTable = document.getElementById('resultsTable').getElementsByTagName('tbody')[0];
      resultsTable.innerHTML = ''; // Clear previous results

      data.forEach((row) => {
        let newRow = resultsTable.insertRow();
        newRow.insertCell(0).innerHTML = row.Id || 'N/A';
        newRow.insertCell(1).innerHTML = row.FirstName || 'N/A';
        newRow.insertCell(2).innerHTML = row.LastName || 'N/A';
        newRow.insertCell(3).innerHTML = row.Born || 'N/A';
      });
    })
    .catch(error => console.error('Error:', error));
});
