# Exploring the HyperText Transfer Protocol

Welcome Miao Cai from Web Application Technologies and Django

**Exploring the HyperText Transfer Protocol**

You are to retrieve the following document in a browser tab with "Developer Mode" enabled so you can examine the HTTP Response headers. You may need to open the URL in a new tab, turn on developer mode, and then press refresh to get the proper data.

- <http://data.pr4e.org/intro-short.txt>

Enter the header values in each of the fields below and press "Submit".

Last-Modified:

`Sat, 13 May 2017 11.22:22 GMT`

ETag:

`1d3-54f6609240717`

Content-Length:

`467`

Cache-Control:

`max-age=0, no-cache, no-store, must-revalidate`

Content-Type:

`text/plain`

Submit

**Note:** If you look at the headers and not all of the headers are present, it may be that your browser is caching the request. Look for the `HTTP Response Code` in the developer console. Normally you should see a "200" code indicating a normal document retrieval. If you see a "304" status code, it means that your browser is likely using a cached copy of the file.
To convince your browser to actually retrieve the document, clear your browser cache and re-retrieve the document, or add a key-value pair to the URL like:

<http://data.pr4e.org/intro-short.txt?x=12345>

And then retrieve that URL. To force a fresh retrieval, simply change the value for x= to any new value and re-retrieve the page until you get a 200 status code.
GT
