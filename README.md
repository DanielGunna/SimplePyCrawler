# SimplePyCrawler

A simple web crawler developed as coursework for Graph Algorithms - PUC Minas 

## What is this supposed to do?
 
This simple script crawl hyperlinks contained on a [HTML(Hypertext Markup Language)](https://en.wikipedia.org/wiki/HTML) page from a specified domain and then it fetches the hyperlinked pages to construct a graph. The graph nodes represents the hyperlinks and the egdges indicates that there is a hyperlink reference from one page to another one (this is a [directed graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Directed_graph)). 
 
- **How is the graph built?** The graph is built recursively in such a way that new referenced pages are visited to search for more hyperlinks and further extend the graph. This recursive process occurs until the script complete a previously specified number of jumps. 

- **How is the graph structured?** This approach uses an [Adjacency List](https://en.wikipedia.org/wiki/Adjacency_list) to represent the graph. New hyperlinks are always added at the end of the adjacency list and thus. The hyperlinks are fetched following the [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) Algorithm strategy.

## How does it work?

The python package manager [pip](https://pip.pypa.io/en/stable/) is required to configure the environment to use this script, because it will be used to install project's dependencies. The required dependecies are listed below:

- [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [urllib3](https://urllib3.readthedocs.io/en/latest/)

Before running the ```config_env.sh``` configuration script you need to provide permission to run it by typing ```chmod +x config_env.sh``` in a terminal. Afterwards, you have to type ```./config_env.sh``` to run the configuration script, which requires user's password because it is a procedure that may require root privileges. Finally, wait for process conclude.

After you have executed all previous steps, you simply need to execute script using a python interpreter by typing the ```python SimplePyCrawler.py``` command in a terminal. Then, you will be asked to insert an url to be processed and choose how many jumps you want the graph to consider.

## Todo 

I do not intend to mantain this script anymore. If you want to contribute or simply would like to use this script on your project,  below there are some enhancements suggestions.
  
  * Implement a more robust method to verify if an URL is valid;
  * Handle graph cycles;
  * Implement politeness in the HTML documents fetching process (such as respecting robots.txt and adding some time before repating requests) to avoid having your bot/IP banned from web servers;
  * Handle url fetching that generates double edges.
 
