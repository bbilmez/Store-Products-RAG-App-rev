document.getElementById("requestForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const inputData = document.getElementById("inputData").value;
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    
    const raw = JSON.stringify({
      "query": inputData
    });
    
    const requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
      redirect: "follow"
    };
    
    fetch("http://127.0.0.1:5000/query", requestOptions)
    .then(response => response.json())
    .then(data => {
        document.getElementById("jsonResponse").textContent = data["response"];
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("jsonResponse").textContent = error;
    });
});
