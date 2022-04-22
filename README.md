_<h1>A small web app to track the growth and fall of my crypto portfolio</h1>_
![image](https://user-images.githubusercontent.com/61281668/164613859-b54d777b-9d67-43a5-a45a-fa1f91428308.png)

<hr>
<h3> Ready endpoints</h3>
<ul>
<li>Register  -> api/register</li>
<li>Create portfolio -> api/addportfolio </li>
<li>Add token to portfolio -> api/testadd</li>
<li>Delete token from portfolio -> api/testdelete</li>
</ul>
<hr>
<h3> To deploy the project to yourself :  </h3>
<p>Install venv -> <code>python -m venv venv</code></p>
<p>Install requirements -> <code>pip install -r requirements.txt</code></p>
<p>Default migrations -> <code> makemigrations/migrate</code></p>
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
