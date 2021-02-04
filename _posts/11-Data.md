> By the end of this module, you'll gain experience in dealing with all the data that your applications will need to generate and consume.

> Module videos:

> Module labs:

## Data (More Specifically - of the Big Variety)

It is now time to discuss **data**, or more commonly, that thing you have to deal with on a daily basis.  Data can be anything, from user input to usage patterns to consumed weather data.  Your cloud applications will most likely be managing data of some kind.

If you're in the cloud realm, there is a reasonable chance that your data is going to be "big."  Big data is a very timely topic, however its definition is constantly changing (mainly due to the result at which data changes).  Previously, data was in the gigabyte range to be considered "big."  Now, we're in the peta/zetabyte range and need to be able to deal with absolutely massive *streams* of information.

Before we talk about the cloud services we can use to manage and analyze our data, let's talk about the other factors that comprise big data.  The following image (c/o Edureka) presents a pretty reasonable overview of the more "standard" V's that big data is known for:

![5 V's of Big Data](https://www.edureka.co/blog/wp-content/uploads/2018/06/Five-Vs-of-Big-Data-What-is-Big-Data-Edureka.png "5 V's of Big Data")

> 5 V's of Big Data

Some places list way more V's, some way less, though 5 is typically accepted as representative of big data.  The reason why we call them "V's" should be clear -- they all start with V.

* Volume

Big data, at its heart, means that there is a massive amount of information to store, analyze, and sift through.  A standard SQL installation will typically falter with this amount of data.  Again, we're in the peta/zetabyte range (as of 2021 anyway).  

* Velocity

Velocity is the speed at which data comes in and leaves our applications.  Consider the various social media platforms and all of the live posts, updates, photos, videos, etc. that are constantly being posted by everybody worldwide.  The speed at which the underlying applications must handle that data (e.g., how do you quickly and reliably pull up your friend information such that the user doesn't notice the lag in searching for a `SELECT * FROM FRIENDS WHERE ID='you'` type of search?  If you don't know what I'm getting at, the prior SQL-ish search would be *super-slow* for a large amount of data.

* Variety

One consideration for big data is that the *format* of the data is generally open to interpretation.  In normal database applications you enforce a schema that formats each table.  Big data is generally schema-less (i.e., NoSQL-type applications) as we don't necessarily know in which format the data will be arriving (and/or leaving).  Data could be an image, a sensor value, a long-winded blog post.  It is up to your applications to handle the data and format it appropriately.

* Veracity

Do you trust the data coming in?  Is it possible that it is malformed, or worse, malicious?  With large amounts of streaming data from multiple sources you will need to ensure that there is little to no uncertainty in your data, as that can very quickly corrupt your database and/or application!  Maybe there are inconsistencies resulting from the same data reported from multiple sources.  Your application must be prepared for this!

* Value

This is the "business/marketing" side of big data, however also very *very* important for those companies concerned with the business of **data analytics**.  Without diverting into the deep, dark field of analytics, Value effectively means what you are able to get out of your data.  Specifically, what business decisions can we make as a result of analyzing the data?  Is our data valuable or worthless (and do we keep it if it is worthless?).

## 


## Additional Resources

* TBD

<hr size="1" />

*Where noted, the original content was provided by Google LLC and modified for the purpose of the course, without input or endorsement from Google LLC*.