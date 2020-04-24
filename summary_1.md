## 1.2 Tuples and Dicts

Mutable vs immutable

python standard library.

list has the standard method reverse which reverses the order of the elements in the list.
usegae => list.reverse()

you can include list or tuple or whatever datatype as dictionary key. However, the key has to be a text wrapped inside the double quotes.
test_dic = {"dic_key1" : test_list, "dic_key2" : "test_values",}

## 1.5 Custom functions

def minus(a,b=0):
print(a-b)

as in b=0, you can set the default value of the argument if the argument is not passed when the function is called.

## 1.8 Keywarded Arguments

positional arguements vs keywarded arguments

## 1.10 conditionals part one

checking the variable type
if type(b) is str :
is and is not are for checking object identity. So know the difference between ==, != and is, is not.

## 1.12 For in

for letter in "tony":
letter variable is created when the for loop starts and is erased when the loop ends. It is created for the iterate purpose. What comes after in is the element of a sequence, such as string, tuple, or list. (even the dictionary! variable will contain the key value.)

## 1.13 modules

from math import ceil, fsum as cool_sum
import math
you can import only the functions you need instead of importing the entire package. Also, you can custom name the function by using as.

## 2.0 & 2.1 What Is Web Scrapping / What Are We Building

Simple intro explaining what web scrapping is and what goal we want to achieve through web scrapper.

## 2.2 Navigating with Python

1. Setting up the environment for this project.

- pipenv --three
- pipenv shell
- pipenv requests
- set the interpreter of the vscode to the virtual environment.

2. Get the response object using request library.

- pipenv install requests
- import requests
- result = requests.get("url")
- result.text gives you the html of the page in text form. But this is super complex to look at. Thus, we will use the beautifulsoup4 library to parse this.

## 2.3 & 2.4 & 2.5 Extracting Pages

Used requests and bs4 library to make a request to the given url and extract information from the response.

- `response = requests.get(URL)`
  Gives you the response object.
- `response = requests.get(f"{URL}&start={p*LIMIT}").status_code`
  Status code gives 200 if the response was received successfully.
- `response.text`
  Gives you the string format of the page html.
- `soup = BeautifulSoup(response.text, "html.parser")`
  Pass the string format of the html into BeautifulSoup function to build the parse so that I can extract information I want.
- `lists = soup.find("div", class_={"pagination"}).find_all("span")`
  Use the find method, which takes in the name of the tag or the name of the class, to get the element you want. Syntax is as shown in the code.
- `p.string` (bs4 method)
  Gives you the text inside the element you picked.

## 2.6 & 2.7 & 2.8 Extracting Information From Each Page

Using the same principle, extract the information you want.

1. Send requests and get response of the html object of the page.
2. Parse the response using BeautifulSoup library.
3. Get the html element that contains the information you want by using find method.
4. Usually the information is stored in the attribute rather than in the text. Thus, retrieve the attribute info.
5. Store the information in the array as a form of dictionary. e.g. [{"country":country, "code":code}, ...]

- <html_obj>["title"]
  Brings the information of the title attribute. (bs4 method)

## 2.9 & 2.10 & 2.11 & 2.12 & 2.13 Extracting StackOverFlow

Same thing for the stackoverflow website.

## 2.14 & 2.15 & 2.16 Saving to CSV

Using python standard library, csv, save the extracted data to .csv file.

1. Create csv file.

- `import csv`
- `with open("jobs.csv", mode="w") as jobs_file:`
  For reading mode, mode="r"
- with clause is shorthand for try/final. Always runs exit() at the end.

2. Create writer

- `jobs_writer = csv.writer(jobs_file)`

3. Write to the file.

- `jobs_writer.writerow(["Title", "Location", "Link"])`

- os.remove("jobs.csv")
  os command for removing files.

## 3.1 The difference between \*args and \*\*kwargs.

\**kwargs, kwargs are a dictionary of keywarded arguements and *args is a list of arguements.

def myFun(\*args,\*\*kwargs):
print("args: ", args)
print("kwargs: ", kwargs)

# Now we can use both \*args ,\*\*kwargs to pass arguments to this function :

myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")

args: ('geeks', 'for', 'geeks')
kwargs {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}

## 4.1 Introduction to flask

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

## Side learning about the network stuffs.

This section is still on progress. I will come back to it later after I finish python lectures first.

- To restart, command+shift+p, and search for reload window!
- To go to next line, command + enter
- To open a file, command + p
- To split the current window, command + \
- .DS_Store is a file that contains the desktop service, such as position of icons or choice of backgrounds.
-

```python
if var :
```

is equivalent to

```python
if bool(var) :
```

- learning about how computer network works. Key concepts: IP addresses, route, router, packet, hop,
- IP address is the unique identifier given to "each device" connected to the internet.
- IP address is IPv4 or IPv6. IPv4 is 32-bit. Since the growth of the internet and the depletion of the available addresses, IPv6 is introduced, which is 64-bit.
- Public IP address and private IP address. When multiple devices are connect to the same local network, their IP address are differenciated by private IP address. This is what makes about 8 billion devices possible when there are about only 4 billion available address possible in IPv4.

* PROTOCOL is a set of rules that specifies how computers should communicate with each other over a network.
* A data is divided into small pieces, packets, before it is sent. And a packet moves through multiple routers before it reaches its destination. Each jump from one router to another is called a hop.
* packets not always arrive in order when some other packets found a faster way than the others. TCP (Transport Control Protocol), however, contains the information of the order of the packet so that it can reconstruct the data no matter of the different arrival time of the packets.
* packet transfer is not guranteed. When, for example, some of mid router receives more packets than it can handle, it has to drop some of the packets. TCP checks for any loss packets by periodically sending acknowledgment packet back to the source computer. And If any loss packet is found, it send request for re-transmission.
* TCP connection: computers communicate through TCP.
