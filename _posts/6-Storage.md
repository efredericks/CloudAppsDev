> By the end of this module, you'll gain experience with storing information on and around the cloud.

> Module videos:

Inevitably, you'll be wanting to "store" things up in the cloud.

Crazy concept, yes, however sometimes we do need persistent data accessible to our various cloud (and even non-cloud) services.  Historically, data has been stored either as file-based (such as an FTP server or file share) or in databases (relational for a *long* time and non-relational for a reasonably recent time).  That's not to say that there aren't other options, but typically it'll either be files or relational data (e.g., MySQL, Microsoft SQL server, PostGreSQL, etc.).

Figure 1 shows how a "typical" database (monolithic on-premises database) might be migrated to some of the various AWS options for cloud storage.

![AWS Database Migration](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2019/01/07/reduce-database-cost-1.gif "AWS Database Migration")

> Figure 1: AWS Database Migration

On the left is the on-prem database that would be typically maintained by your local infrastructure team.  On the right are some of the technologies available to turn a database into a cloud-based service.  *Note: there is not necessarily one "correct" way to store your data in the cloud -- there are options*!

For instance, you might simply be interested in a direct migration of your files to a [cloud storage bucket](https://cloud.google.com/storage/docs/key-terms#buckets) (container for holding files/data).  Or, you may be interested in simply taking your local SQL database and putting it up into a similar database management system hosted on a virtual machine.

You can take it further as well to non-relational databases (NoSQL databases), data warehousing strategies for big data and data analytics, etc.  Basically, the decision *you* need to make is *how* your data is to be stored and *what* you want to do with it.

## Storage

## Additional Resources

* TBD