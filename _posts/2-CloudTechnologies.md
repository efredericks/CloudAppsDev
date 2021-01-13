
> By the end of this module, you will know what cloud computing can be used for, how to enable a cloud API, and how to navigate the cloud shell.

> Module Video: TBD

## Cloud Technologies

The benefit of using cloud technologies are that you are effectively using somebody else's servers.  The downside is that you are limited to the technologies supported by that provider.  For instance, you will probably be hard-pressed to try and use BigQuery (Google-specific technology for sifting through massive datasets) on DigitalOcean.  However, you may not need that technology!  (Again, consider all tradeoffs when selecting a provider).  

Since we are using Google Cloud for this course, we are going to focus on the technologies supported by Google.  Here is a page with the [full list of Google Cloud services](https://cloud.google.com/products).

*For reference, here are the products supported by [AWS](https://aws.amazon.com/products/) and [Microsoft Azure](https://azure.microsoft.com/)*.

You will notice a lot of overlap!  Consider that each are competing for *cloud dominance* and that each provider wants *you* to pay for their service.


ASSIGNMENT: WRITEUP 5 SERVICES

### IaaS vs. PaaS vs. SaaS

> Module video TBD

There are three different (main) paradigms when it comes to cloud computing.  You more than likely have seen these acronyms before, however we should still define them for propriety's sake.  First, we have **Infrastructure as a Service (IaaS)**, then **Platform as a Service (PaaS)**, and **Software as a Service (SaaS)**.  Each of these terms effectively means transitioning your *thing* to become a cloud-based service. 

> If you are getting lost with these acronyms, reflect on that first word.  It is the key to what is being turned into a service.

Figure 1 presents a sample (c/o Google) of some of their different categories of cloud services.  On the left you see Compute Engine, which is their IaaS platform.  There are a lot of options available within Compute Engine, however the most prominent/well-known tends to be virtual machines.  Next you have App Engine, their PaaS platform.  App Engine enables you to create applications without having to worry about pesky things like servers or virtual machines.  Not pictured but still available is the SaaS applications, where these tend to be the "other" cloud services you have (and will vary from provider to provider).  Here, the main consideration is not the service but the software -- effectively you put data in, have some sort of "transformation" occur, and receive changed data out.  Consider applications such as translate (e.g., Google Translate) or machine learning (e.g., TensorFlow) and you have SaaS.  No servers to configure, no applications to develop, simply configure the application to your needs and feed it data.

![Google Cloud Service Options](/CloudAppsDev/assets/images/1-iaas-paas.png "Google Cloud Service Options]")

> Figure 1: Google Cloud Service Options

Next, we'll highlight some of the more common aspects of cloud computing that you are most likely to run into.

> Want a different perspective?  Check out this post: [https://www.bigcommerce.com/blog/saas-vs-paas-vs-iaas/](https://www.bigcommerce.com/blog/saas-vs-paas-vs-iaas/)

### Virtual Machines [IaaS]

One of the more common cloud services that are available are virtual machines (VM).   These are effectively computers that you can setup that are accessible anywhere you have a network connection (and the necessary technology to access it -- for Google Cloud it is simply a browser).   Figure 2 shows you a common VM concept, normal vs. sole tenancy.  The concept here is that sole tenant nodes are strictly provisioned to you and your workloads -- there are no other users sharing that host.  

![Google Cloud Normal Host vs. Sole-tenant node](https://cloudx-bricks-prod-bucket.storage.googleapis.com/d5c9cad33f729dc110d8b907db5a695ca9cf6b0f4b692f44f0f2c0e276d78369.svg "Google Cloud Normal Host vs. Sole-tenant node]")

> Figure 2: Normal vs. Sole-tenant nodes

Figure 3 then shows off a sample VM that I created for one of the labs we're working through.  Here, you see the instance name, a bit of information about the VM that is relevant (machine type, logging availability, CPU, etc.).  Effectively, you can pick what type of machines you want, where you want them located, and what operating systems to load onto them.  These can be provisioned as necessary for your environment, including scaling as needed.

### Virtual Networks [IaaS]

### Cloud Storage [IaaS]

### Internet of Things [IaaS/PaaS]

### Microservices [PaaS/SaaS/Somewhere In-Between]

Microservices tend to fall into the buzzwordy camp (for me at least), but at their core they tend to be the result of breaking up larger applications into more bite-sized pieces.  Typically the end up being small portions of an application that have been migrated to functions that accept data and transform it (or relay it) in some fashion.  There are multiple approaches for creating microservices, however in the cloud realm you may wish to consider using a serverless technology such as Cloud Functions (or Lambda/Azure Functions) or an App Engine (PaaS) type of environment.  

Both approaches are completely feasible and both rely on code development.  Figure X shows an example of a microservice architecture (c/o microservices.io).  Here, you see multiple aspects of what typically would be a monolithic application broken down into manageable services, each accessible via some sort of endpoint (e.g., web, API, RESTful call, etc.).

![Microservice Architecture](https://microservices.io/i/Microservice_Architecture.png "Microservice Architecture")

> Figure X: Microservice Architecture

### Containers / Orchestration

[Kubernetes](https://kubernetes.io/) (or K8s)

### Analytics / Artificial Intelligence / Machine Learning [SaaS]

### Data Management [SaaS]

### Recovery

### Performance

vms
virt networks
services
iot
microservices
containers
analytics
data mgmt
recovery


> Demos - website hosting, failover network, API, cloud shell

## Cloud Shell

  
## Codelabs

## QwikLabs

## Colabs

## Additional Resources

* [Codelab: Getting Started with Cloud Shell & gcloud](https://codelabs.developers.google.com/codelabs/cloud-shell/#0)
* [Running gcloud Commands with Cloud Shell](https://cloud.google.com/shell/docs/running-gcloud-commands)
* [IaaS vs PaaS vs SaaS Enter the Ecommerce Vernacular: What You Need to Know, Examples & More](https://www.bigcommerce.com/blog/saas-vs-paas-vs-iaas/)