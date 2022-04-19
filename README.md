_<h1>A small web app to track the growth and fall of my crypto portfolio</h1>_
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

1.1 
Implemented on the backend side:

Registration
Authorization via JWT (there is also an implementation, via storing jwt in a cookie, with the httponly * flag if necessary)
Custom user model
Custom manager
Other models
Created the necessary endpoints (starter package)
-> register
-> access token
-> refresh token
-> portfolio
-> add coin
-> delete coin

To the front side (Vue3):

An indefinite part (test) has been written.
Some functionality has been added, including endpoints for authorization, registration, getting data from a portfolio, tracking users + a mechanism for automatically renewing tokens
