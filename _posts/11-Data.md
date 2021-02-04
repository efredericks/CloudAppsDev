> By the end of this module, you'll gain experience in dealing with all the data that your applications will need to generate and consume.

> Module videos:

> Module labs:

## Data (More Specifically - of the Big Variety)

It is now time to discuss **data**, or more commonly, that thing you have to deal with on a daily basis.  Data can be anything, from user input to usage patterns to consumed weather data.  Your cloud applications will most likely be managing data of some kind.

If you're in the cloud realm, there is a reasonable chance that your data is going to be "big."  Big data is a very timely topic, however its definition is constantly changing (mainly due to the result at which data changes).  Previously, data was in the gigabyte range to be considered "big."  Now, we're in the peta/zetabyte range and need to be able to deal with absolutely massive *streams* of information.  Figure 1 (c/o Google) shows you a nice little visualization of what we mean by "big."

![Petabyte Size](/CloudAppsDev/assets/images/11-data-size.png "Petabyte size")

> Figure 1: Petabyte Size

That's talking about petabytes.  Already in the various big data-related outlets they're discussing zetabytes of data (hint: a scale factor more than petabytes).  *That* is how much data you have to deal with.  However, a petabyte really isn't all that much at scale.  Figure 2 (c/o Google) shows how little data can be stored within a petabyte:

![Petabyte Size - Inverted](/CloudAppsDev/assets/images/11-data-size-invert.png "Petabyte Size - Inverted") 

> Figure 2: Petabyte Size - Inverted

Before we talk about the cloud services we can use to manage and analyze our data, let's talk about the other factors that comprise big data.  The following image (c/o Edureka) presents a pretty reasonable overview of the more "standard" V's that big data is known for:

![5 V's of Big Data (c/o Edureka)](https://www.edureka.co/blog/wp-content/uploads/2018/06/Five-Vs-of-Big-Data-What-is-Big-Data-Edureka.png "5 V's of Big Data (c/o Edureka)")

> 5 V's of Big Data (c/o Edureka)

Some places list way more V's, some way less, though 5 is typically accepted as representative of big data.  The reason why we call them "V's" should be clear -- they all start with V.

* **Volume**

Big data, at its heart, means that there is a massive amount of information to store, analyze, and sift through.  A standard SQL installation will typically falter with this amount of data.  Again, we're in the peta/zetabyte range (as of 2021 anyway).  

* **Velocity**

Velocity is the speed at which data comes in and leaves our applications.  Consider the various social media platforms and all of the live posts, updates, photos, videos, etc. that are constantly being posted by everybody worldwide.  The speed at which the underlying applications must handle that data (e.g., how do you quickly and reliably pull up your friend information such that the user doesn't notice the lag in searching for a `SELECT * FROM FRIENDS WHERE ID='you'` type of search?  If you don't know what I'm getting at, the prior SQL-ish search would be *super-slow* for a large amount of data.

* **Variety**

One consideration for big data is that the *format* of the data is generally open to interpretation.  In normal database applications you enforce a schema that formats each table.  Big data is generally schema-less (i.e., NoSQL-type applications) as we don't necessarily know in which format the data will be arriving (and/or leaving).  Data could be an image, a sensor value, a long-winded blog post.  It is up to your applications to handle the data and format it appropriately.

* **Veracity**

Do you trust the data coming in?  Is it possible that it is malformed, or worse, malicious?  With large amounts of streaming data from multiple sources you will need to ensure that there is little to no uncertainty in your data, as that can very quickly corrupt your database and/or application!  Maybe there are inconsistencies resulting from the same data reported from multiple sources.  Your application must be prepared for this!

* **Value**

This is the "business/marketing" side of big data, however also very *very* important for those companies concerned with the business of **data analytics**.  Without diverting into the deep, dark field of analytics, Value effectively means what you are able to get out of your data.  Specifically, what business decisions can we make as a result of analyzing the data?  Is our data valuable or worthless (and do we keep it if it is worthless?).

## Fortunately, the Cloud 

As you would expect by this point, there are several cloud services to help us manage big data for our applications.  Per usual, we'll talk about them in terms of Google Cloud, however similar services exist in Azure/AWS.  We'll be mainly looking at this in terms of *managed services* (mild shock) that we can leverage to do all the heavy lifting for us.  Here are the main services we'll be looking at in Google Cloud (with their other provider analogues):

* [**Dataproc**](https://cloud.google.com/dataproc/)
  * Amazon analogue - [AWS EMR](https://aws.amazon.com/emr/)
  * Microsoft analogue - [Azure Hindsight](https://azure.microsoft.com/en-us/services/hdinsight/)

Dataproc (and similar) are going to be your engines for processing big data.  Common strategies leverage Hadoop/Spark for working with data.  These are open-source technologies that can be used for handling massive amounts of unstructured data.

* [**Dataflow**](https://cloud.google.com/dataflow)
  * Amazon analogue = [AWS Data Pipeline](https://aws.amazon.com/datapipeline/)
  * Microsoft analogue = [Azure Data Factory](https://azure.microsoft.com/en-us/services/data-factory/)

You may be interested in streaming data.  Streaming data effectively has you analyze and manage data as it arrives in real time, and can typically be setup as a streaming or batch processing service.

* [**BigQuery**](khttps://cloud.google.com/bigquery)
  * Amazon analogue = [AWS Redshift](https://aws.amazon.com/redshift/)
  * Microsoft analogue = [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/)

You will also probably need to manage analytics at some point as well (or, analyzing your data).  Essentially, you will take what you know of common database queries (think: SQL) and translate them to higher-order services for quickly searching for, understanding, and leveraging your data.  Data warehousing was the precursor to this area.

## Dataproc

First of all, let's talk about [Hadoop](https://hadoop.apache.org/) and [Spark](https://spark.apache.org/) (both open-source projects from Apache).  You will often find these two technologies in big data applications.  **Hadoop** effectively ties together computers/servers in a cluster to enable distribution and processing of data, and **Spark** is an analytics engine for large-scale data processing (both in stream form and batch form).  **Dataproc** then ties these two technologies together as a managed service.  With Dataproc clusters can be spun up quickly, managed, and run in an ephemeral fashion (i.e., you save money when they're off). Figure X (c/o Google) shows an overview of Dataproc and its sub-services:

![Dataproc Overview](/CloudAppsDev/assets/images/11-dataproc.png "Dataproc Overview")

> Figure X: Dataproc Overview

Here are some quotes from Google on the key Dataproc features:

> Dataproc is priced at 1 cent per virtual CPU per cluster per hour, on top of any other Google Cloud resources you use. In addition, Dataproc clusters can include preemptible instances that have lower compute prices. You use and pay for things only when you need them.
> Dataproc clusters are quick to start, scale, and shutdown, with each of these operations taking 90 seconds or less, on average. Clusters can be created and scaled quickly with a variety of virtual machine types, disk sizes, number of nodes, and networking options.
> You can use Spark and Hadoop tools, libraries, and documentation with Dataproc. Dataproc provides frequent updates to native versions of Spark, Hadoop, Pig, and Hive, so there’s no need to learn new tools or APIs, and it’s possible to move existing projects or ETL pipelines without redevelopment.
> You can easily interact with clusters and Spark or Hadoop jobs, without the assistance of an administrator or special software, through the Cloud Console, the Cloud SDK, or the Dataproc REST API. When you're done with a cluster, simply turn it off, so money isn’t spent on an idle cluster.
> Image versioning allows you to switch between different versions of Apache Spark, Apache Hadoop, and other tools.
> The built-in integration with Cloud Storage, BigQuery, and Cloud Bigtable ensures data will not be lost. This, together with Cloud Logging and Cloud Monitoring, provides a complete data platform and not just a Spark or Hadoop cluster. For example, you can use Dataproc to effortlessly ETL terabytes of raw log data directly into BigQuery for business reporting.


## Additional Resources

* TBD

<hr size="1" />

*Where noted, the original content was provided by Google LLC and modified for the purpose of the course, without input or endorsement from Google LLC*.