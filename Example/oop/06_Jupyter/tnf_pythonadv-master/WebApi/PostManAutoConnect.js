// Copier coller dans pre-request script

const logUrl = 'http://localhost:8000/api/auth/token/'

const getTokenReq = 
{
    method: 'POST',
    url: logUrl,
    header: 'Content-Type:application/json',
    body: 
    {
        mode: 'application/json',
        raw: JSON.stringify({
            "username": "test",
            "password": "p@5w0rD-1"
        })
    }
}

pm.sendRequest(getTokenReq, (err, res) => 
{
    console.log(res);
    if(err == null)
    {
        var resJson = res.json();
        let token = resJson.access;
        pm.collectionVariables.set('access_token', token);
    }
})