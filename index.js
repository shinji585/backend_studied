document.getElementById('countryForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const countryData = {
        name: document.getElementById('name').value, 
        capita: document.getElementById('capital').value, 
        area: parseInt(document.getElementById('area').value)
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/countries', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(countryData)
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById('countryForm').reset(); 
        }
    } catch (error) {
        console.error(error);
        const msg = document.getElementById("responseMessage");
        if (msg) msg.innerText = "Could not connect to server.";
    }
});