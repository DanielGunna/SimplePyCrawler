# SimplePyCrawler

A simple web crawler developed as coursework for Algorithms on Graph Theory - PUC Minas 


# What's this supposed to do ?

This simple script make requests to get hyperlinks contained on a [HTML(Hypertext Markup Language)](https://en.wikipedia.org/wiki/HTML) page from a specified domain. The main objective is to build a [undirected graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Undirected_graph) where nodes represents the hyperlinks and there is edge between two nodes when the hyperlinks represented by those nodes references each other. The process of build the graph is recursive, so the new hyperlinks added to graph will be visited and the hyperlinks contained on HTML pages referenced by those hyperlinks will be added to graph and visited and so on... this recursive process will occur until the script complete a specified number of jumps, thus the number of jumps controls how recursion can be more "deepiest". The approach used to represent the graph was the [Adjacency List](https://en.wikipedia.org/wiki/Adjacency_list) approach. The new hyperlinks will be always added on the end of the list, so the way that script handles the visit to fetch of new HTML pages is the strategy of [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) Algorithm.

# How it works ?

All that you need to do is run the script, using python interpreter typing the command  ```python SimplePyCrawler.py``` on a terminal, then you'll be asked to insert an url to be processed and the number of jumps.

# Todo 

I not intend to mantain this script anymore, but if you want to start to contribute or want to use this script on your project, below i sugest some enhancements.
  
  * Implement a most robust method to verify if an URL is valid;
  * Handle cycles on graph;
  * Implement some politeness policies on the fetch of HTML documents (such as process robots.txt, intervals between requests etc.) to avoid banning from web servers;
  * Handle fetch of urls that generate double edges.
