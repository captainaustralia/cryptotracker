This branch contains JWT authentication with saving a token in cookies, but I don't quite understand how I can check the state of the client, and also what to do with passing the refresh token, maybe I'll use this later. But now I'm facing several problems :
- how to pass a refresh token (it is possible to make access infinite, but then what's the point)
- how to use this token from cookies to reflect the state of the client (it is possible to put some kind of state with the true flag in vuex after authorization and remove it after some point ...)
Everything works correctly, the token is in the cookies, maybe I'll come back to this
