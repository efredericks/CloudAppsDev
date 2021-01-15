> By the end of this module, you'll gain experience with geographic concerns and asynchronous processes.

> Module videos:
> * Core concepts
> * Geographic Concerns
> * Asynchronous processes

## Geographic Concerns

Let us assume you are working for a company that has offices worldwide.  Typically, you would need infrastructure spread throughout each geographic region to support company activities, including application servers, file servers, database servers, etc.  Basically, each location would need to be closely located to their servers and workstations to provide an acceptable quality of service to their users.

Naturally, this can become a massive orchestration nightmare if you're working in infrastructure!  How do you manage a worldwide network of servers, applications, and all the other technologies needed to keep a company moving forward?  Up to this point, you most likely would have local teams (and still will, going to the cloud doesn't reduce that need!) that each provide the local infrastructure necessary for each office.

![A worldwide map, according to those not geo-concerned (i.e., Pangea) (c/o TheVerge)](https://cdn.vox-cdn.com/thumbor/w86HpxoBVhRBnVcgICIM6ywdVXY=/0x0:739x508/1200x800/filters:focal(296x206:414x324)/cdn.vox-cdn.com/uploads/chorus_image/image/60083775/Screen_Shot_2018_06_15_at_9.23.03_AM.0.png "A worldwide map, according to those not geo-concerned (i.e., Pangea)")

> Figure 1: A worldwide map, according to those not geo-concerned (i.e., Pangea)

### Locations

The whole point of this diversion into world geography is to ensure that your clients/customers receive a satistfactory quality of service.  This quality can be noticed from application response times to geographically-relevant data.  For example, if an employee is trying to put together a project team (perhaps it is an Agile environment) and is searching the personnel directory for people with 10 years of full stack experience as well as 20 years of React experience (clearly, this was a bad joke), then you most likely would prefer to filter for employees/contracters that are nearby and can attend project meetings, meet in the break room for a coffee, etc.

> With times being what they are, this example probably doesn't hold much water anymore, does it?

Regardless, when developing cloud applications you will need to consider geographic concerns.  These concerns will mainly boil down to *where* you are serving your cloud services *from*.  For instance, when creating a new virtual machine you are given the option to select a region!  Or when creating an App Engine project you are given the option ... to select a region!

What could this mean?  Well, the *thing* you have created needs to be stored/hosted somewhere.  That somewhere is a cloud server in the region you specified.  Now, this concept applies to *all* cloud providers.  Again, you need servers to host all these nifty applications you're creating.  And, those servers need to be physically located somewhere, no matter how many layers of virtualization there are.  That machine that you are using to create will have actual, real-world concerns such as network latency.

To take the VM example from before, when you create a VM in a particular region you are hosting that VM on a server within that region.  Meaning, the users who will be interacting with that machine will experience a quality of service based on how far away they are from that machine.

Dig into your memory to your old networking classes.  The length of time it takes for a network packet to reach its destination is directly tied to how far away it is, right?  Same concept applies here!  There's no escaping the real world, unfortunately.

Now this is not to say that you can't do some neat tricks cloud-wise.  You can mirror servers, load balance across regions, etc., to provide all users with a similar experience.  The point stands though that, for lightning-fast response times, you still need to be near a server that is hosting your application!

Let's take a look at the big three in terms of regional availability.  *Note that companies spin up new data centers faster than I can keep a blog updated, so these maps will most likely change!*

![Google Cloud Regions (c/o Google)](/CloudAppsDev/assets/images/5-gcp-regions.png "Google Cloud Regions")

> Figure X: Google Cloud Regions

[Google Cloud Regions](https://cloud.google.com/about/locations/)

![AWS Regions (c/o Amazon)](/CloudAppsDev/assets/images/5-aws-regions.png "AWS Regions")

> Figure X: AWS Regions

[AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)

![Microsoft Azure Regions (c/o Microsoft)](https://azurecomcdn.azureedge.net/cvt-501c9a38819bd9ffc1ed855f2ed8b5db5e8936aed3e3a6732ff13f313a6c0ca4/images/shared/regions-map-desktop.svg "Microsoft Azure Regions")

> Figure X: Microsoft Azure Regions

[Microsoft Azure Regions](https://azure.microsoft.com/en-us/global-infrastructure/geographies/)

### Export Controls

## Additional Resources

* TBD

<hr size="1" />

*Where noted, the original content was provided by Google LLC and modified for the purpose of the course, without input or endorsement from Google LLC*.