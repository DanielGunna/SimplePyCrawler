# SimplePyCrawler

A simple web crawler developed as coursework for Graph Algorithms - PUC Minas 

## What is this supposed to do?
 
This simple script crawl hyperlinks contained on a [HTML(Hypertext Markup Language)](https://en.wikipedia.org/wiki/HTML) page from a specified domain and then it fetches the hyperlinked pages to construct a graph. The graph nodes represents the hyperlinks and the egdges indicates that there is a hyperlink reference from one page to another one (this is a directed graph). 
 
- **How is the graph built?** The graph is built recursively in such a way that new referenced pages are visited to search for more hyperlinks and further extend the graph. This recursive process occurs until the script complete a previously specified number of jumps. 

- **How is the graph structured?** This approach uses an [Adjacency List](https://en.wikipedia.org/wiki/Adjacency_list) to represent the graph. New hyperlinks are always added at the end of the adjacency list and thus. The hyperlinks are fetched following the [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) Algorithm strategy.

## How does it work?

The python package manager [pip](https://pip.pypa.io/en/stable/) its required to configure the environment to use this script, because it will be used to install project's dependencies. The required dependecies are listed below:

- [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [urllib3](https://urllib3.readthedocs.io/en/latest/)

Before run the configuration script ```config_env.sh```, you need to provide permission to run it by typing command ```chmod +x config_env.sh``` on a terminal. After that, you'll type ```./config_env.sh``` to run the configuration script then you'll must provide user's password, because script may require root privileges. Finally, wait for process conclude with success, certifying that errors not ocurred.

After execute all previous steps, you simply need to execute script, using a python interpreter typing the command ```python SimplePyCrawler.py``` on a terminal, then you'll be asked to insert an url to be processed and how many jumps you want the graph to consider.

## Todo 

I not intend to mantain this script anymore, but if you want to start to contribute or want to use this script on your project, below i sugest some enhancements.
  
  * Implement a most robust method to verify if an URL is valid;
  * Handle cycles on graph;
  * Implement some politeness policies on the fetch of HTML documents (such as process robots.txt, intervals between requests etc.) to avoid banning from web servers;
  * Handle fetch of urls that generate double edges.
 
