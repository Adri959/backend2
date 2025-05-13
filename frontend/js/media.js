function getAllItems()
{
    fetch("http://127.0.0.1:8000/api/items/").
    then(res=>res.json()).
    then(result=>{
        console.log(result)
    });
}

getAllItems()