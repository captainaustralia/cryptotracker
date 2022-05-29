<<<<<<< HEAD
_<h1>A small web app to track the growth and fall of my crypto portfolio</h1>_
![image](https://user-images.githubusercontent.com/61281668/164613859-b54d777b-9d67-43a5-a45a-fa1f91428308.png)

=======
This branch contains JWT authentication with saving a token in cookies, but I don't quite understand how I can check the state of the client, and also what to do with passing the refresh token, maybe I'll use this later. But now I'm facing several problems :
- how to pass a refresh token (it is possible to make access infinite, but then what's the point)
- how to use this token from cookies to reflect the state of the client (it is possible to put some kind of state with the true flag in vuex after authorization and remove it after some point ...)
<hr>

<h3> Ready endpoints</h3>
<ul>
<li>Register  -> api/register</li>
<li>Create portfolio -> api/addportfolio </li>
<li>Add token to portfolio -> api/testadd</li>
<li>Delete token from portfolio -> api/testdelete</li>
</ul>
>>>>>>> 04e314cfd3a23dd2a4d30b336d0344c5bbb74a77
<hr>
<h3> To deploy the project to yourself :  </h3>
<p>Install venv -> <code>python -m venv venv</code></p>
<p>Install requirements -> <code>pip install -r requirements.txt</code></p>
<p>Default migrations -> <code> makemigrations/migrate</code></p>
<code> Django v 4.0.4 / Django Rest Framework 3.13.1 </code>

<p> Frontside <strong> Vue 3 </strong></p>
<p> Install npm (frontend folder) -> <code> npm install </code>
<hr>
<h3>v1.1 pre </h3>
Implemented on the backend side:

<ul>
<li>Registration</li>
<li>Authorization via JWT (there is also an implementation, via storing jwt in a cookie, with the httponly * flag if necessary)</li>
<li>Custom user model</li>
<li>Custom manager</li>
<li>Other models</li>
</ul>

Created the necessary endpoints (starter package)
<ul>
<li>-> register</li>
<li>-> access token</li>
<li>-> refresh token</li>
<li>-> portfolio</li>
<li>-> add coin</li>
<li>-> delete coin</li>
</ul>

To the front side (Vue3):

<p>An indefinite part (test) has been written.
Some functionality has been added, including endpoints for authorization, registration, getting data from a portfolio, tracking users + a mechanism for automatically renewing tokens</p>
=======
Everything works correctly, the token is in the cookies, maybe I'll come back to this

