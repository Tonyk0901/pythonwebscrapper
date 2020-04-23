## 4.2 Dynamic URLs and Templates

In this section, I learned how to deal with a variable in the url, and render_template function of flask.

```python
@app.route("/<username>")
def home(username):
    return f"Hello! Nicholas!{username}"
```

Inside the url, the variable is passed on as <username>
When variable is passed in url, be sure to pass that as an argument to the function.

```python
from flask import render_template

@app.route("/<username>")
def home(username):
    return render_template("<html_url>")
```

You can return the html file by using the render_template function. Make sure to save html file under templates folder. Then the render_templates automatically looks for the html file under "templates" folder.

```html
<input required />
```

input tag is a self-closed tag. Also, required keyword forces the input to be given before submitted.

## 4.3 Forms and Query Arguments

In this section, I learned to redirect the url when the form is submitted and how to utilize the user input.

```html
<form action="/report" method="get">
  <input required name="word" />
  <button>Search</button>
</form>
```

Form tag has action and method attribute. Action attribute specifies the url to be redirected to when the form is submitted. In our exmaple, upon submission, the user will see url/report.

Also there are two methods for action: get and post. Get method displays the input and data in the urls. For example, "/?page=1&pagesize=50". Advantage is that the redirected page has the unique urls that the user can bookmark the page.

Post method, on the other hand, does not display the form input in the url. All the data is hidden. It's appropriate when the form input is a sensitive information. However, since no changes on the surface, it is not suitable for book marking.

Also, you can assign a name on the input tag with the name attribute.

```html
<input required name="job_name" />
```

Then when the form action occurs, the input data will appear at the end of the action url as "?job_name=<input>&..."

```python
from flask import request
print(request.args)
# ImmutableMultiDict([('job_name', 'python')])
```

We can retrieve the form input data by parsing the request using request function.
As can be seen in the result, the function returns a dictionary, which means we can use the "get" method to retreive the values.

Everytime you visit a web page or send a data to a web page, it is a request!!

?page=1&pagesize=100
This is called a query argument.

```python
word = request.args.get("job_name")
return render_template("flask_search_result.html", search_by = word)
```

Inside the html file,

```html
<h3>You are looking for a job in {{search_by}}</h3>
```

Render_template function takes in keyward arguements which can be passed onto the html file when being rendered.
First, pass the keyward arguement. Second, called the key in the html by following the syntax, {{search_by}}

## 4.4 Scrapper Integration

In this lecture, we integrate the scrapper we built previously into the flask app. There are some fixes made for now we want to search for jobs of any programming stacks, not just the python.

```python
from flask import redirect

if word :
    word.lower()
else :
    return redirect("/")
```

If word is not given, you can direct the user to a page you want by using the redirect function.
Important note: if you want to redirect to root page, the specific url is "/"

## For sure do some research and learn precisely about the git fetch and git pull and all the options available for those command for god's sake. git's fucking giving me headaches.

## 4.5 Faster Scrapper

In this lecture, we implemented a fake db that stores the search result so that when a same keyword is searched for the second time, we don't need to run the script again, which saves a ton of time.

To do so, simply implement a dictionary outside of the app scope as

```python
db = {}
```

And add block of codes which checks for the existence of the data and inserts one if it does not exist.

```python
if word not in db.keys():
    job = indeed_job_scrape.get_jobs(word)
    db[word] = job
```

## 4.6 Rendering Jobs!

CSS grid!

```css
section {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
}
```

grid-template-columns sepecifies the width of each column. For example, `grid-template-columns : 1fr 1fr 1fr 1fr, it will create four columns, with 1:1:1:1 width ratio. repeat(4, 1fr) is just a shortened form of it. Another example is, 1fr 2fr 1fr 2fr is equivalent to repeat(2, 1fr 2fr)

Similarly, you can set the grid height by using grid-template-rows.

```html
<head>
  <style>
    section {
      display: grid;
    }
  </style>
</head>
```

You don't need to set the link to the css. You can setup the style directly inside the head part.

## 4.7 & 4.8 Export Route and File Download

In this sections, we add the previously built save_to_csv function and implement a button that allows downloading the csv file that has the search results.
