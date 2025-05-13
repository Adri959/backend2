const serverURl = "http://127.0.0.1:8000/"

function getAllItems()
{
    fetch("http://127.0.0.1:8000/api/items/").
    then(res=>res.json()).
    then(result=>{

        result.array.forEach(item => {
            document.querySelector("#result").innerHTML+=
            `
            <div class ="col-12 col-md-4 col-lg-3">
            <div class="card" style="width:400px">
                <img class="card-body" src="${serverURL}${item.boxArt}" >
                <div class="card-body">
                    <h4 class="card-title">${item.title}</h4>
                    <p class="card-text">
                    ${item.description} <br/>
                    ${item.uploadDate}<br/>
                    ${item.category.categoryName}
                    </p>
                    <form action="javascript:deleteItem(${item.id}" method="POST")
                    <input type="submit" class="btn btn-primary" value="Delete">
                    </form>
                    
                </div>
            </div>
            
            
            `
            
        });
            
        })
        
    };


getAllItems()