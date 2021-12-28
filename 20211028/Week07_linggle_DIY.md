Week 07: Linggle DIY
=========================

 * See here for the rendered md file: https://hackmd.io/@Cloude/nlp-linggle-diy

From the lecture so far, we've learned word frequency ([week01][as01]), skip-gram and how to use MapReduce technique ([week05][as05]) to process a big dataset.  
Now, let's use our knowledge to implement something real! This week, we are going to build our own linguistic search engine.  


What is Linggle?
-------------------------

[Linggle][linggle] is a search engine specifically targeting gram-pattern searching.  
For example, if you are not sure whether *"in the campus"* or *"on the campus"* is correct, you can search on Linggle with the query "[on/in the campus][query1]", so you can see that *"on the campus"* is more correct.  
Another example. Suppose you are working on your paper and don't know which verb should be used to bring out your method, you can search "[we v. a method][query2]", and you can know "present a method" might be a good idea.  
As you may guess, this system is heavily based on ngram processing, so you are able to build your own Linggle as well!  


Implementation
-------------------------

Knowing what Linggle is, let's see what we should do!  

### Requirements

In this assignment, your system must support the following functionalities:

1. placeholder `_` :  
   Query with `_` means there is exactly one word in between. 
   For example, *"_ dinner"* is mapped to *have dinner*, *a dinner*, *after dinner*, etc.
2. wildcard `*` :  
   Query with `*` means there can be zero or more word(s) in between.
   For example, *"play \* role"* can be mapped to *play role*, *play a role*, *play a key role*, etc.
3. or `/` :  
   Query with `/` means you need to generate ngrams with all combinations. 
   For example, *"in/at/on the morning"* is mapped to *in the morning*, *at the morning*, and *on the morning*.  
4. optional `?` :  
   Query with a `?` preceeding a word means that word is optional. 
   For example, *"discuss ?about the issue"* should be mapped to *discuss the issue* and *discuss about the issue*. 

### Step 1: ngram frequency

We have calculated the ngram frequency for you. You can download the file, `nc.10.txt`, from the [data folder][data].  
In this file, 
 1. puctuations are all removed, and
 2. only grams with frequency > 10 is kept.  

### Step 2: mapper and reducer for index inverting

Write a **mapper** and **reducer** to generate inverted indice for all possible queries.  
You may refer to the slide for more I/O hints, and also the sample code for tiny search engine is provided [here][sample].  
Sample i/o files of mapper and reducer can be found in the [template folder][template]: `bnc.nc.sample.txt`, a smaller ngram frequency data, can be used to validate your code, while `bnc.linggle.sample.txt` is the sample result of your reducer and can be processed by `linggle.py` directly.  

### Step 3: setup your search engine

After generating your linggle database, you can start on `linggle.py` and try to interactively search for the ngrams!  
```
python linggle.py ${YOUR_INDEX_FILE}
```
\*Template for `linggle.py` is in the [template folder][template].

### Bouns (optional)

In your linggle system, you can also provide some additional features, and you will get some extra points in this assignment if you do so.  
Here are some examples:  

1. POS wildcards `v.`/`adj.`/etc. :  
   Allow users to search with part-of-speech. 
   For example, *"v. dinner"* should return *eat dinner*, *have dinner*, *make dinner*, etc., but the results shouldn't include *the dinner* or *after dinner*.  
   The file `enron.tagged.txt` already include POS information for you; you can download it from [data folder][data].
2. phrasal unit `_` :  
   Multiple words combined by `_` means they should be a phrase. 
   For example, *"going_to/will happen anyway"* should be mapped to *going to happen* and *will happen*, but not *going will happen* .  
   \*This is different from the placeholder; don't mix them up.  
3. partial match `$` :  
   If there's a `$` in the word, it's an in-word wildcard. It means you should add one or more character(s) at that place. 
   For example, *"$ing to"* should be mapped to *sing to*, *going to*, *jumping to*, etc.  
4. re-ordering `{}` :  
   If several words are grouped in curly brackets `{}`, it means that all permutations should be generated, original order ignored. 
   For example, *"where {you are}"* should be mapped to *where you are* and *where are you*.  
5. any other features you can imagine.

Also, you need to **write a simple report** to explain what you have done and why/how you do so.     
With every new feature, you gain some extra points, so we encourage you to try. Do more and earn more! ;)


TA's note
-------------------------

Don't forget to <b>[make an appoiment with TA][demo] to demo/explain your implementation <u>before <font color="red">11/4 15:30</font></u></b> .  

During the demo, you need to 

1. show us your linggle database, 
2. run `linggle.py` to interactively query ngrams, 
3. demonstrate bonus features if you have done it, and
4. show us your implementation in `mapper.py`, `reducer.py` and `linggle.py`.  

Note that **you only have 5 minutes for your demonstration**. Even that you have implemented hundreds of features, you still have only 5 mins to show off your masterpiece, so use your time wisely and make sure you cut straight to the point.  

Last but not least, **make sure you submit your `mapper.py`, `reducer.py`, `linggle.py`** and (if you do the bonus) the report to [eeclass][as07].


---

###### tags: `nlplab` 

[linggle]: https://linggle.com/
  [query1]: https://linggle.com/?q=on%2Fin+the+campus
  [query2]: https://linggle.com/?q=we+v.+a+method

[demo]: https://docs.google.com/spreadsheets/d/1QGeYl5dsD9sFO9SYg4DIKk-xr-yGjRDOOLKZqCLDv2E/edit?usp=sharing
[as01]: https://eeclass.nthu.edu.tw/course/homework/1874
[as05]: https://eeclass.nthu.edu.tw/course/homework/3285
[as07]: https://eeclass.nthu.edu.tw/course/homework/3979

[data]: https://drive.google.com/drive/folders/1zvtF3VqRZ4_AcFz_hBQUu0x8tllN3096?usp=sharing
  [sample]: https://drive.google.com/drive/folders/1s3baFZVTi0qBvsqrAZpEZwrtj4qzd6kv?usp=sharing
  [template]: https://drive.google.com/drive/folders/15N6ODRrCqZGXUis1TgpKza5jmQ0PCLlL?usp=sharing