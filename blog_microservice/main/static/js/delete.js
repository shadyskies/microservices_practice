async function delete_blog(post_id){
    let ans = window.confirm("Are you sure you want to delete?")
    if (ans)
    {
        url = `http://172.17.0.1:8000/api/blogs/${post_id}`
        try{
            let response = await fetch(url, {
                method: 'DELETE',
                headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest'
                }
            })
            let response_data = await response.json();
            console.log(response_data)
            if (response.status === 200)
                window.location.href = "";
        }
        catch(err){
            console.log(err);
        }
    }
}