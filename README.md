# SimplePyCrawler

A simple web crawler developed as coursework for Graph Algorithms - PUC Minas 


## What is this supposed to do?

This simple script crawl hyperlinks contained on a [HTML(Hypertext Markup Language)](https://en.wikipedia.org/wiki/HTML) page from a specified domain and then it fetches the hyperlinked pages to construct a graph. The graph nodes represents the hyperlinks and the egdges indicates that there is a hyperlink reference from one page to another one (this is a directed graph). 

- **How is the graph built?** The graph is built recursively in such a way that new referenced pages are visited to search for more hyperlinks and further extend the graph. This recursive process occurs until the script complete a previously specified number of jumps. 

- **How is the graph structured?** This approach uses an [Adjacency List](https://en.wikipedia.org/wiki/Adjacency_list) to represent the graph. New hyperlinks are always added at the end of the adjacency list and thus. The hyperlinks are added following the [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) Algorithm strategy.

## How does it work?

All that you need to do is to run the script using python interpreter and type the command ```python SimplePyCrawler.py``` on a terminal, then you'll be asked to insert an url to be processed and how many jumps you want the graph to consider.
