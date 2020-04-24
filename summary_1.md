# Python Web Scrapper

## #1, Theory

Learned basic python syntax.

- Python Standard Library.

  https://docs.python.org/3/library/

- Mutable vs immutable
- List has reverse function that reverses its order.

  ```python
  test_list.reverse()
  ```

  By the way, the name `list` is already occupied by python. So be careful not to name a variable as list.

- In dictionary, the key should be a string while the value can be any type.

  ```python
  test_dic = {"dic_key1" : test_list, "dic_key2" : "test_values"}
  ```

- When defining a function, you can set the default of the argument.

  ```python
  def minus(a, b = 0):
  ```

- You can check the type of a variable.

  ```python
  if type(b) is str :
  ```

  `is` and `is not` are for checking object identity. Know the difference between `==`, `!=` and `is`, `is not`.

- String is a list. You can set the for loop with a string.

  ```python
  for letter in "tony":
    print(letter)

  #t
  #o
  #n
  #y
  ```

  In place of `"tony"` should come an element of sequence: string, list, tuple, dictionary.

- You can import python packages.
  ```python
  import math
  from math import ceil, fsum as cool_sum
  ```
  You can either import the entire package or just the functions you want. Also you can rename the imported function using `as`.

## #2.0 ~ #2.3, Setting Up Environment

- Build a virtual environment using pipenv.
  ```
  pipenv --three
  pipenv shell
  pipenv install requests
  pipenv install bs4
  ```
- Set the interpreter of VSCode to the virtual environment.

## 2.3 ~ # 2.13, Scrapping

Extract data using `requests` and `bs4` library.

- Get the response object using request library.

  ```python
  import requests
  from bs4 import BeautifulSoup
  response = requests.get("url")
  result = response.text
  ```

  `result` is a response object. It can be of various format. `response.text` turns it into a text. `response.json()` turns it into a JSON.

- You can check if the webpage is up or down.

  ```python
  response = requests.get(URL).status_code
  ```

  `response` is 200 if webpage is up, 404 if down.

- `bs4` provides tools to parse the html text.

  ```python
  soup = BeautifulSoup(response.text, "html.parser")
  ```

- Find the html element by using `find` or `find_all`.

  ```python
  div_element = soup.find("div", class_={"pagination"}).find_all("span")
  ```

  First arugement is the name of html tag. `class_` specifies the class of the element you want to find. `find` finds one element, and `find_all` finds all element and return in list format.

- You can get the inner text.

  ```python
  text = soup.find("div").string
  ```

- You can get a certain attribute of the element.

  ```python
  title_attribute = soup.find("div")["title"]
  ```

- Recap
  1. Send requests and get response from the page.
  2. Turn the response into a either JSON or text.
  3. If text, you can parse the content using BeautifulSoup library.
  4. Get the html element that contains the target information by using find function.
  5. Get the text. Sometimes the information is stored in the attribute rather than in the text. If that's the case, retrieve the attribute.
  6. Store the information in the array as a form of dictionary. e.g. `[{"country":country, "code":code}, ...]`

## #2.14 ~ #2.16, Saving to CSV

Using standard package, csv, save data to .csv file.

- Create .csv file.

  ```python
  import csv
  with open("jobs.csv", mode="w") as jobs_file:
    # with block.
  ```

  `mode="w"` means write mode. If you want read mode, `mode="r"`.

  `with` is a shorthand for `try` / `final`. It ensures the `exist()` / `close()` at the end.

- Create a writer and write
  ```python
  jobs_writer = csv.writer(jobs_file)
  jobs_writer.writerow(["Title", "Location", "Link"])
  ```

## #3.1, Variable Arguments / Keyworded Arugments

In case you cannot specify exact number of argument, you can use the variable arguments / keyworded arguments concept. `*` or `**` is used infornt of arguments to show that arguments can be multiple.

- `*` stores multiple arguements in a list. `**` stores keyworded arguments in a dictionary.

  ```python
  def myFun(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

  myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")
  ```

  gives the output

  ```
  args: ('geeks', 'for', 'geeks')
  kwargs {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}
  ```

## #4.1, Introduction to flask

This section, I learned to start the basic flask application.

```python
app = Flask("Super Scrapper")
app.run() # If you are using repl.it, set host = "0.0.0.0"
```

above block of code starts flask app and runs it.

```python
@app.route("/")
def home():
  return "Hello! Welcome."
```

If you want to run the function when a certain url is posted, use above block of code. The def name does not matter.

- Need to recap what decorator is.

## Side Notes

- Useful VSCode shortcuts.

  1. To restart, `command + shift + p`, and search for <u>reload window</u>!
  2. To go to next line, `command + enter`.
  3. To open a file, `command + p`.
  4. To split the current window, `command + \`.
  5. `.DS_Store` is a file that contains the desktop service, such as position of icons or choice of backgrounds.

- To remove a file, use `os.remove`. To check if file exists, `os.path.exists`

  ```python
  import os
  os.path.exists("<url_or_filename>")
  os.remove("<url_or_filename>")
  ```

- You can simply pass a variable to `if` condition. Python automatically checks if any value is assigned to the variable.

  ```python
  if var :
  ```

  is equivalent to

  ```python
  if bool(var) :
  ```

- Computer network stuffs.
  1. Key concepts:
- learning about how computer network works. Key concepts: IP addresses, route, router, packet, hop,
- IP address is the unique identifier given to "each device" connected to the internet.
- IP address is IPv4 or IPv6. IPv4 is 32-bit. Since the growth of the internet and the depletion of the available addresses, IPv6 is introduced, which is 64-bit.
- Public IP address and private IP address. When multiple devices are connect to the same local network, their IP address are differenciated by private IP address. This is what makes about 8 billion devices possible when there are about only 4 billion available address possible in IPv4.

* PROTOCOL is a set of rules that specifies how computers should communicate with each other over a network.
* A data is divided into small pieces, packets, before it is sent. And a packet moves through multiple routers before it reaches its destination. Each jump from one router to another is called a hop.
* packets not always arrive in order when some other packets found a faster way than the others. TCP (Transport Control Protocol), however, contains the information of the order of the packet so that it can reconstruct the data no matter of the different arrival time of the packets.
* packet transfer is not guranteed. When, for example, some of mid router receives more packets than it can handle, it has to drop some of the packets. TCP checks for any loss packets by periodically sending acknowledgment packet back to the source computer. And If any loss packet is found, it send request for re-transmission.
* TCP connection: computers communicate through TCP.
