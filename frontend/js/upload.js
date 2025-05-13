function getCategories()
{
    fetch("http://127.0.0.1:8000/api/categories/").
    then(res=>res.json()).
    then(result=> {
        result.forEach(item => {
            document.querySelector("#category").innerHTML+=
            `
            <option value="${item.id}">${item.categoryName} </option>
            `;
            });
        
    });
}

function uploadMedia()
{
    let data = new FormData();
    data.append("title",document.querySelector("#title").value);
    data.append("description",document.querySelector("#description").value);
    data.append("boxArt",document.querySelector("#boxart").files[0]);
    data.append("category",document.querySelector("#category").value);
    fetch('http://127.0.0.1:8000/api/items/',
        {
            method: "POST",
            headers:{"Accept":"application/json"},
            body: data
        }
    ).then(alert("Uppload successful!"));
}

getCategories();