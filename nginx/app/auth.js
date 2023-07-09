async function authGuard(r) {
    let auth = r.headersIn['Authorization'];
  
    if (!auth) {
      r.return(401, 'Unauthorized');
      return;
    }
  
    let jwt_token = null;
  
    try {
      
      jwt_token = auth.split(' ')[1];
  
      if (!jwt_token) {
        r.return(401, 'Unauthorized');
        return;
      }
  
      let response = await ngx.fetch(`http://host.docker.internal:8881/public/auth/token/info?access_token=${jwt_token}`);
  
      let data = await response.json();
  
      if (response.status === 200) {
        r.headersOut['X-Auth-User'] = data.data.username;
        r.headersOut['X-Auth-Role'] = data.data.role;
        r.return(200, 'OK');
        return;
      } 
  
      r.return(response.status, '');
  
    } catch (err) {
      r.return(500, 'Internal server error');
      return;
    }
  
    
  }
  
  export default { authGuard };
  