> By the end of this module, you'll gain experience with storing information on and around the cloud.

> Module videos:
> * [Cloud Datatypes [16:38]](https://youtu.be/HVvoLTspxzs)
> * [Cloud Storage Overview [9:54]](https://youtu.be/cJh_naOJ-qM)
> * [Cloud Storage / Cloud Shell Demo [8:45]](https://youtu.be/_rFd7lRsDOQ)
> * [Cloud Storage / Cloud Functions / DLP demo (1/2) [15:21]](https://youtu.be/eX9yGgVU_5I)
> * [Cloud Storage / Cloud Functions / DLP demo (2/2) [16:10]](https://youtu.be/zmhFTUioSkU)
> * [Cloud Datastore Demo [13:39]](https://youtu.be/y9T9Xm7oge0)
> * [Cloud Spanner Demo [10:56]](https://youtu.be/1r7rY6BKmUY)

Inevitably, you'll be wanting to "store" things up in the cloud.

Crazy concept, yes, however sometimes we do need persistent data accessible to our various cloud (and even non-cloud) services.  Historically, data has been stored either as file-based (such as an FTP server or fGile share) or in databases (relational for a *long* time and non-relational for a reasonably recent time).  That's not to say that there aren't other options, but typically it'll either be files or relational data (e.g., MySQL, Microsoft SQL server, PostGreSQL, etc.).

Figure 1 shows how a "typical" database (monolithic on-premises database) might be migrated to some of the various AWS options for cloud storage.

![AWS Database Migration](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2019/01/07/reduce-database-cost-1.gif "AWS Database Migration")

> Figure 1: AWS Database Migration

On the left is the on-prem database that would be typically maintained by your local infrastructure team.  On the right are some of the technologies available to turn a database into a cloud-based service.  *Note: there is not necessarily one "correct" way to store your data in the cloud -- there are options*!

For instance, you might simply be interested in a direct migration of your files to a [cloud storage bucket](https://cloud.google.com/storage/docs/key-terms#buckets) (container for holding files/data).  Or, you may be interested in simply taking your local SQL database and putting it up into a similar database management system hosted on a virtual machine.

You can take it further as well to non-relational databases (NoSQL databases), data warehousing strategies for big data and data analytics, etc.  Basically, the decision *you* need to make is *how* your data is to be stored and *what* you want to do with it.

> Module video: [Cloud Datatypes [16:38]](https://youtu.be/HVvoLTspxzs)

## Storage

> Module Video: [Cloud Storage Overview [9:54]](https://youtu.be/cJh_naOJ-qM)

Focusing on Google now, let's take a look at what options are available to you as a developer.

> Note: you can interact with all of these products via the Cloud console (web interface) or the Cloud shell (CLI).

Figure 2 shows the currently-available options (c/o Google):

![Google Cloud Storage Options](/CloudAppsDev/assets/images/6-cloud-storage.png "Cloud Storage Options")

> Figure 2: Google Cloud Storage Options

This figure is helpful in that it also identifies the *type* of storage that each service provides.  For instance, you have access to your typical relational databases (Cloud SQL, Cloud Spanner), non-relational (i.e., NoSQL) databases (Datastore, Cloud BigTable), and data warehousing (BigQuery).  Cloud Storage is a place to store files and data objects.  As with *any* infrastructure activity, selecting the correct type of storage is an important task.

I will leave the selection process to the more appropriate database/systems administration courses (Google provides a handy flowchart that I've included later in this post).  Considerations though:

* All applications and services will most likely need to create, store, retrieve, and consume data.  This includes text files, images, application data, etc.  Selecting the appropriate storage option can help you speed up response times, save costs, and enhance flexibility.
* Cloud-based storage options have the benefits that other services do in that they are provisionable on-demand and are highly-scalable.
* Relational vs. non-relational can be a religious debate to some, however if you have a small-scale application that you never plan to grow it may not make sense to use the full power of a data warehousing strategy.  Likewise, a massive social network-type application where data is constantly changing will perform poorly on a standard relational database.  Choose the appropriate tool!

For reference, Microsoft Azure has a similar set of available options, as shown in Figure 3 (c/o dremio.com):

![Microsoft Azure Storage Options](https://www.dremio.com/img/explained/azure-storage/image_0.png "Microsoft Azure Storage Options")

> Figure 3: Microsoft Azure Storage Options

> * Module video: [Cloud Storage / Cloud Shell Demo [8:45]](https://youtu.be/_rFd7lRsDOQ)

We also can do some other nifty things with Cloud Storage.  In this next demo, we'll hook up Cloud Storage, Cloud Functions, and the DLP API:

* Link to [Codelab](https://codelabs.developers.google.com/codelabs/cloud-storage-dlp-functions)
* Link to [Medium article where you can find the correct GitHub repository](https://medium.com/google-cloud/automating-cloud-storage-data-classification-dlp-api-and-cloud-function-7546b3763203)

> * Module video: [Cloud Storage / Cloud Functions / DLP demo (1/2) [15:21]](https://youtu.be/eX9yGgVU_5I)
> * Module video: [Cloud Storage / Cloud Functions / DLP demo (2/2) [16:10]](https://youtu.be/zmhFTUioSkU)

## Structured vs. Unstructured Data

This discussion is best suited for a proper database course (normalization anybody?), so you get the highlights here.  First and foremost, data that you put into a database must be considered very carefully before you begin (or even before you begin transforming an existing database application to a cloud-based application).

Let's start with relational (i.e., structured) data.  This tends to be data best represented in spreadsheet form (rows, columns, etc.).  This type of data would be your typical web application, billing information, etc.  Structured data is pretty well-understood at this point both from a theoretical perspective and from a programming perspective.  Data manipulation in the relational/structural world tends to be straightforward.

Unstructured data, however, has no organization.  It is *unstructured* by nature, meaning it is schema-less.  What this means is that there is nothing in the database system enforcing table format.  For example, if you create an unstructured object for storing customer information, it is up to you/your application to enforce how usernames, customer names, email addresses, etc., are stored within that object.  The database itself does not care!

Common relational database systems include MySQL/MariaDB, PostGreSQL, SQLite, and Microsoft SQL Server (and Access, though we don't talk about that (ง'̀-'́)ง).  If you are working in industry, more than likely you have come across one of these.

Common non-relational/unstructured/NoSQL databases include MongoDB, CouchDB, Neo4J, and BigTable.  These types of databases generally have their own particular methods of access and manipulation, whereas the relational databases all implement some form of SQL.  For example, Neo4J uses the Cypher language to manipulate a database graph, whereas MongoDB uses JSON-style objects to store information and can be manipulated via API calls.

Figure 4 (c/o Google) presents a view of structured vs. unstructured data.  

![Google Cloud - Structured vs. Unstructured Data](/CloudAppsDev/assets/images/6-cloud-data-type.png "Google Cloud - Structured vs. Unstructured Data")

> Figure 4: Google Cloud - Structured vs. Unstructured Data

To illustrate the difference that you may see with an unstructured database environment, Figure 5 (c/o Neo4j) shows a graph-based database.  In this system, the *relationships* between objects are generally most important, with each object being a self-contained entity.

![Sample Neo4j database](https://dist.neo4j.com/wp-content/uploads/20180103014233/data-profiling-neo4j-apoc-library.png "Sample Neo4j database")

> Figure 5: Sample Neo4j database

## What do I use?

This is the "hard" question, as there are just so many available services and technologies out there to use.  Figure 6 shows a decision tree (c/o Google) for picking a Google-specific storage technology.  Note that you can use this flowchart to make similar decisions in other cloud provider ecosystems!

![Google Cloud Storage Selection Strategy](/CloudAppsDev/assets/images/6-cloud-selection.png "Google Cloud Selection Strategy")

> Figure 6: Google Cloud Storage Selection Strategy

The figure is fairly self-explanatory, however some key decisions you must consider are:

* Do I want my data be structured or unstructured (i.e., relational vs. NoSQL)?
* Do I need my application to be scalable or not (i.e., how many users am I expecting to have AND will it be bursty or fairly even in usage)?
* What sort of performance do I need out of it?
* How much data do I plan to store?

Next, we'll do a couple of examples with the different technologies available in Google Cloud.

## Example

As we've discussed, you have multiple options for data storage.  Here, we'll focus on examples for the two *categories* of data: structured and unstructured.

### Structured Example

With structured data, typically you're looking to model something fairly *relational* in nature (i.e., a normal database).  For this example we'll take a look at Cloud Spanner, a tool that aims to give you the feel of a normal database with the scalability features of a non-relational database.

> Module video: [Cloud Spanner Demo [10:56]](https://youtu.be/1r7rY6BKmUY) 

Links to the demo article: [https://cloud.google.com/spanner/docs/query-syntax#appendix_a_examples_with_sample_data](https://cloud.google.com/spanner/docs/query-syntax#appendix_a_examples_with_sample_data)

And how to use Python with it: [https://cloud.google.com/spanner/docs/getting-started/python](https://cloud.google.com/spanner/docs/getting-started/python)

### Unstructured Example

Here, you might go for BigTable if you're looking to manage data considered 'big data,' however we'll focus on Cloud Datastore as that may be more tenable for everyday applications.

> Module Video: [Cloud Datastore Demo [13:39]](https://youtu.be/y9T9Xm7oge0)

Cloud Datastore - [https://codelabs.developers.google.com/codelabs/cloud-spring-datastore/](https://codelabs.developers.google.com/codelabs/cloud-spring-datastore/)

## Lab

Let's do something fun now that you have gained some experience with the more 'standard' methods of handling data (both structured and unstructured).  Let's use BigTable
https://codelabs.developers.google.com/codelabs/bigtable-keyviz-art-hbase-java#0


## Additional Resources

* [Cloud Storage Bucket](https://cloud.google.com/storage/docs/key-terms#buckets) 

<hr size="1" />

*Where noted, the original content was provided by Google LLC and modified for the purpose of the course, without input or endorsement from Google LLC*.