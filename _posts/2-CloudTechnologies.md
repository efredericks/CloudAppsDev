
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

Figure 1 presents a sample (c/o Google) of some of their different categories of cloud services.  On the left you see Compute Engine, which is their IaaS platform.  There are a lot of options available within Compute Engine, however the most prominent/well-known tends to be virtual machines.  Next you have App Engine, their PaaS platform.  App Engine enables you to create applications without having to worry about pesky things like servers or virtual machines.  On the right are the SaaS applications, where these tend to be the "other" cloud services you have (and will vary from provider to provider).  Here, the main consideration is not the service but the software -- effectively you put data in, have some sort of "transformation" occur, and receive changed data out.  Consider applications such as translate (e.g., Google Translate) or machine learning (e.g., TensorFlow) and you have SaaS.  No servers to configure, no applications to develop, simply configure the application to your needs and feed it data.

![Google Cloud Service Options](/CloudAppsDev/assets/images/1-iaas-paas.png "Google Cloud Service Options]")

> Figure 1: Google Cloud Service Options

Next, we'll highlight some of the more common aspects of cloud computing that you are most likely to run into.

> Want a different perspective?  Check out this post: [https://www.bigcommerce.com/blog/saas-vs-paas-vs-iaas/](https://www.bigcommerce.com/blog/saas-vs-paas-vs-iaas/)

### Virtual Machines [IaaS]

One of the more common cloud services that are available are virtual machines (VM).   These are effectively computers that you can setup that are accessible anywhere you have a network connection (and the necessary technology to access it -- for Google Cloud it is simply a browser).   Figure 2 shows you a common VM concept, normal vs. sole tenancy.  The concept here is that sole tenant nodes are strictly provisioned to you and your workloads -- there are no other users sharing that host.  

![Google Cloud Normal Host vs. Sole-tenant node](https://cloudx-bricks-prod-bucket.storage.googleapis.com/d5c9cad33f729dc110d8b907db5a695ca9cf6b0f4b692f44f0f2c0e276d78369.svg "Google Cloud Normal Host vs. Sole-tenant node")

> Figure 2: Normal vs. Sole-tenant nodes

Figure 3 then shows off a sample VM that I created for one of the labs we're working through.  Here, you see the instance name, a bit of information about the VM that is relevant (machine type, logging availability, CPU, etc.).  Effectively, you can pick what type of machines you want, where you want them located, and what operating systems to load onto them.  These can be provisioned as necessary for your environment, including scaling as needed.

![Sample Virtual Machine](/CloudAppsDev/assets/images/1-sample-vm.png "Sample Virtual Machine")

> Figure 3: Sample Virtual Machine

With VMs comes other options as well, such as virtual networks, persistent storage, and everything you need to make a fully virtualized ecosystem.  For example, Figure 4 shows off a virtual private cloud (VPC) network architecture (c/o Google). Here, you can specify firewalls, subnets, etc.:

![VPC network](https://cloud.google.com/vpc/images/vpc-overview-example.svg "VPC network")

> Figure 4: VPC network

Note there are different regions specified as well!  These can correlate to geographic locations of your customers/clients and provide a better quality of service.

### Internet of Things [IaaS/PaaS]



### Microservices [PaaS/SaaS/Somewhere In-Between]

Microservices tend to fall into the buzzwordy camp (for me at least), but at their core they tend to be the result of breaking up larger applications into more bite-sized pieces.  Typically the end up being small portions of an application that have been migrated to functions that accept data and transform it (or relay it) in some fashion.  There are multiple approaches for creating microservices, however in the cloud realm you may wish to consider using a serverless technology such as Cloud Functions (or Lambda/Azure Functions) or an App Engine (PaaS) type of environment.  

Both approaches are completely feasible and both rely on code development.  Figure X shows an example of a microservice architecture (c/o microservices.io).  Here, you see multiple aspects of what typically would be a monolithic application broken down into manageable services, each accessible via some sort of endpoint (e.g., web, API, RESTful call, etc.).

![Microservice Architecture](https://microservices.io/i/Microservice_Architecture.png "Microservice Architecture")

> Figure X: Microservice Architecture

### Containers / Orchestration

Containers and [Kubernetes](https://kubernetes.io/) (or K8s) are a discussion in and of themselves, however they offer an extremely attractive proposition for both IT and developers alike: a sane environment that can be deployed anywhere without needing to worry about specifics like machine type or operating system.  Effectively containers become a light VM environment that enables cross-platform deployments.  Kubernetes offers orchestration of containers, in essence, container management at scale.  Figure X (c/o [DZone](https://dzone.com/articles/how-kubernetes-works)) shows a sample Kubernetes architecture, including multiple worker nodes that contain Docker containers. 

![Kubernetes Sample Architecture](/CloudAppsDev/assets/images/2-k8s-dzone.png "Kubernetes Sample Architecture")

> Figure X: Kubernetes Sample Architecture

### Analytics / Artificial Intelligence / Machine Learning [SaaS]



### Data Management [SaaS]

Many of the APIs available in the cloud provide some sort of data management and/or transformational capabilities.  When we talk about management however, we generally are discussing some form of data storage.  In Google Cloud this is BigQuery, a data management system that scales up to the big data range.  As you'll see later, there is also a specific Cloud shell program (`bq`) to interact directly with your data.  With BigQuery comes application interaction, varying forms of database commands (both SQL and BigQuery specific), and analytics capabilities.  We'll go into more detail on BigQuery (and its associated storage technique BigTable) later on. 

### Recovery and Performance


> Demos - website hosting, failover network, API, cloud shell

## Cloud Shell

> Module video: TBD

Cloud Shell (or th eCloud SDK) is a command-line interface (CLI) for interacting with Google Cloud services, plus it provides a Linux-like interface that you may be familiar with.  Here are the Google-specific commands to become familiar with:

* `gcloud`

`gcloud` is your main interface with Google Cloud via the CLI.  You can perform authentication, change your local configuration (e.g., project ID, user account, etc.), and interact with the various APIs.  For instance, one of your labs will have you using `gcloud` to deploy and re-deploy App Engine programs.

* `gsutil`

`gsutil` allows you to work with [Cloud Storage buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets) and objects.  Effectively, this is your program for working with files and data that you are keeping in persistent storage.

* `bq`

`bq` interacts with [BigQuery](https://cloud.google.com/bigquery/), Google's service for interacting with large datasets.  Here, you can run queries, manipulate datasets/tables, and other entities that are part of the BigQuery ecosystem.

Figure X shows a sample screenshot of my Google Cloud console, with Cloud Shell activated.  Note that you can open it by clicking the little terminal icon at the top right, and it will pop open the shell in the bottom of your screen.  

![Cloud Shell Screenshot](/CloudAppsDev/assets/images/2-cloud-shell.png "Cloud Shell Screenshot")

> Figure X: Cloud Shell Screenshot

Note, for each of these commands, you can add the `--help` parameter to get more information about the tool and how it can be used.  For example, entering `gcloud --help` shows information about the `gcloud` command itself, and `gcloud app --help` shows information about how to interact with App Engine via `gcloud`.  Further note, as this is effectively a Linux terminal, hitting `q` will escape the manual page that pops up whenever you look at the help files.

### Text Editing

One thing you will be doing often in this course is writing/updatining files within the Cloud shell.  You can use your favorite text editor of choice (`vim`, `nano`, `emacs`, etc.), or you can use the Cloud shell editor.  To launch this, you can either click the `Open Editor` button in the Cloud shell interface, or type `cloudshell edit <file>`, where you replace `<file>` with whatever file you're trying to edit.  This action gives you a Notepad-like environment with a file browser on the side.  Use this if you're unfamiliar with CLI-based text editing.

> Note: I will be using `vim` in all my demos.  Don't feel obligated to learn it, just be aware that's how I prefer to edit files.

## Codelabs, QuikLabs, and Colabs

This is a slight aside but I wanted to clarify the difference between these three "lab-ish" technologies we'll be mainly using.  You already have experience with Codelabs already if you did the VM setup assignment, however...

* [Codelabs](https://codelabs.developers.google.com/)
* [Quiklabs](https://www.qwiklabs.com/)
* [Colabs](https://colab.research.google.com/)

Codelabs are effectively tutorial-style manuals that walk you through a task.  These can be developed by anybody (and the [tools for doing so have been made open source](https://github.com/googlecodelabs/tools)) and focus on a particular topic.  We will be using a lot of these for our assignments.  Of note is that these are **free** to participate in.

Qwiklabs are **paid-for** labs that are similar in style to Codelabs, however they are better structured and generally will focus around a theme (called Quests).  Qwiklabs can be used to get badges that you can share on social media noting that you have experience with a particular topic.  There also tend to be videos associated with Quests as well.  Of note is that these are **not free**, however if you are enrolled in class with me you will receive credits to apply to Qwiklabs as needed.

Colabs are an interesting aside in that they are effectively Jupyter notebooks demonstrating some topic.  A Colab will typically have Markdown and executable code interspersed in a single document that you can interact with.  These are free to the point that you will be charged cloud credits to use (i.e., the executing code runs against your billing account).

## Additional Resources

* [Codelab: Getting Started with Cloud Shell & gcloud](https://codelabs.developers.google.com/codelabs/cloud-shell/#0)
* [Running gcloud Commands with Cloud Shell](https://cloud.google.com/shell/docs/running-gcloud-commands)
* [IaaS vs PaaS vs SaaS Enter the Ecommerce Vernacular: What You Need to Know, Examples & More](https://www.bigcommerce.com/blog/saas-vs-paas-vs-iaas/)
* [How Kubernetes Works](https://dzone.com/articles/how-kubernetes-works)

<hr size="1" />

*Where noted, the original content was provided by Google LLC and modified for the purpose of the course, without input or endorsement from Google LLC*.