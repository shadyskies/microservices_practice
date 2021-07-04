document.getElementById('submit-button').addEventListener("click", async function post(){
	let url = "http://172.17.0.1:8000/api/login/";
	let username = document.getElementById('username').value
	let pwd = document.getElementById('password').value
	
	let data = {
		"username": username,
		"password": pwd
	};
	
	try{
		let response = await fetch(url, {
		method: 'POST',
		headers: {
		'Accept': 'application/json',
		'Content-Type': 'application/json',
		'X-Requested-With': 'XMLHttpRequest'
		},
		body: JSON.stringify(data)
	})
		let response_data = await response.json();
		console.log(response_data);
		console.log(response.status);
		if (response.status === 200)
		{
			let access_token = JSON.parse(response_data.token).access; 
			document.write(access_token);
			window.localStorage.setItem('access_token', access_token);
			window.location.href = "/";
		}
	}
	catch(err){
		console.log(err);
	}
})